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
from pathlib import Path
from typing import Dict, List, Any
import anthropic


class TestCaseGenerator:
    def __init__(self, api_key: str):
        """Initialize the test case generator with Claude API client."""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.problems = []
        
    def load_dataset(self, file_path: str) -> None:
        """Load the HumanEval dataset from JSONL file."""
        print(f"Loading dataset from {file_path}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
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
        prompt = f"""You are a Python testing expert. I need you to create comprehensive pytest test cases for the following function.

Function signature and description:
{problem['prompt']}

Canonical implementation:
```python
def {problem['entry_point']}({problem['prompt'].split('def ' + problem['entry_point'] + '(')[1].split(')')[0]}):
{problem['canonical_solution']}
```

Please generate pytest test cases that:
1. Test edge cases and boundary conditions
2. Test normal use cases
3. Test error conditions if applicable
4. Provide good code coverage
5. Use descriptive test function names

Format your response as a complete Python test file that can be run with pytest. Include only the test functions, imports, and any necessary fixtures. Do not include the original function implementation.

Example format:
```python
import pytest
from your_module import {problem['entry_point']}

def test_{problem['entry_point']}_basic_cases():
    # Test basic functionality
    pass

def test_{problem['entry_point']}_edge_cases():
    # Test edge cases
    pass
```

Generate comprehensive test cases now:"""
        
        return prompt
    
    def generate_test_cases(self, problem: Dict[str, Any]) -> str:
        """Generate test cases using Claude API."""
        prompt = self.generate_prompt(problem)
        
        print(f"Generating test cases for {problem['task_id']}...")
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                temperature=0.1,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text
            
        except Exception as e:
            print(f"Error generating test cases: {e}")
            return ""
    
    def save_test_cases(self, problem: Dict[str, Any], test_cases: str, output_dir: str) -> str:
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
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"Test cases saved to {filepath}")
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
    
    def generate_for_specific_problem(self, task_id: str, output_dir: str = "generated_tests") -> str:
        """Generate test cases for a specific problem by task_id."""
        problem = next((p for p in self.problems if p['task_id'] == task_id), None)
        if not problem:
            raise ValueError(f"Problem {task_id} not found in dataset")
        
        print(f"Selected problem: {problem['task_id']}")
        
        test_cases = self.generate_test_cases(problem)
        if test_cases:
            return self.save_test_cases(problem, test_cases, output_dir)
        else:
            raise RuntimeError("Failed to generate test cases")


def main():
    parser = argparse.ArgumentParser(description="Generate test cases for HumanEval problems using Claude API")
    parser.add_argument("--dataset", default="HumanEval.jsonl", help="Path to HumanEval dataset file")
    parser.add_argument("--output-dir", default="generated_tests", help="Output directory for test files")
    parser.add_argument("--task-id", help="Specific task ID to generate tests for (optional)")
    parser.add_argument("--api-key", help="Claude API key (or set ANTHROPIC_API_KEY env var)")
    
    args = parser.parse_args()
    
    # Get API key from argument or environment
    api_key = args.api_key or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Please provide Claude API key via --api-key argument or ANTHROPIC_API_KEY environment variable")
        return 1
    
    try:
        # Initialize generator
        generator = TestCaseGenerator(api_key)
        
        # Load dataset
        generator.load_dataset(args.dataset)
        
        # Generate test cases
        if args.task_id:
            output_file = generator.generate_for_specific_problem(args.task_id, args.output_dir)
        else:
            output_file = generator.generate_for_random_problem(args.output_dir)
        
        print(f"\n✅ Successfully generated test cases!")
        print(f"📁 Output file: {output_file}")
        print(f"\nTo run the tests:")
        print(f"  cd {args.output_dir}")
        print(f"  pytest {Path(output_file).name} -v --cov")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())