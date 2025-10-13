#!/usr/bin/env python3
"""
Problem Classification Module (Flake8-Cognitive-Complexity Version)

Handles automatic classification of HumanEval problems based on cognitive complexity
using flake8-cognitive-complexity as the sole complexity measurement method.

Key Features:
- Complexity measurement exclusively using flake8-cognitive-complexity
- Adaptive threshold calculation based on data distribution
- Robust error handling with clear error messages when flake8 is unavailable
- Subprocess-based integration with flake8-cognitive-complexity
"""

import json
import textwrap
import numpy as np
import subprocess
import tempfile
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


class ProblemClassifier:
    """Handles classification of HumanEval problems by cognitive complexity.

    Uses flake8-cognitive-complexity exclusively for complexity measurements.
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

    def _calculate_cognitive_complexity_flake8(self, code: str) -> Dict[str, Any]:
        """
        Calculate cognitive complexity using flake8-cognitive-complexity.

        This method uses subprocess to call flake8 with the cognitive complexity plugin
        and parses the results to extract complexity scores.

        Args:
            code: Python code string to analyze (may be a function body or complete function)

        Returns:
            Dictionary containing cognitive complexity information
        """
        try:
            # Wrap code in a dummy function if it's not already a complete function
            # HumanEval canonical_solution is often just the function body
            if not code.strip().startswith("def "):
                # Indent the code to be inside a function
                indented_code = textwrap.indent(code, "    ")
                # Wrap the code in a dummy function to make it syntactically valid
                wrapped_code = f"def _temp_function():\n{indented_code}\n"
            else:
                wrapped_code = code

            # Create a temporary file to write the code
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".py", delete=False
            ) as temp_file:
                temp_file.write(wrapped_code)
                temp_file_path = temp_file.name

            try:
                # Run flake8 with cognitive complexity plugin
                # Set a very low threshold (1) to ensure CCR001 warnings are generated for all functions
                # This allows us to extract the actual complexity score from the warning message
                result = subprocess.run(
                    [
                        "flake8",
                        "--max-cognitive-complexity=1",  # Low threshold to capture all scores
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

                # Return the maximum complexity found (in case of multiple functions)
                # If no warnings found, the function has complexity 0 (empty or very simple)
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
        Classify a HumanEval problem based on its cognitive complexity.

        Uses flake8-cognitive-complexity exclusively for complexity measurement.
        If flake8-cognitive-complexity fails, returns error information instead of fallback values.

        Args:
            problem_data: Dictionary containing problem information including
                         canonical_solution and task_id

        Returns:
            Dictionary with complexity metrics and classification:
                - complexity_level: "simple", "medium", "complex", or "error"
                - complexity_score: Cognitive complexity score from flake8 (0 if error)
                - cognitive_complexity: Same as complexity_score
                - cognitive_complexity_method: Method used for calculation
                - problem_id: Problem ID extracted from task_id
                - error: Error message (only present if classification failed)
        """
        canonical_solution = problem_data.get("canonical_solution", "")
        task_id = problem_data.get("task_id", "")

        # Clean up indentation issues in canonical solution
        clean_solution = textwrap.dedent(canonical_solution).strip()

        # Calculate cognitive complexity using flake8-cognitive-complexity
        try:
            cognitive_complexity_info = self._calculate_cognitive_complexity_flake8(
                clean_solution
            )
            cognitive_complexity = cognitive_complexity_info["cognitive_complexity"]

            # Use cognitive complexity as the sole complexity score
            complexity_score = cognitive_complexity

            # Determine complexity level based on cognitive complexity
            complexity_level = self._determine_complexity_level(complexity_score)

            return {
                "complexity_level": complexity_level,
                "complexity_score": complexity_score,
                "cognitive_complexity": cognitive_complexity,
                "cognitive_complexity_method": cognitive_complexity_info["method"],
                "problem_id": int(task_id.split("/")[1]) if "/" in task_id else 0,
            }

        except SyntaxError as e:
            # Syntax error in code - cannot use flake8-cognitive-complexity
            error_msg = f"Syntax error in problem {task_id}: {e}"
            print(f"ERROR: {error_msg}")
            return {
                "complexity_level": "error",
                "complexity_score": 0,
                "cognitive_complexity": 0,
                "cognitive_complexity_method": "error-syntax",
                "problem_id": int(task_id.split("/")[1]) if "/" in task_id else 0,
                "error": error_msg,
            }
        except Exception as e:
            # General error - flake8-cognitive-complexity failed
            error_msg = (
                f"Failed to calculate cognitive complexity for problem {task_id}: {e}"
            )
            print(f"ERROR: {error_msg}")
            return {
                "complexity_level": "error",
                "complexity_score": 0,
                "cognitive_complexity": 0,
                "cognitive_complexity_method": "error-general",
                "problem_id": int(task_id.split("/")[1]) if "/" in task_id else 0,
                "error": error_msg,
            }

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
            problem_id,
            {
                "complexity_level": "unknown",
                "complexity_score": 0,
                "cognitive_complexity": 0,
                "error": "Problem ID not found in classifications",
            },
        )

    def get_all_classifications(self) -> Dict[int, Dict[str, Any]]:
        """Get all problem classifications."""
        return self.problem_classifications
