#!/usr/bin/env python3
"""
Data Loading Module

Handles loading and parsing of test statistics files and combining them
with problem classification data.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any
from .problem_classifier import ProblemClassifier


class DataLoader:
    """Handles loading and parsing of test result statistics files."""

    def __init__(
        self,
        results_dir: str = "generated_tests",
        dataset_path: str = "dataset/HumanEval.jsonl",
    ):
        """Initialize the data loader with results and dataset paths."""
        self.results_dir = Path(results_dir)
        self.dataset_path = dataset_path
        self.data = []
        self.classifier = ProblemClassifier(dataset_path)
        # Define the desired order for configuration types
        self.config_order = ["basic", "ast", "docstring", "docstring_ast"]

    def parse_filename(self, filename: str) -> Dict[str, Any]:
        """Parse configuration information from filename.
        Examples:
        - test_humaneval_0_success.stats.json -> {problem_id: 0, docstring: False, ast: False, success: True}
        - test_humaneval_5_docstring_ast_false.stats.json -> {problem_id: 5, docstring: True, ast: True, success: False}
        """
        # Remove .stats.json extension
        base_name = filename.replace(".stats.json", "")

        # Extract problem ID
        match = re.search(r"test_humaneval_(\d+)", base_name)
        if not match:
            return None

        problem_id = int(match.group(1))

        # Check for configuration flags
        has_docstring = "_docstring" in base_name
        has_ast = "_ast" in base_name

        # Check success status
        is_success = base_name.endswith("_success")
        is_false = base_name.endswith("_false")

        # Determine configuration type
        if has_docstring and has_ast:
            config_type = "docstring_ast"
        elif has_docstring:
            config_type = "docstring"
        elif has_ast:
            config_type = "ast"
        else:
            config_type = "basic"

        return {
            "problem_id": problem_id,
            "has_docstring": has_docstring,
            "has_ast": has_ast,
            "config_type": config_type,
            "success": is_success,
            "filename": filename,
        }

    def load_data(self) -> List[Dict[str, Any]]:
        """Load all stats.json files and parse them."""
        # First load problem classifications
        self.classifier.load_problem_classifications()

        print(f"Loading data from {self.results_dir}...")
        stats_files = list(self.results_dir.glob("*.stats.json"))
        print(f"Found {len(stats_files)} stats files")

        for stats_file in stats_files:
            # Parse filename for configuration info
            file_config = self.parse_filename(stats_file.name)
            if not file_config:
                print(f"Warning: Could not parse filename {stats_file.name}")
                continue

            # Load stats data
            try:
                with open(stats_file, "r") as f:
                    stats_data = json.load(f)

                # Combine filename info with stats data
                combined_data = {**file_config, **stats_data}

                # Handle missing code_coverage_percent field
                if "code_coverage_percent" not in combined_data:
                    combined_data["code_coverage_percent"] = 0.0

                # Add problem classification data
                problem_id = combined_data.get("problem_id")
                classification = self.classifier.get_classification(problem_id)
                if classification:
                    combined_data.update(classification)
                else:
                    # Add default classification if problem not found
                    combined_data.update(
                        {
                            "complexity_level": "unknown",
                            "algorithm_type": "unknown",
                            "complexity_score": 0,
                        }
                    )

                self.data.append(combined_data)

            except Exception as e:
                print(f"Error loading {stats_file}: {e}")

        print(f"Successfully loaded {len(self.data)} records")
        return self.data

    def get_data(self) -> List[Dict[str, Any]]:
        """Get loaded data."""
        return self.data

    def get_classifier(self) -> ProblemClassifier:
        """Get the problem classifier instance."""
        return self.classifier
