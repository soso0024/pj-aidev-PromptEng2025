#!/usr/bin/env python3
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
from pathlib import Path
from typing import Dict, List, Any
import anthropic
from dotenv import load_dotenv


class TestCaseGenerator:
    def __init__(
        self,
        api_key: str,
        include_docstring: bool = False,
        include_ast: bool = False,
        show_prompt: bool = False,
    ):
        """Initialize the test case generator with Claude API client."""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.problems = []
        self.include_docstring = include_docstring
        self.include_ast = include_ast
        self.show_prompt = show_prompt
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0

        # Claude 3.5 Sonnet pricing (as of 2024)
        self.input_cost_per_1k_tokens = 0.003  # $3 per 1M tokens
        self.output_cost_per_1k_tokens = 0.015  # $15 per 1M tokens

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

        for line in lines:
            # Start collecting lines when we see imports, decorators, or function definitions
            if not code_started and (
                line.strip().startswith("import ")
                or line.strip().startswith("from ")
                or line.strip().startswith("def ")
                or line.strip().startswith("@pytest")
                or line.strip().startswith("@")
            ):
                code_started = True

            if code_started:
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
        estimated_cost = (estimated_tokens / 1000) * self.input_cost_per_1k_tokens

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

    def calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate the cost based on token usage."""
        input_cost = (input_tokens / 1000) * self.input_cost_per_1k_tokens
        output_cost = (output_tokens / 1000) * self.output_cost_per_1k_tokens
        return input_cost + output_cost

    def get_usage_stats(self) -> Dict[str, Any]:
        """Get current usage statistics."""
        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "total_cost_usd": round(self.total_cost, 6),
        }

    def generate_test_cases(self, problem: Dict[str, Any]) -> str:
        """Generate test cases using Claude API."""
        prompt = self.generate_prompt(problem)

        print(f"Generating test cases for {problem['task_id']}...")

        # Show prompt and get confirmation if requested
        if self.show_prompt:
            if not self.display_prompt_and_confirm(prompt):
                return ""

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
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

            cost = self.calculate_cost(input_tokens, output_tokens)
            self.total_cost += cost

            raw_response = response.content[0].text
            return self.clean_generated_code(raw_response)

        except Exception as e:
            print(f"Error generating test cases: {e}")
            return ""

    def save_test_cases(
        self, problem: Dict[str, Any], test_cases: str, output_dir: str
    ) -> str:
        """Save generated test cases to a file."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Create filename from task_id
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

    def generate_for_random_problem(self, output_dir: str = "generated_tests") -> str:
        """Generate test cases for a randomly selected problem."""
        if not self.problems:
            raise ValueError("No problems loaded. Call load_dataset() first.")

        problem = self.select_random_problem()
        print(f"Selected problem: {problem['task_id']}")

        test_cases = self.generate_test_cases(problem)
        if test_cases:
            return self.save_test_cases(problem, test_cases, output_dir)
        else:
            raise RuntimeError("Failed to generate test cases")

    def generate_for_specific_problem(
        self, task_id: str, output_dir: str = "generated_tests"
    ) -> str:
        """Generate test cases for a specific problem by task_id."""
        problem = next((p for p in self.problems if p["task_id"] == task_id), None)
        if not problem:
            raise ValueError(f"Problem {task_id} not found in dataset")

        print(f"Selected problem: {problem['task_id']}")

        test_cases = self.generate_test_cases(problem)
        if test_cases:
            return self.save_test_cases(problem, test_cases, output_dir)
        else:
            raise RuntimeError("Failed to generate test cases")


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
            include_docstring=args.include_docstring,
            include_ast=args.include_ast,
            show_prompt=args.show_prompt,
        )

        # Load dataset
        generator.load_dataset(args.dataset)

        # Generate test cases
        if args.task_id:
            output_file = generator.generate_for_specific_problem(
                args.task_id, args.output_dir
            )
        else:
            output_file = generator.generate_for_random_problem(args.output_dir)

        # Display final usage statistics
        stats = generator.get_usage_stats()

        print(f"\n✅ Successfully generated test cases!")
        print(f"📁 Output file: {output_file}")
        print(f"\n📊 Token Usage & Cost:")
        print(f"  Input tokens: {stats['total_input_tokens']}")
        print(f"  Output tokens: {stats['total_output_tokens']}")
        print(f"  Total tokens: {stats['total_tokens']}")
        print(f"  Total cost: ${stats['total_cost_usd']}")
        print(f"\nTo run the tests:")
        print(f"  cd {args.output_dir}")
        print(f"  pytest {Path(output_file).name} -v --cov")

        return 0

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
