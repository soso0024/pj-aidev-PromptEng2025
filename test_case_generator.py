"""
HumanEval Test Case Generator using Claude API

This script reads the HumanEval dataset, randomly selects problems,
and generates pytest-compatible test cases using Claude API.
"""

import json
import random
import os
import argparse
import re
import ast
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Tuple
import anthropic
from dotenv import load_dotenv
from model_utils import get_available_models, get_default_model


class TestCaseGenerator:
    def __init__(
        self,
        api_key: str,
        models: List[str] = None,
        include_docstring: bool = False,
        include_ast: bool = False,
        show_prompt: bool = False,
        enable_evaluation: bool = True,
        max_fix_attempts: int = 3,
        verbose_evaluation: bool = True,
        config_path: str = "models_config.json",
    ):
        """Initialize the test case generator with Claude API client."""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.problems = []

        # Load model configuration from external file
        self.config = self._load_model_config(config_path)
        self.model_mapping = {
            model: config["api_name"] for model, config in self.config["models"].items()
        }

        # Set default model if none provided
        if models is None:
            models = [self.config["default_model"]]

        # Validate models
        self.models = []
        for model in models:
            if model in self.model_mapping:
                self.models.append(model)
            else:
                raise ValueError(
                    f"Unsupported model: {model}. Supported models: {list(self.model_mapping.keys())}"
                )

        self.include_docstring = include_docstring
        self.include_ast = include_ast
        self.show_prompt = show_prompt
        self.enable_evaluation = enable_evaluation
        self.max_fix_attempts = max_fix_attempts
        self.verbose_evaluation = verbose_evaluation
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0

    def _load_model_config(self, config_path: str) -> Dict[str, Any]:
        """Load model configuration from JSON file."""
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Model configuration file not found: {config_path}"
            )
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in model configuration file: {e}")

    def get_model_folder_name(self, model: str) -> str:
        """Convert model name to a folder-friendly string."""
        return self.config["models"][model]["folder_name"]

    def load_dataset(self, file_path: str) -> None:
        """Load the HumanEval dataset from JSONL file."""
        print(f"Loading dataset from {file_path}...")

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    problem = json.loads(line.strip())
                    self.problems.append(problem)

        print(f"Loaded {len(self.problems)} problems from dataset")

    def select_random_problem(self) -> Dict[str, Any]:
        """Randomly select a problem from the dataset."""
        return random.choice(self.problems)

    def extract_function_signature(self, prompt: str, entry_point: str) -> str:
        """Extract just the function signature without docstring."""
        lines = prompt.split("\n")
        signature_lines = []
        in_signature = False

        for line in lines:
            if line.strip().startswith(f"def {entry_point}("):
                in_signature = True
                signature_lines.append(line)
            elif in_signature:
                if line.strip().startswith('"""') or line.strip().startswith("'''"):
                    # Stop at docstring
                    break
                elif (
                    line.strip()
                    and not line.startswith(" ")
                    and not line.startswith("\t")
                ):
                    # Stop at next top-level statement
                    break
                else:
                    signature_lines.append(line)
                    if line.strip().endswith(":"):
                        # End of function signature
                        break

        return "\n".join(signature_lines)

    def generate_ast_string(
        self, canonical_solution: str, prompt: str, entry_point: str
    ) -> str:
        """Generate a readable AST representation of the canonical solution."""
        try:
            # Extract function signature from the prompt more robustly
            # Find the def line and continue until we hit the docstring or end of signature
            lines = prompt.split("\n")
            signature_lines = []
            signature_started = False

            for line in lines:
                if line.strip().startswith(f"def {entry_point}("):
                    signature_started = True
                    signature_lines.append(line.strip())
                elif signature_started:
                    if line.strip().startswith('"""') or line.strip().startswith("'''"):
                        # Hit docstring, stop
                        break
                    elif line.strip().endswith(":") or line.strip() == "":
                        # End of signature or empty line
                        if line.strip().endswith(":"):
                            signature_lines.append(line.strip())
                        break
                    else:
                        signature_lines.append(line.strip())

            if not signature_lines:
                return "Error: Could not extract function signature"

            signature = " ".join(signature_lines)
            if not signature.endswith(":"):
                signature += ":"

            # Create complete function code
            full_function = f"{signature}\n{canonical_solution}"

            # Parse the AST
            tree = ast.parse(full_function)

            # Format the AST as a readable string
            return ast.dump(tree, indent=2)
        except Exception as e:
            return f"Error generating AST: {e}"

    def generate_prompt(self, problem: Dict[str, Any]) -> str:
        """Create a prompt for Claude to generate test cases."""

        if self.include_docstring:
            # Include full function signature with docstring
            function_info = problem["prompt"]
        else:
            # Include only function signature without docstring
            function_info = self.extract_function_signature(
                problem["prompt"], problem["entry_point"]
            )

        ast_section = ""
        if self.include_ast:
            ast_repr = self.generate_ast_string(
                problem["canonical_solution"], problem["prompt"], problem["entry_point"]
            )
            ast_section = f"""

AST representation of canonical solution:
```
{ast_repr}
```"""

        prompt = f"""Generate pytest test cases for this function. Return ONLY executable Python code, no explanations or markdown.

Function signature:
{function_info}

Canonical implementation:
```python
def {problem['entry_point']}({problem['prompt'].split('def ' + problem['entry_point'] + '(')[1].split(')')[0]}):
{problem['canonical_solution']}
```{ast_section}

Requirements:
- Return ONLY Python code that can be executed directly
- Include comprehensive test cases covering edge cases, normal cases, and error conditions
- Use pytest format
- Include necessary imports
- DO NOT include explanations, markdown, or the original function implementation
- DO NOT wrap code in ```python``` blocks
- IMPORTANT: When using @pytest.mark.parametrize, properly escape quotes in parameter values
- Use single quotes inside double quotes or vice versa, or use triple quotes for complex strings
- Example: @pytest.mark.parametrize("input,expected", [("test", True), ('another', False)])

Start your response with "import pytest" and include only executable Python test code:"""

        return prompt

    def clean_generated_code(self, raw_response: str) -> str:
        """Clean the generated response to extract only executable Python code."""
        # Remove markdown code blocks
        cleaned = re.sub(r"```python\s*\n?", "", raw_response)
        cleaned = re.sub(r"```\s*$", "", cleaned, flags=re.MULTILINE)

        # Remove explanatory text before the first import or function definition
        lines = cleaned.split("\n")
        code_lines = []
        code_started = False
        seen_imports = set()  # Track imports to avoid duplicates

        for line in lines:
            stripped_line = line.strip()

            # Start collecting lines when we see imports, decorators, or function definitions
            if not code_started and (
                stripped_line.startswith("import ")
                or stripped_line.startswith("from ")
                or stripped_line.startswith("def ")
                or stripped_line.startswith("@pytest")
                or stripped_line.startswith("@")
            ):
                code_started = True

            if code_started:
                # Check for duplicate imports
                if stripped_line.startswith("import ") or stripped_line.startswith(
                    "from "
                ):
                    if stripped_line not in seen_imports:
                        seen_imports.add(stripped_line)
                        code_lines.append(line)
                    # Skip duplicate imports
                else:
                    code_lines.append(line)

        # Try to validate the code by checking for syntax errors
        try:
            result = "\n".join(code_lines).strip()
            # Basic validation - try to compile the code
            compile(result, "<string>", "exec")

            # If successful and contains test functions, return it
            if result and "def test_" in result:
                return result
        except SyntaxError:
            # If there's a syntax error, try to return the original response
            pass

        # Fallback: if validation fails, return the original response
        return raw_response

    def display_prompt_and_confirm(self, prompt: str) -> bool:
        """Display the prompt to user and ask for confirmation."""
        print("\n" + "=" * 80)
        print("PROMPT PREVIEW")
        print("=" * 80)
        print(prompt)
        print("=" * 80)

        # Estimate token count (rough approximation: 1 token ≈ 4 chars)
        estimated_tokens = len(prompt) // 4
        # Use the first model for cost estimation in prompt preview
        first_model = self.models[0] if self.models else self.config["default_model"]
        estimated_cost = (estimated_tokens / 1000) * self.config["models"][first_model][
            "pricing"
        ]["input_per_1k"]

        print(f"Estimated input tokens: {estimated_tokens}")
        print(f"Estimated input cost: ${estimated_cost:.6f}")
        print("=" * 80)

        while True:
            response = input("\nProceed with this prompt? (y/n/q): ").lower().strip()
            if response in ["y", "yes"]:
                return True
            elif response in ["n", "no"]:
                print("Prompt rejected. Exiting...")
                return False
            elif response in ["q", "quit"]:
                print("Quitting...")
                return False
            else:
                print("Please enter 'y' (yes), 'n' (no), or 'q' (quit)")

    def calculate_cost(
        self, input_tokens: int, output_tokens: int, model: str
    ) -> float:
        """Calculate the cost based on token usage and model."""
        pricing = self.config["models"][model]["pricing"]
        input_cost = (input_tokens / 1000) * pricing["input_per_1k"]
        output_cost = (output_tokens / 1000) * pricing["output_per_1k"]
        return input_cost + output_cost

    def get_usage_stats(self) -> Dict[str, Any]:
        """Get current usage statistics."""
        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "total_cost_usd": round(self.total_cost, 6),
        }

    def rename_file_with_result(
        self, original_filepath: str, evaluation_success: bool
    ) -> str:
        """Rename the test file to include success/failure status."""
        original_path = Path(original_filepath)

        # Get the current filename without extension
        stem = original_path.stem

        # Remove any existing success/failure suffix
        if stem.endswith("_success") or stem.endswith("_false"):
            stem = "_".join(stem.split("_")[:-1])

        # Add the new suffix based on evaluation result
        suffix = "success" if evaluation_success else "false"
        new_stem = f"{stem}_{suffix}"

        # Create new filepath
        new_filepath = original_path.parent / f"{new_stem}{original_path.suffix}"

        # Rename the file
        if original_path.exists():
            original_path.rename(new_filepath)
            print(f"📝 Renamed {original_path.name} → {new_filepath.name}")

        return str(new_filepath)

    def update_final_stats(
        self,
        filepath: str,
        problem: Dict[str, Any],
        evaluation_success: bool,
        fix_attempts_used: int,
        code_coverage: float = 0.0,
    ) -> str:
        """Update the stats file with final statistics after evaluation process.

        Returns:
            str: The final filepath (potentially renamed)
        """
        # Rename file with evaluation result
        final_filepath = self.rename_file_with_result(filepath, evaluation_success)

        # Also rename the stats file to match
        original_stats_filepath = Path(filepath).with_suffix(".stats.json")
        final_stats_filepath = Path(final_filepath).with_suffix(".stats.json")

        final_stats = self.get_usage_stats()
        final_stats.update(
            {
                "task_id": problem["task_id"],
                "generated_file": str(final_filepath),
                "evaluation_enabled": self.enable_evaluation,
                "evaluation_success": evaluation_success,
                "fix_attempts_used": fix_attempts_used,
                "max_fix_attempts": self.max_fix_attempts,
                "code_coverage_percent": code_coverage,
            }
        )

        with open(final_stats_filepath, "w", encoding="utf-8") as f:
            json.dump(final_stats, f, indent=2)

        # Remove old stats file if it's different
        if (
            original_stats_filepath != final_stats_filepath
            and original_stats_filepath.exists()
        ):
            original_stats_filepath.unlink()

        print(f"📊 Final stats saved to {final_stats_filepath}")
        return str(final_filepath)

    def display_pytest_errors(self, error_output: str, attempt: int) -> None:
        """Display pytest errors in a readable format."""
        if not self.verbose_evaluation:
            return

        print(f"\n{'='*80}")
        print(f"📋 PYTEST ERROR DETAILS - Attempt {attempt}")
        print(f"{'='*80}")

        # Parse and display relevant parts of pytest output
        lines = error_output.split("\n")
        in_failures = False
        in_errors = False

        for line in lines:
            # Show test results summary
            if "FAILED" in line and "::" in line:
                print(f"❌ {line}")
            elif "PASSED" in line and "::" in line:
                print(f"✅ {line}")
            elif "=== FAILURES ===" in line:
                in_failures = True
                print(f"\n🔍 FAILURE DETAILS:")
                print("-" * 40)
            elif "=== ERRORS ===" in line:
                in_errors = True
                print(f"\n🚨 ERROR DETAILS:")
                print("-" * 40)
            elif in_failures and line.startswith("="):
                if "short test summary" in line:
                    in_failures = False
                    print("\n" + "=" * 40)
                else:
                    print(line)
            elif in_failures:
                print(line)
            elif (
                "SyntaxError" in line
                or "ImportError" in line
                or "ModuleNotFoundError" in line
            ):
                print(f"🐛 {line}")

        print(f"{'='*80}\n")

    def display_fix_prompt(self, prompt: str, attempt: int) -> None:
        """Display the fix prompt being sent to LLM."""
        if not self.verbose_evaluation:
            return

        print(f"\n{'='*80}")
        print(f"🤖 LLM FIX PROMPT - Attempt {attempt}")
        print(f"{'='*80}")
        print(prompt)
        print(f"{'='*80}")

        # Ask user if they want to proceed (optional)
        if self.show_prompt:
            while True:
                response = (
                    input(f"\nProceed with fix attempt {attempt}? (y/n/q): ")
                    .lower()
                    .strip()
                )
                if response in ["y", "yes"]:
                    break
                elif response in ["n", "no"]:
                    print("Skipping fix attempt...")
                    return False
                elif response in ["q", "quit"]:
                    print("Quitting evaluation...")
                    return False
                else:
                    print("Please enter 'y' (yes), 'n' (no), or 'q' (quit)")

        return True

    def display_fix_response(self, response: str, attempt: int) -> None:
        """Display the LLM's fix response."""
        if not self.verbose_evaluation:
            return

        print(f"\n{'='*80}")
        print(f"🔧 LLM FIX RESPONSE - Attempt {attempt}")
        print(f"{'='*80}")

        # Show first few lines and last few lines of the response
        lines = response.split("\n")
        if len(lines) <= 20:
            print(response)
        else:
            print("\n".join(lines[:10]))
            print(f"\n... ({len(lines) - 20} lines omitted) ...\n")
            print("\n".join(lines[-10:]))

        print(f"{'='*80}\n")

    def generate_test_cases(self, problem: Dict[str, Any], model: str) -> str:
        """Generate test cases using Claude API."""
        prompt = self.generate_prompt(problem)

        print(f"Generating test cases for {problem['task_id']} using {model}...")

        # Show prompt and get confirmation if requested
        if self.show_prompt:
            if not self.display_prompt_and_confirm(prompt):
                return ""

        try:
            response = self.client.messages.create(
                model=self.model_mapping[model],
                max_tokens=2000,
                temperature=0.0,  # A temperature of 0.0 results in the most deterministic and consistent responses, as the model will consistently choose the most probable words and sequences.
                messages=[{"role": "user", "content": prompt}],
            )

            # Track token usage and cost
            usage = response.usage
            input_tokens = usage.input_tokens
            output_tokens = usage.output_tokens

            self.total_input_tokens += input_tokens
            self.total_output_tokens += output_tokens

            cost = self.calculate_cost(input_tokens, output_tokens, model)
            self.total_cost += cost

            raw_response = response.content[0].text
            return self.clean_generated_code(raw_response)

        except Exception as e:
            print(f"Error generating test cases: {e}")
            return ""

    def save_test_cases(
        self, problem: Dict[str, Any], test_cases: str, output_dir: str, model: str
    ) -> str:
        """Save generated test cases to a file."""
        # Create model-specific output directory
        model_folder = self.get_model_folder_name(model)
        model_output_dir = f"{output_dir}_{model_folder}"
        output_path = Path(model_output_dir)
        output_path.mkdir(exist_ok=True)

        # Create filename from task_id (no model name in filename since folder identifies model)
        base_name = f"test_{problem['task_id'].replace('/', '_').lower()}"
        filename_parts = [base_name]

        if self.include_docstring:
            filename_parts.append("docstring")
        if self.include_ast:
            filename_parts.append("ast")

        filename = f"{'_'.join(filename_parts)}.py"
        filepath = output_path / filename

        # Add the function implementation and test cases
        full_content = f"""# Test cases for {problem['task_id']}
# Generated using Claude API

{problem['prompt']}
{problem['canonical_solution']}

# Generated test cases:
{test_cases}
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)

        print(f"Test cases saved to {filepath}")

        # Also save usage stats alongside the test file
        stats_filepath = filepath.with_suffix(".stats.json")
        stats = self.get_usage_stats()
        stats["task_id"] = problem["task_id"]
        stats["generated_file"] = str(filepath)

        with open(stats_filepath, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)

        return str(filepath)

    def run_pytest(self, test_file_path: str) -> Tuple[bool, str, float]:
        """Run pytest on the test file and return (success, error_output, coverage_percentage)."""

        # Use absolute path and run from project root
        abs_path = Path(test_file_path).resolve()
        cmd = ["pytest", str(abs_path), "--cov", "-v"]

        try:
            # Run pytest and capture output
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,  # 60 second timeout
                cwd=Path.cwd(),  # Run from current working directory
            )

            # Check if tests passed (return code 0)
            success = result.returncode == 0

            # Combine stdout and stderr for complete error information
            output = f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"

            # Extract coverage percentage from pytest output
            coverage_percentage = 0.0
            if result.stdout:
                # Look for coverage percentage in format like "TOTAL    100%"
                coverage_match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", result.stdout)
                if coverage_match:
                    coverage_percentage = float(coverage_match.group(1))

            return success, output, coverage_percentage

        except subprocess.TimeoutExpired:
            return False, "Error: pytest execution timed out after 60 seconds", 0.0
        except Exception as e:
            return False, f"Error running pytest: {str(e)}", 0.0

    def generate_fix_prompt(
        self,
        original_code: str,
        error_output: str,
        attempt: int,
        problem: Dict[str, Any],
    ) -> str:
        """Generate a prompt to fix test case errors with white box testing approach."""
        return f"""The following test code has errors when running pytest. Please fix the issues and return ONLY the corrected Python code, no explanations or markdown.

FUNCTION BEING TESTED (WHITE BOX):
```python
{problem['prompt']}
{problem['canonical_solution']}
```

CURRENT TEST CODE WITH ERRORS:
```python
{original_code}
```

PYTEST ERROR OUTPUT:
```
{error_output}
```

This is attempt {attempt} of {self.max_fix_attempts}.

Requirements:
- Return ONLY executable Python code that can be run directly
- Fix all syntax errors, import errors, and test failures
- Use the provided function implementation to understand expected behavior
- Ensure tests properly validate the function's actual behavior
- Maintain comprehensive test coverage
- DO NOT include explanations, markdown, or code blocks
- DO NOT wrap code in ```python``` blocks
- DO NOT include the function implementation in your response (it's already in the file)
- Start your response with the corrected imports

Corrected code:"""

    def fix_test_cases(
        self,
        test_code: str,
        error_output: str,
        attempt: int,
        problem: Dict[str, Any],
        model: str,
    ) -> str:
        """Use LLM to fix test case errors."""
        fix_prompt = self.generate_fix_prompt(test_code, error_output, attempt, problem)

        # Display the fix prompt if verbose mode is enabled
        should_proceed = self.display_fix_prompt(fix_prompt, attempt)
        if should_proceed is False:  # User chose to skip
            return test_code

        try:
            print(f"🤖 Sending fix request to LLM (attempt {attempt}) using {model}...")

            response = self.client.messages.create(
                model=self.model_mapping[model],
                max_tokens=3000,
                temperature=0.0,
                messages=[{"role": "user", "content": fix_prompt}],
            )

            # Track token usage
            usage = response.usage
            self.total_input_tokens += usage.input_tokens
            self.total_output_tokens += usage.output_tokens

            cost = self.calculate_cost(usage.input_tokens, usage.output_tokens, model)
            self.total_cost += cost

            if self.verbose_evaluation:
                print(
                    f"💰 Fix attempt {attempt} cost: ${cost:.6f} (Input: {usage.input_tokens}, Output: {usage.output_tokens})"
                )

            raw_response = response.content[0].text
            cleaned_response = self.clean_generated_code(raw_response)

            # Display the LLM's fix response
            self.display_fix_response(cleaned_response, attempt)

            return cleaned_response

        except Exception as e:
            print(f"❌ Error fixing test cases: {e}")
            return test_code  # Return original code if fixing fails

    def evaluate_and_fix_tests(
        self, test_file_path: str, problem: Dict[str, Any], model: str
    ) -> Tuple[bool, int, float]:
        """Evaluate test file with pytest and fix errors iteratively.

        Returns:
            Tuple[bool, int, float]: (success, attempts_used, final_coverage)
        """
        if not self.enable_evaluation:
            return True, 0, 0.0

        print(f"🧪 Evaluating test file: {Path(test_file_path).name}")

        final_coverage = 0.0

        for attempt in range(1, self.max_fix_attempts + 1):
            # Run pytest
            success, error_output, coverage = self.run_pytest(test_file_path)
            final_coverage = coverage

            if success:
                print(
                    f"✅ Tests passed on attempt {attempt} (Coverage: {coverage:.1f}%)"
                )
                return True, attempt - 1, final_coverage

            print(f"❌ Tests failed on attempt {attempt}")

            # Display detailed error information
            self.display_pytest_errors(error_output, attempt)

            if attempt < self.max_fix_attempts:
                print(f"🔧 Attempting to fix errors...")

                # Read current test file content
                with open(test_file_path, "r", encoding="utf-8") as f:
                    current_content = f.read()

                # Extract just the test code part (after "# Generated test cases:")
                test_code_start = current_content.find("# Generated test cases:\n")
                if test_code_start != -1:
                    test_code = current_content[
                        test_code_start + len("# Generated test cases:\n") :
                    ]
                else:
                    test_code = current_content

                # Get fixed version from LLM
                fixed_code = self.fix_test_cases(
                    test_code, error_output, attempt, problem, model
                )

                # Update the test file with fixed code
                base_content = (
                    current_content[:test_code_start]
                    if test_code_start != -1
                    else f"""# Test cases for {problem['task_id']}
# Generated using Claude API

{problem['prompt']}
{problem['canonical_solution']}

"""
                )

                updated_content = (
                    base_content + "# Generated test cases:\n" + fixed_code
                )

                with open(test_file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

                print(f"📝 Updated test file with fixes")
            else:
                print(f"🚫 Maximum fix attempts ({self.max_fix_attempts}) reached")
                print("Final error output:")
                print(error_output)

        return False, self.max_fix_attempts, final_coverage

    def _generate_and_evaluate_test_cases(
        self, problem: Dict[str, Any], output_dir: str = "generated_tests"
    ) -> List[str]:
        """Generate test cases for a problem using all selected models, evaluate them, and return final filepaths."""
        print(f"Selected problem: {problem['task_id']}")
        print(
            f"Generating test cases using {len(self.models)} model(s): {', '.join(self.models)}"
        )

        final_filepaths = []
        model_results = {}

        for model in self.models:
            print(f"\n{'='*60}")
            print(f"Processing with model: {model}")
            print(f"{'='*60}")

            test_cases = self.generate_test_cases(problem, model)
            if not test_cases:
                print(f"❌ Failed to generate test cases for model {model}")
                model_results[model] = {"status": "generation_failed", "filepath": None}
                continue

            filepath = self.save_test_cases(problem, test_cases, output_dir, model)

            # Run evaluation and fix cycle if enabled
            evaluation_success = True
            fix_attempts_used = 0
            code_coverage = 0.0

            if self.enable_evaluation:
                evaluation_success, fix_attempts_used, code_coverage = (
                    self.evaluate_and_fix_tests(filepath, problem, model)
                )
                if evaluation_success:
                    print(
                        f"🎉 Test generation and evaluation completed successfully for {model}!"
                    )
                    model_results[model] = {
                        "status": "success",
                        "filepath": filepath,
                        "coverage": code_coverage,
                    }
                else:
                    print(
                        f"⚠️  Test generation completed but evaluation failed for {model}"
                    )
                    model_results[model] = {
                        "status": "evaluation_failed",
                        "filepath": filepath,
                        "coverage": code_coverage,
                    }
            else:
                model_results[model] = {
                    "status": "generated_no_eval",
                    "filepath": filepath,
                }

            # Update final stats after complete process and get final filepath
            final_filepath = self.update_final_stats(
                filepath, problem, evaluation_success, fix_attempts_used, code_coverage
            )

            final_filepaths.append(final_filepath)

        # Print summary of model results
        self._print_model_summary(model_results)

        return final_filepaths

    def _print_model_summary(self, model_results: Dict[str, Dict[str, Any]]) -> None:
        """Print a summary of results for all models."""
        print(f"\n{'='*60}")
        print(f"MODEL PROCESSING SUMMARY")
        print(f"{'='*60}")

        successful_models = []
        failed_generation = []
        failed_evaluation = []
        no_eval_models = []

        for model, result in model_results.items():
            status = result["status"]
            if status == "success":
                coverage = result.get("coverage", 0)
                successful_models.append(f"{model} (Coverage: {coverage:.1f}%)")
            elif status == "generation_failed":
                failed_generation.append(model)
            elif status == "evaluation_failed":
                coverage = result.get("coverage", 0)
                failed_evaluation.append(f"{model} (Coverage: {coverage:.1f}%)")
            elif status == "generated_no_eval":
                no_eval_models.append(model)

        if successful_models:
            print(f"✅ Successfully completed ({len(successful_models)}):")
            for model in successful_models:
                print(f"   • {model}")

        if no_eval_models:
            print(f"📝 Generated without evaluation ({len(no_eval_models)}):")
            for model in no_eval_models:
                print(f"   • {model}")

        if failed_evaluation:
            print(f"⚠️  Generated but evaluation failed ({len(failed_evaluation)}):")
            for model in failed_evaluation:
                print(f"   • {model}")

        if failed_generation:
            print(f"❌ Failed to generate ({len(failed_generation)}):")
            for model in failed_generation:
                print(f"   • {model}")

        total_attempted = len(model_results)
        total_with_output = len([r for r in model_results.values() if r["filepath"]])
        print(
            f"\n📊 Overall: {total_with_output}/{total_attempted} models produced test files"
        )

    def generate_for_random_problem(
        self, output_dir: str = "generated_tests"
    ) -> List[str]:
        """Generate test cases for a randomly selected problem."""
        if not self.problems:
            raise ValueError("No problems loaded. Call load_dataset() first.")

        problem = self.select_random_problem()
        return self._generate_and_evaluate_test_cases(problem, output_dir)

    def generate_for_specific_problem(
        self, task_id: str, output_dir: str = "generated_tests"
    ) -> List[str]:
        """Generate test cases for a specific problem by task_id."""
        problem = next((p for p in self.problems if p["task_id"] == task_id), None)
        if not problem:
            raise ValueError(f"Problem {task_id} not found in dataset")

        return self._generate_and_evaluate_test_cases(problem, output_dir)


def main():
    # Load environment variables from .env file
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Generate test cases for HumanEval problems using Claude API"
    )
    parser.add_argument(
        "--dataset",
        default="dataset/HumanEval.jsonl",
        help="Path to HumanEval dataset file",
    )
    parser.add_argument(
        "--output-dir",
        default="generated_tests",
        help="Output directory for test files",
    )
    parser.add_argument(
        "--task-id", help="Specific task ID to generate tests for (optional)"
    )
    parser.add_argument("--api-key", help="Claude API key (or set in .env file)")
    parser.add_argument(
        "--models",
        nargs="+",
        default=[get_default_model()],
        choices=get_available_models(),
        help="Claude model(s) to use for test generation (can specify multiple)",
    )
    parser.add_argument(
        "--include-docstring",
        action="store_true",
        help="Include function docstring in prompt (default: only function signature)",
    )
    parser.add_argument(
        "--include-ast",
        action="store_true",
        help="Include AST of canonical solution in prompt",
    )
    parser.add_argument(
        "--show-prompt",
        action="store_true",
        help="Display the prompt before sending to LLM and ask for confirmation",
    )
    parser.add_argument(
        "--disable-evaluation",
        action="store_true",
        help="Disable automatic evaluation and fixing of generated tests",
    )
    parser.add_argument(
        "--max-fix-attempts",
        type=int,
        default=3,
        help="Maximum number of attempts to fix test errors (default: 3)",
    )
    parser.add_argument(
        "--quiet-evaluation",
        action="store_true",
        help="Disable verbose output during error fixing process",
    )

    args = parser.parse_args()

    # Get API key from argument, environment, or .env file
    api_key = args.api_key or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Please provide Claude API key via:")
        print("  1. --api-key argument")
        print("  2. ANTHROPIC_API_KEY environment variable")
        print("  3. Set ANTHROPIC_API_KEY in .env file")
        return 1

    try:
        # Initialize generator
        generator = TestCaseGenerator(
            api_key,
            models=args.models,
            include_docstring=args.include_docstring,
            include_ast=args.include_ast,
            show_prompt=args.show_prompt,
            enable_evaluation=not args.disable_evaluation,
            max_fix_attempts=args.max_fix_attempts,
            verbose_evaluation=not args.quiet_evaluation,
        )

        # Load dataset
        generator.load_dataset(args.dataset)

        # Generate test cases
        if args.task_id:
            output_files = generator.generate_for_specific_problem(
                args.task_id, args.output_dir
            )
        else:
            output_files = generator.generate_for_random_problem(args.output_dir)

        # Check if any files were generated
        if not output_files:
            print(f"\n❌ No test cases were generated successfully for any model.")
            return 1

        # Display final usage statistics
        stats = generator.get_usage_stats()

        if output_files:
            print(f"\n✅ Generated test files!")
            print(f"📁 Output folders and files ({len(output_files)}):")

            # Group files by folder
            folders = {}
            for output_file in output_files:
                folder = Path(output_file).parent.name
                filename = Path(output_file).name
                if folder not in folders:
                    folders[folder] = []
                folders[folder].append(filename)

            for i, (folder, files) in enumerate(folders.items(), 1):
                print(f"  {i}. {folder}/")
                for file in files:
                    print(f"     └── {file}")

            print(f"\n📊 Token Usage & Cost:")
            print(f"  Input tokens: {stats['total_input_tokens']}")
            print(f"  Output tokens: {stats['total_output_tokens']}")
            print(f"  Total tokens: {stats['total_tokens']}")
            print(f"  Total cost: ${stats['total_cost_usd']}")
            print(f"\nTo run the tests:")
            if len(folders) == 1:
                folder_name = list(folders.keys())[0]
                print(f"  cd {folder_name}")
                print(f"  pytest . -v --cov")
            else:
                print(f"  # Run tests from specific model folder:")
                for folder in folders.keys():
                    print(f"  cd {folder} && pytest . -v --cov")
                print(f"  # Or run all tests from parent directory:")
                print(f"  pytest generated_tests_*/ -v --cov")
        else:
            print(f"\n❌ No test files were generated successfully.")
            print(f"📊 Token Usage & Cost:")
            print(f"  Input tokens: {stats['total_input_tokens']}")
            print(f"  Output tokens: {stats['total_output_tokens']}")
            print(f"  Total tokens: {stats['total_tokens']}")
            print(f"  Total cost: ${stats['total_cost_usd']}")

        return 0

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
