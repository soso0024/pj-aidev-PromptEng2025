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
from pathlib import Path
from typing import Dict, List, Any
import anthropic
from dotenv import load_dotenv


class TestCaseGenerator:
    def __init__(self, api_key: str):
        """Initialize the test case generator with Claude API client."""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.problems = []
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

    def generate_prompt(self, problem: Dict[str, Any]) -> str:
        """Create a prompt for Claude to generate test cases."""
        prompt = f"""Generate pytest test cases for this function. Return ONLY executable Python code, no explanations or markdown.

Function signature and description:
{problem['prompt']}

Canonical implementation:
```python
def {problem['entry_point']}({problem['prompt'].split('def ' + problem['entry_point'] + '(')[1].split(')')[0]}):
{problem['canonical_solution']}
```

Requirements:
- Return ONLY Python code that can be executed directly
- Include comprehensive test cases covering edge cases, normal cases, and error conditions
- Use pytest format
- Include necessary imports
- DO NOT include explanations, markdown, or the original function implementation
- DO NOT wrap code in ```python``` blocks

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
            # Start collecting lines when we see imports or function definitions
            if not code_started and (
                line.strip().startswith("import ")
                or line.strip().startswith("from ")
                or line.strip().startswith("def ")
                or line.strip().startswith("@")
            ):
                code_started = True

            if code_started:
                code_lines.append(line)

        # Remove explanatory text after the last function/code
        final_code = []
        for line in code_lines:
            # Stop at explanatory text (lines that are clearly not code)
            if (
                line.strip()
                and not line.strip().startswith("#")
                and not line.strip().startswith("import")
                and not line.strip().startswith("from")
                and not line.strip().startswith("def")
                and not line.strip().startswith("@")
                and not line.strip().startswith("assert")
                and not line.strip().startswith("with")
                and not line.strip().startswith("if")
                and not line.strip().startswith("for")
                and not line.strip().startswith("return")
                and not line.strip().startswith("yield")
                and not line.strip().startswith("raise")
                and not line.strip().startswith("try")
                and not line.strip().startswith("except")
                and not line.strip().startswith("finally")
                and not line.strip().startswith("while")
                and not line.strip().startswith("elif")
                and not line.strip().startswith("else")
                and not line.strip().startswith("pass")
                and not line.strip().startswith("break")
                and not line.strip().startswith("continue")
                and not line.strip().startswith("class")
                and not line.strip().startswith('"""')
                and not line.strip().startswith("'''")
                and not "=" in line
                and not line.strip().endswith(":")
                and not line.strip().startswith(")")
            ):
                # This looks like explanatory text, stop here
                break
            final_code.append(line)

        result = "\n".join(final_code).strip()

        # If the result is empty or doesn't contain test functions, return the original
        if not result or "def test_" not in result:
            return raw_response

        return result

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

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                temperature=0.1,
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

            print(f"  Input tokens: {input_tokens}")
            print(f"  Output tokens: {output_tokens}")
            print(f"  Cost: ${cost:.6f}")

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
        filename = f"test_{problem['task_id'].replace('/', '_').lower()}.py"
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
        generator = TestCaseGenerator(api_key)

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
