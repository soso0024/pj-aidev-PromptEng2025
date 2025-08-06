#!/usr/bin/env python3
"""
Problem Classification Module

Handles automatic classification of HumanEval problems based on complexity
and algorithm types using AST analysis and keyword detection.
"""

import json
import ast
import textwrap
from pathlib import Path
from typing import Dict, List, Any
from collections import Counter


class ProblemClassifier:
    """Handles classification of HumanEval problems by complexity and algorithm type."""
    
    def __init__(self, dataset_path: str = "dataset/HumanEval.jsonl"):
        """Initialize the classifier with dataset path."""
        self.dataset_path = Path(dataset_path)
        self.problem_classifications = {}
        # Define consistent algorithm type ordering
        self.algorithm_type_order = [
            "list_search",
            "string_sorting", 
            "mathematical",
            "list_manipulation",
            "string_manipulation",
            "general_logic",
            "number_theory",
            "list_sorting",
            "mathematical_sequence",
            "validation",
            "data_structures",
            "graph_tree",
            "control_flow_heavy",
            "unknown",
        ]
    
    def classify_problem_complexity(self, problem_data: Dict[str, Any]) -> Dict[str, Any]:
        """Classify a HumanEval problem based on its code structure and complexity."""
        canonical_solution = problem_data.get("canonical_solution", "")
        prompt = problem_data.get("prompt", "")
        task_id = problem_data.get("task_id", "")

        # Parse the canonical solution to analyze code structure
        try:
            # Clean up indentation issues in canonical solution
            clean_solution = textwrap.dedent(canonical_solution).strip()
            tree = ast.parse(clean_solution)

            # Count different types of nodes
            node_counts = Counter()
            control_flow_depth = 0
            max_loop_depth = 0
            max_condition_depth = 0
            current_loop_depth = 0
            current_condition_depth = 0

            for node in ast.walk(tree):
                node_counts[type(node).__name__] += 1

                # Track nested loops
                if isinstance(node, (ast.For, ast.While)):
                    current_loop_depth += 1
                    max_loop_depth = max(max_loop_depth, current_loop_depth)
                elif isinstance(node, (ast.If, ast.IfExp)):
                    current_condition_depth += 1
                    max_condition_depth = max(
                        max_condition_depth, current_condition_depth
                    )

            # Calculate complexity metrics
            total_nodes = sum(node_counts.values())
            loop_count = node_counts.get("For", 0) + node_counts.get("While", 0)
            condition_count = node_counts.get("If", 0) + node_counts.get("IfExp", 0)
            function_calls = node_counts.get("Call", 0)
            list_comprehensions = node_counts.get("ListComp", 0) + node_counts.get(
                "DictComp", 0
            )

            # Determine algorithm type based on prompt and code patterns
            algorithm_type = self._determine_algorithm_type(
                prompt, canonical_solution, node_counts
            )

            # Determine complexity level
            complexity_score = (
                loop_count * 2
                + condition_count * 1.5
                + max_loop_depth * 3
                + max_condition_depth * 2
                + function_calls * 0.5
                + list_comprehensions * 1.5
                + (total_nodes / 10)
            )

            if complexity_score <= 5:
                complexity_level = "simple"
            elif complexity_score <= 15:
                complexity_level = "medium"
            else:
                complexity_level = "complex"

            return {
                "complexity_level": complexity_level,
                "complexity_score": complexity_score,
                "algorithm_type": algorithm_type,
                "loop_count": loop_count,
                "condition_count": condition_count,
                "max_loop_depth": max_loop_depth,
                "max_condition_depth": max_condition_depth,
                "total_nodes": total_nodes,
                "function_calls": function_calls,
                "list_comprehensions": list_comprehensions,
                "has_nested_loops": max_loop_depth > 1,
                "has_nested_conditions": max_condition_depth > 1,
                "problem_id": int(task_id.split("/")[1]) if "/" in task_id else 0,
            }

        except Exception as e:
            print(f"Error analyzing problem {task_id}: {e}")
            return {
                "complexity_level": "unknown",
                "complexity_score": 0,
                "algorithm_type": "unknown",
                "loop_count": 0,
                "condition_count": 0,
                "max_loop_depth": 0,
                "max_condition_depth": 0,
                "total_nodes": 0,
                "function_calls": 0,
                "list_comprehensions": 0,
                "has_nested_loops": False,
                "has_nested_conditions": False,
                "problem_id": 0,
            }

    def _determine_algorithm_type(
        self, prompt: str, code: str, node_counts: Dict
    ) -> str:
        """Determine the primary algorithm type based on prompt and code patterns."""
        prompt_lower = prompt.lower()
        code_lower = code.lower()

        # String processing
        if any(
            keyword in prompt_lower
            for keyword in ["string", "character", "word", "text", "replace"]
        ):
            if "sort" in prompt_lower:
                return "string_sorting"
            return "string_manipulation"

        # Mathematical operations
        if any(
            keyword in prompt_lower
            for keyword in [
                "number",
                "digit",
                "prime",
                "factorial",
                "sum",
                "product",
                "math",
            ]
        ):
            if "prime" in prompt_lower:
                return "number_theory"
            if any(
                keyword in prompt_lower
                for keyword in ["factorial", "fibonacci", "sequence"]
            ):
                return "mathematical_sequence"
            return "mathematical"

        # List/Array operations
        if any(keyword in prompt_lower for keyword in ["list", "array", "element"]):
            if "sort" in prompt_lower:
                return "list_sorting"
            if any(keyword in prompt_lower for keyword in ["search", "find", "index"]):
                return "list_search"
            return "list_manipulation"

        # Graph/Tree operations
        if any(
            keyword in prompt_lower for keyword in ["tree", "graph", "node", "path"]
        ):
            return "graph_tree"

        # Control flow heavy
        if node_counts.get("For", 0) + node_counts.get("While", 0) > 2:
            return "control_flow_heavy"

        # Pattern matching/validation
        if any(
            keyword in prompt_lower
            for keyword in ["valid", "check", "verify", "pattern"]
        ):
            return "validation"

        # Data structure operations
        if any(
            keyword in prompt_lower for keyword in ["dictionary", "dict", "map", "set"]
        ):
            return "data_structures"

        return "general_logic"

    def load_problem_classifications(self) -> None:
        """Load and classify all problems from the HumanEval dataset."""
        print(f"Loading problem classifications from {self.dataset_path}...")

        if not self.dataset_path.exists():
            print(
                f"Warning: Dataset file {self.dataset_path} not found. Skipping problem classification."
            )
            return

        try:
            with open(self.dataset_path, "r") as f:
                for line in f:
                    if line.strip():
                        problem_data = json.loads(line)
                        task_id = problem_data.get("task_id", "")
                        if "/" in task_id:
                            problem_id = int(task_id.split("/")[1])
                            classification = self.classify_problem_complexity(
                                problem_data
                            )
                            self.problem_classifications[problem_id] = classification

            print(
                f"Successfully classified {len(self.problem_classifications)} problems"
            )

        except Exception as e:
            print(f"Error loading problem classifications: {e}")
    
    def get_classification(self, problem_id: int) -> Dict[str, Any]:
        """Get classification data for a specific problem ID."""
        return self.problem_classifications.get(problem_id, {
            "complexity_level": "unknown",
            "algorithm_type": "unknown"
        })
    
    def get_all_classifications(self) -> Dict[int, Dict[str, Any]]:
        """Get all problem classifications."""
        return self.problem_classifications