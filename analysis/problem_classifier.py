#!/usr/bin/env python3
"""
Problem Classification Module (Flake8-Cognitive-Complexity Version)

Handles automatic classification of HumanEval problems based on complexity
and algorithm types using flake8-cognitive-complexity as the sole complexity
measurement method, with AST analysis only for algorithm type classification.

Key Features:
- Complexity measurement exclusively using flake8-cognitive-complexity
- AST-based analysis only for algorithm type classification
- Adaptive threshold calculation based on data distribution
- Robust error handling with multiple fallback methods
- Subprocess-based integration with flake8-cognitive-complexity
- Supplementary metrics (loops, conditions, recursion) for analysis purposes only
"""

import json
import ast
import textwrap
import numpy as np
import subprocess
import tempfile
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import Counter


class ProblemClassifier:
    """Handles classification of HumanEval problems by complexity and algorithm type.

    Uses flake8-cognitive-complexity exclusively for complexity measurements.
    AST analysis is used only for algorithm type classification.
    """

    def __init__(
        self,
        dataset_path: str = "dataset/HumanEval.jsonl",
        use_adaptive_thresholds: bool = True,
    ):
        """Initialize the classifier with dataset path."""
        self.dataset_path = Path(dataset_path)
        self.problem_classifications = {}
        self.use_adaptive_thresholds = use_adaptive_thresholds
        self.complexity_thresholds = None  # Will be set after loading all data

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

    def _compute_nesting_depth(
        self, node: ast.AST, target_types: tuple, current_depth: int = 0
    ) -> int:
        """
        Recursively compute maximum nesting depth for specific node types.

        This method properly handles nested structures by recursing through the AST,
        avoiding the pitfalls of breadth-first traversal.

        Args:
            node: Current AST node
            target_types: Tuple of AST node types to track (e.g., (ast.For, ast.While))
            current_depth: Current depth level

        Returns:
            Maximum nesting depth found in the subtree
        """
        max_depth = current_depth

        for child in ast.iter_child_nodes(node):
            if isinstance(child, target_types):
                # This is a target node, increase depth
                child_depth = self._compute_nesting_depth(
                    child, target_types, current_depth + 1
                )
                max_depth = max(max_depth, child_depth)
            else:
                # Not a target node, maintain current depth
                child_depth = self._compute_nesting_depth(
                    child, target_types, current_depth
                )
                max_depth = max(max_depth, child_depth)

        return max_depth

    def _detect_recursion(self, tree: ast.AST) -> bool:
        """
        Detect if the function contains recursive calls.

        This helps identify short but complex functions that use recursion,
        which may be more challenging for LLMs to generate tests for.

        Args:
            tree: AST tree of the function

        Returns:
            True if recursion is detected, False otherwise
        """
        func_name = None

        # Find the function name
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                break

        if not func_name:
            return False

        # Check for recursive calls
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == func_name:
                    return True

        return False

    def _calculate_cognitive_complexity_flake8(self, code: str) -> Dict[str, Any]:
        """
        Calculate cognitive complexity using flake8-cognitive-complexity.

        This method uses subprocess to call flake8 with the cognitive complexity plugin
        and parses the results to extract complexity scores.

        Args:
            code: Python code string to analyze

        Returns:
            Dictionary containing cognitive complexity information
        """
        try:
            # Create a temporary file to write the code
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".py", delete=False
            ) as temp_file:
                temp_file.write(code)
                temp_file_path = temp_file.name

            try:
                # Run flake8 with cognitive complexity plugin
                # Set a high threshold to avoid errors, we just want the complexity values
                result = subprocess.run(
                    [
                        "flake8",
                        "--max-cognitive-complexity=100",  # High threshold to avoid errors
                        temp_file_path,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,  # Prevent hanging
                )

                # Parse the output for cognitive complexity warnings
                cognitive_complexity_scores = []
                lines = result.stdout.split("\n")

                for line in lines:
                    if "CCR001" in line and "Cognitive complexity is too high" in line:
                        # Extract complexity score from line like:
                        # file.py:10:5: CCR001 Cognitive complexity is too high (15 > 100)
                        try:
                            # Find the score in parentheses
                            start = line.find("(") + 1
                            end = line.find(" >")
                            if start > 0 and end > start:
                                score = int(line[start:end])
                                cognitive_complexity_scores.append(score)
                        except (ValueError, IndexError):
                            continue

                # If no cognitive complexity warnings, try to get basic complexity
                if not cognitive_complexity_scores:
                    # Fallback: use a simple heuristic based on code structure
                    cognitive_complexity_scores = [
                        self._estimate_cognitive_complexity_fallback(code)
                    ]

                # Return the maximum complexity found (in case of multiple functions)
                max_complexity = (
                    max(cognitive_complexity_scores)
                    if cognitive_complexity_scores
                    else 0
                )

                return {
                    "cognitive_complexity": max_complexity,
                    "cognitive_complexity_scores": cognitive_complexity_scores,
                    "method": "flake8-cognitive-complexity",
                }

            finally:
                # Clean up temporary file
                os.unlink(temp_file_path)

        except subprocess.TimeoutExpired:
            return {
                "cognitive_complexity": 0,
                "cognitive_complexity_scores": [0],
                "method": "flake8-cognitive-complexity-timeout",
            }
        except Exception as e:
            print(f"Error calculating cognitive complexity with flake8: {e}")
            return {
                "cognitive_complexity": 0,
                "cognitive_complexity_scores": [0],
                "method": "flake8-cognitive-complexity-error",
            }

    def _estimate_cognitive_complexity_fallback(self, code: str) -> int:
        """
        Fallback method to estimate cognitive complexity when flake8 fails.

        This provides a simple heuristic based on control flow structures.

        Args:
            code: Python code string

        Returns:
            Estimated cognitive complexity score
        """
        complexity = 0

        # Basic control flow complexity
        complexity += code.count("if ") + code.count("elif ")
        complexity += code.count("for ") + code.count("while ")
        complexity += code.count("except ") + code.count("try:")
        complexity += code.count("and ") + code.count("or ")

        # Nested structures add more complexity
        lines = code.split("\n")
        for line in lines:
            stripped = line.strip()
            if stripped.startswith(("if ", "for ", "while ", "def ", "class ")):
                # Count indentation level (rough approximation of nesting)
                indent_level = len(line) - len(line.lstrip())
                if indent_level > 4:  # More than one level of nesting
                    complexity += 1

        return complexity

    def _determine_complexity_level(
        self, complexity_score: float, thresholds: Optional[Tuple[float, float]] = None
    ) -> str:
        """
        Determine complexity level based on score and thresholds.

        Args:
            complexity_score: Calculated complexity score
            thresholds: Optional tuple of (low_threshold, high_threshold)
                       If None, uses adaptive thresholds or fixed defaults

        Returns:
            Complexity level: "simple", "medium", or "complex"
        """
        if thresholds is None:
            if self.complexity_thresholds is not None:
                thresholds = self.complexity_thresholds
            else:
                # Default fixed thresholds
                thresholds = (5.0, 15.0)

        low_threshold, high_threshold = thresholds

        if complexity_score <= low_threshold:
            return "simple"
        elif complexity_score <= high_threshold:
            return "medium"
        else:
            return "complex"

    def classify_problem_complexity(
        self, problem_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Classify a HumanEval problem based on its code structure and complexity.

        Uses flake8-cognitive-complexity exclusively for complexity measurement.
        AST-based analysis is used only for algorithm type classification and
        supplementary metrics for analysis purposes.

        Args:
            problem_data: Dictionary containing problem information including
                         canonical_solution, prompt, and task_id

        Returns:
            Dictionary with complexity metrics and classification:
                - complexity_level: "simple", "medium", or "complex"
                - complexity_score: Cognitive complexity score from flake8
                - cognitive_complexity: Same as complexity_score
                - algorithm_type: Detected algorithm type
                - Supplementary metrics: loop_count, condition_count, etc.
        """
        canonical_solution = problem_data.get("canonical_solution", "")
        prompt = problem_data.get("prompt", "")
        task_id = problem_data.get("task_id", "")

        # Clean up indentation issues in canonical solution
        clean_solution = textwrap.dedent(canonical_solution).strip()

        # Calculate cognitive complexity using flake8-cognitive-complexity
        cognitive_complexity_info = self._calculate_cognitive_complexity_flake8(
            clean_solution
        )
        cognitive_complexity = cognitive_complexity_info["cognitive_complexity"]

        # Parse the canonical solution for supplementary AST-based analysis
        try:
            tree = ast.parse(clean_solution)

            # Count different types of nodes for algorithm classification
            node_counts = Counter()
            for node in ast.walk(tree):
                node_counts[type(node).__name__] += 1

            # Compute nesting depths for supplementary metrics
            max_loop_depth = self._compute_nesting_depth(tree, (ast.For, ast.While))
            max_condition_depth = self._compute_nesting_depth(tree, (ast.If, ast.IfExp))

            # Detect recursion
            has_recursion = self._detect_recursion(tree)

            # Calculate supplementary AST-based metrics
            total_nodes = sum(node_counts.values())
            loop_count = node_counts.get("For", 0) + node_counts.get("While", 0)
            condition_count = node_counts.get("If", 0) + node_counts.get("IfExp", 0)
            function_calls = node_counts.get("Call", 0)
            list_comprehensions = node_counts.get("ListComp", 0) + node_counts.get(
                "DictComp", 0
            )

            # Determine algorithm type using AST analysis
            algorithm_type = self._determine_algorithm_type(
                prompt, canonical_solution, node_counts
            )

            # Use cognitive complexity as the sole complexity score (no adjustments)
            complexity_score = cognitive_complexity

            # Determine complexity level based on cognitive complexity
            complexity_level = self._determine_complexity_level(complexity_score)

            return {
                "complexity_level": complexity_level,
                "complexity_score": complexity_score,
                "cognitive_complexity": cognitive_complexity,
                "cognitive_complexity_method": cognitive_complexity_info["method"],
                "algorithm_type": algorithm_type,
                # Supplementary AST-based metrics for analysis only
                "loop_count": loop_count,
                "condition_count": condition_count,
                "max_loop_depth": max_loop_depth,
                "max_condition_depth": max_condition_depth,
                "total_nodes": total_nodes,
                "function_calls": function_calls,
                "list_comprehensions": list_comprehensions,
                "has_recursion": has_recursion,
                "has_nested_loops": max_loop_depth > 1,
                "has_nested_conditions": max_condition_depth > 1,
                "problem_id": int(task_id.split("/")[1]) if "/" in task_id else 0,
            }

        except SyntaxError as e:
            # Fallback for syntax errors - use only cognitive complexity
            print(f"Syntax error analyzing problem {task_id}: {e}")
            loc = len(canonical_solution.strip().split("\n"))

            # Use cognitive complexity if available, otherwise fallback to LOC
            fallback_score = (
                cognitive_complexity if cognitive_complexity > 0 else loc / 2.0
            )

            return {
                "complexity_level": self._determine_complexity_level(fallback_score),
                "complexity_score": fallback_score,
                "cognitive_complexity": cognitive_complexity,
                "cognitive_complexity_method": cognitive_complexity_info["method"],
                "algorithm_type": "unknown",
                "loop_count": 0,
                "condition_count": 0,
                "max_loop_depth": 0,
                "max_condition_depth": 0,
                "total_nodes": 0,
                "function_calls": 0,
                "list_comprehensions": 0,
                "has_recursion": False,
                "has_nested_loops": False,
                "has_nested_conditions": False,
                "problem_id": int(task_id.split("/")[1]) if "/" in task_id else 0,
                "error": "syntax_error",
            }
        except Exception as e:
            print(f"Error analyzing problem {task_id}: {e}")
            return {
                "complexity_level": "unknown",
                "complexity_score": 0,
                "cognitive_complexity": 0,
                "cognitive_complexity_method": "error",
                "algorithm_type": "unknown",
                "loop_count": 0,
                "condition_count": 0,
                "max_loop_depth": 0,
                "max_condition_depth": 0,
                "total_nodes": 0,
                "function_calls": 0,
                "list_comprehensions": 0,
                "has_recursion": False,
                "has_nested_loops": False,
                "has_nested_conditions": False,
                "problem_id": 0,
                "error": str(e),
            }

    def _determine_algorithm_type(
        self, prompt: str, code: str, node_counts: Dict
    ) -> str:
        """
        Determine the primary algorithm type based on prompt and code patterns.

        Note: This is treated as auxiliary metadata and is independent of the
        complexity scoring to avoid confounding variables in analysis.
        """
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
        """
        Load and classify all problems from the HumanEval dataset.

        IMPROVEMENT ⑤: If use_adaptive_thresholds=True, calculates percentile-based
        thresholds after classifying all problems, ensuring data-driven categorization
        rather than arbitrary fixed values.
        """
        print(f"Loading problem classifications from {self.dataset_path}...")

        if not self.dataset_path.exists():
            print(
                f"Warning: Dataset file {self.dataset_path} not found. Skipping problem classification."
            )
            return

        try:
            # First pass: classify all problems with default thresholds
            temp_scores = []

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
                            temp_scores.append(classification["complexity_score"])

            # IMPROVEMENT ⑤: Calculate adaptive thresholds based on data distribution
            if self.use_adaptive_thresholds and temp_scores:
                p33, p66 = np.percentile(temp_scores, [33, 66])
                self.complexity_thresholds = (p33, p66)
                print(
                    f"Using adaptive thresholds: {p33:.2f} (33rd) and {p66:.2f} (66th percentile)"
                )

                # Second pass: reclassify with adaptive thresholds
                for problem_id, classification in self.problem_classifications.items():
                    score = classification["complexity_score"]
                    classification["complexity_level"] = (
                        self._determine_complexity_level(
                            score, self.complexity_thresholds
                        )
                    )

            print(
                f"Successfully classified {len(self.problem_classifications)} problems"
            )

        except Exception as e:
            print(f"Error loading problem classifications: {e}")

    def get_classification(self, problem_id: int) -> Dict[str, Any]:
        """Get classification data for a specific problem ID."""
        return self.problem_classifications.get(
            problem_id, {"complexity_level": "unknown", "algorithm_type": "unknown"}
        )

    def get_all_classifications(self) -> Dict[int, Dict[str, Any]]:
        """Get all problem classifications."""
        return self.problem_classifications
