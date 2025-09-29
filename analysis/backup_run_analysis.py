#!/usr/bin/env python3
"""
Test Results Visualization Tool

Analyzes generated test results from stats.json files and creates visualizations
comparing different configurations (basic, docstring, AST, both).
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ast
from collections import Counter


class TestResultsAnalyzer:
    def __init__(
        self,
        results_dir: str = "generated_tests",
        dataset_path: str = "dataset/HumanEval.jsonl",
    ):
        """Initialize the analyzer with the results directory."""
        self.results_dir = Path(results_dir)
        self.dataset_path = Path(dataset_path)
        self.data = []
        # Define the desired order for configuration types
        self.config_order = ["basic", "ast", "docstring", "docstring_ast"]
        # Problem classification data
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

    def classify_problem_complexity(
        self, problem_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Classify a HumanEval problem based on its code structure and complexity."""
        canonical_solution = problem_data.get("canonical_solution", "")
        prompt = problem_data.get("prompt", "")
        task_id = problem_data.get("task_id", "")

        # Parse the canonical solution to analyze code structure
        try:
            # Clean up indentation issues in canonical solution
            import textwrap

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

    def load_data(self) -> None:
        """Load all stats.json files and parse them."""
        # First load problem classifications
        self.load_problem_classifications()

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
                if problem_id in self.problem_classifications:
                    classification = self.problem_classifications[problem_id]
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

        # Convert to DataFrame for easier analysis
        self.df = pd.DataFrame(self.data)

        # Set categorical ordering for config_type and rename labels
        if not self.df.empty:
            # Rename docstring_ast to ast+docstring for better readability
            self.df["config_type_display"] = self.df["config_type"].replace(
                "docstring_ast", "ast+docstring"
            )

            # Create display order matching the internal order
            display_order = ["basic", "ast", "docstring", "ast+docstring"]
            self.df["config_type_display"] = pd.Categorical(
                self.df["config_type_display"], categories=display_order, ordered=True
            )

    def create_visualizations(self, output_dir: str = "visualizations") -> None:
        """Create all visualization graphs."""
        if not self.data:
            print("No data loaded. Call load_data() first.")
            return

        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Set style
        plt.style.use("default")
        sns.set_palette("husl")

        print(f"Creating visualizations in {output_path}...")

        # 1. Success Rate by Configuration
        self._plot_success_rate(output_path)

        # 2. Code Coverage by Configuration
        self._plot_code_coverage(output_path)

        # 3. Cost Analysis by Configuration
        self._plot_cost_analysis(output_path)

        # 4. Fix Attempts by Configuration
        self._plot_fix_attempts(output_path)

        # 5. Success Rate by Problem ID
        self._plot_success_by_problem(output_path)

        # 6. Cost vs Quality Scatter Plot
        self._plot_cost_vs_quality(output_path)

        # 7. Input Token Usage by Configuration
        self._plot_input_tokens(output_path)

        # 8. Success Rate by Problem Complexity
        self._plot_success_by_complexity(output_path)

        # 9. Success Rate by Algorithm Type
        self._plot_success_by_algorithm_type(output_path)

        # 10. Configuration Performance by Complexity
        self._plot_config_performance_by_complexity(output_path)

        # 11. Cost vs Complexity Analysis
        # self._plot_cost_vs_complexity(output_path)

        # 12. Algorithm Type Distribution
        self._plot_algorithm_type_distribution(output_path)

        print("All visualizations created successfully!")

    def _plot_success_rate(self, output_path: Path) -> None:
        """Plot success rate by configuration type."""
        fig, ax = plt.subplots(figsize=(10, 6))

        success_rate = (
            self.df.groupby("config_type_display", observed=False)["success"]
            .agg(["mean", "count"])
            .reset_index()
        )
        success_rate["success_rate"] = success_rate["mean"] * 100
        success_rate = success_rate.sort_values("config_type_display")

        bars = ax.bar(success_rate["config_type_display"], success_rate["success_rate"])
        ax.set_title(
            "Success Rate by Configuration Type", fontsize=14, fontweight="bold"
        )
        ax.set_xlabel("Configuration Type")
        ax.set_ylabel("Success Rate (%)")
        ax.set_ylim(0, 100)

        # Add value labels on bars
        for bar, rate, count in zip(
            bars, success_rate["success_rate"], success_rate["count"]
        ):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 1,
                f"{rate:.1f}%\n(n={count})",
                ha="center",
                va="bottom",
            )

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_path / "1_success_rate.png", dpi=300, bbox_inches="tight")
        plt.close()

    def _plot_code_coverage(self, output_path: Path) -> None:
        """Plot code coverage by configuration type."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Box plot
        sns.boxplot(
            data=self.df, x="config_type_display", y="code_coverage_percent", ax=ax1
        )
        ax1.set_title("Code Coverage Distribution by Configuration", fontweight="bold")
        ax1.set_xlabel("Configuration Type")
        ax1.set_ylabel("Code Coverage (%)")
        ax1.tick_params(axis="x", rotation=45)

        # Bar plot of mean coverage
        coverage_stats = (
            self.df.groupby("config_type_display", observed=False)[
                "code_coverage_percent"
            ]
            .agg(["mean", "std", "count"])
            .reset_index()
        )
        coverage_stats = coverage_stats.sort_values("config_type_display")
        bars = ax2.bar(
            coverage_stats["config_type_display"],
            coverage_stats["mean"],
            yerr=coverage_stats["std"],
            capsize=5,
        )
        ax2.set_title("Average Code Coverage by Configuration", fontweight="bold")
        ax2.set_xlabel("Configuration Type")
        ax2.set_ylabel("Average Code Coverage (%)")
        ax2.tick_params(axis="x", rotation=45)

        # Add value labels
        for bar, mean, count in zip(
            bars, coverage_stats["mean"], coverage_stats["count"]
        ):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 1,
                f"{mean:.1f}%\n(n={count})",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        plt.savefig(output_path / "2_code_coverage.png", dpi=300, bbox_inches="tight")
        plt.close()

    def _plot_cost_analysis(self, output_path: Path) -> None:
        """Plot cost analysis by configuration type."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Total cost box plot
        sns.boxplot(data=self.df, x="config_type_display", y="total_cost_usd", ax=ax1)
        ax1.set_title("Total Cost Distribution by Configuration", fontweight="bold")
        ax1.set_xlabel("Configuration Type")
        ax1.set_ylabel("Total Cost (USD)")
        ax1.tick_params(axis="x", rotation=45)

        # Average cost bar plot
        cost_stats = (
            self.df.groupby("config_type_display", observed=False)["total_cost_usd"]
            .agg(["mean", "std", "count"])
            .reset_index()
        )
        cost_stats = cost_stats.sort_values("config_type_display")
        bars = ax2.bar(
            cost_stats["config_type_display"],
            cost_stats["mean"],
            yerr=cost_stats["std"],
            capsize=5,
        )
        ax2.set_title("Average Total Cost by Configuration", fontweight="bold")
        ax2.set_xlabel("Configuration Type")
        ax2.set_ylabel("Average Total Cost (USD)")
        ax2.tick_params(axis="x", rotation=45)

        # Add value labels
        for bar, mean, count in zip(bars, cost_stats["mean"], cost_stats["count"]):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.001,
                f"${mean:.4f}\n(n={count})",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        plt.savefig(output_path / "3_cost_analysis.png", dpi=300, bbox_inches="tight")
        plt.close()

    def _plot_fix_attempts(self, output_path: Path) -> None:
        """Plot fix attempts needed by configuration type."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Box plot
        sns.boxplot(
            data=self.df, x="config_type_display", y="fix_attempts_used", ax=ax1
        )
        ax1.set_title("Fix Attempts Distribution by Configuration", fontweight="bold")
        ax1.set_xlabel("Configuration Type")
        ax1.set_ylabel("Fix Attempts Used")
        ax1.tick_params(axis="x", rotation=45)

        # Average fix attempts
        fix_stats = (
            self.df.groupby("config_type_display", observed=False)["fix_attempts_used"]
            .agg(["mean", "std", "count"])
            .reset_index()
        )
        fix_stats = fix_stats.sort_values("config_type_display")
        bars = ax2.bar(
            fix_stats["config_type_display"],
            fix_stats["mean"],
            yerr=fix_stats["std"],
            capsize=5,
        )
        ax2.set_title("Average Fix Attempts by Configuration", fontweight="bold")
        ax2.set_xlabel("Configuration Type")
        ax2.set_ylabel("Average Fix Attempts")
        ax2.tick_params(axis="x", rotation=45)

        # Add value labels
        for bar, mean, count in zip(bars, fix_stats["mean"], fix_stats["count"]):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.05,
                f"{mean:.2f}\n(n={count})",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        plt.savefig(output_path / "4_fix_attempts.png", dpi=300, bbox_inches="tight")
        plt.close()

    def _plot_success_by_problem(self, output_path: Path) -> None:
        """Plot success rate by problem ID across configurations."""
        fig, ax = plt.subplots(figsize=(15, 8))

        # Create pivot table for heatmap
        pivot_data = self.df.pivot_table(
            values="success",
            index="problem_id",
            columns="config_type_display",
            aggfunc="mean",
            fill_value=0,
            observed=False,
        )

        # Create heatmap
        sns.heatmap(
            pivot_data,
            annot=True,
            fmt=".2f",
            cmap="RdYlGn",
            ax=ax,
            cbar_kws={"label": "Success Rate"},
        )
        ax.set_title("Success Rate by Problem ID and Configuration", fontweight="bold")
        ax.set_xlabel("Configuration Type")
        ax.set_ylabel("Problem ID")

        plt.tight_layout()
        plt.savefig(
            output_path / "5_success_by_problem.png", dpi=300, bbox_inches="tight"
        )
        plt.close()

    def _plot_cost_vs_quality(self, output_path: Path) -> None:
        """Plot cost vs quality (coverage) scatter plot."""
        fig, ax = plt.subplots(figsize=(12, 8))

        # Create scatter plot with different colors for each config type
        for config_type in self.df["config_type_display"].unique():
            data = self.df[self.df["config_type_display"] == config_type]
            ax.scatter(
                data["total_cost_usd"],
                data["code_coverage_percent"],
                label=config_type,
                alpha=0.7,
                s=60,
            )

        ax.set_title("Cost vs Code Coverage by Configuration", fontweight="bold")
        ax.set_xlabel("Total Cost (USD)")
        ax.set_ylabel("Code Coverage (%)")
        ax.legend()
        ax.grid(True, alpha=0.3)

        # Add trend line
        if len(self.df) > 1:
            z = np.polyfit(
                self.df["total_cost_usd"], self.df["code_coverage_percent"], 1
            )
            p = np.poly1d(z)
            ax.plot(
                self.df["total_cost_usd"],
                p(self.df["total_cost_usd"]),
                "r--",
                alpha=0.8,
                linewidth=1,
            )

        plt.tight_layout()
        plt.savefig(output_path / "6_cost_vs_quality.png", dpi=300, bbox_inches="tight")
        plt.close()

    def _plot_input_tokens(self, output_path: Path) -> None:
        """Plot input token usage by configuration type."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Box plot for distribution
        sns.boxplot(
            data=self.df, x="config_type_display", y="total_input_tokens", ax=ax1
        )
        ax1.set_title("Input Token Distribution by Configuration", fontweight="bold")
        ax1.set_xlabel("Configuration Type")
        ax1.set_ylabel("Input Tokens")
        ax1.tick_params(axis="x", rotation=45)

        # Bar plot for average
        token_stats = (
            self.df.groupby("config_type_display", observed=False)["total_input_tokens"]
            .agg(["mean", "std", "count"])
            .reset_index()
        )
        token_stats = token_stats.sort_values("config_type_display")
        bars = ax2.bar(
            token_stats["config_type_display"],
            token_stats["mean"],
            yerr=token_stats["std"],
            capsize=5,
        )
        ax2.set_title("Average Input Tokens by Configuration", fontweight="bold")
        ax2.set_xlabel("Configuration Type")
        ax2.set_ylabel("Average Input Tokens")
        ax2.tick_params(axis="x", rotation=45)

        # Add value labels
        for bar, mean, count in zip(bars, token_stats["mean"], token_stats["count"]):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 50,
                f"{mean:.0f}\n(n={count})",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        plt.savefig(output_path / "7_input_tokens.png", dpi=300, bbox_inches="tight")
        plt.close()

    def _plot_success_by_complexity(self, output_path: Path) -> None:
        """Plot success rate by problem complexity level."""
        if "complexity_level" not in self.df.columns:
            print(
                "Warning: complexity_level not found in data. Skipping complexity analysis."
            )
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Success rate by complexity level
        complexity_order = ["simple", "medium", "complex"]
        complexity_data = self.df[self.df["complexity_level"].isin(complexity_order)]

        # Ensure proper ordering
        complexity_data["complexity_level"] = pd.Categorical(
            complexity_data["complexity_level"],
            categories=complexity_order,
            ordered=True,
        )

        success_by_complexity = (
            complexity_data.groupby(
                ["complexity_level", "config_type_display"], observed=False
            )["success"]
            .agg(["mean", "count"])
            .reset_index()
        )
        success_by_complexity["success_rate"] = success_by_complexity["mean"] * 100

        # Pivot for grouped bar chart
        pivot_success = success_by_complexity.pivot(
            index="complexity_level",
            columns="config_type_display",
            values="success_rate",
        ).fillna(0)

        if not pivot_success.empty and len(pivot_success.columns) > 0:
            pivot_success.plot(kind="bar", ax=ax1, width=0.8)
        else:
            ax1.text(
                0.5,
                0.5,
                "No classified complexity data available",
                ha="center",
                va="center",
                transform=ax1.transAxes,
            )
        ax1.set_title(
            "Success Rate by Problem Complexity and Configuration", fontweight="bold"
        )
        ax1.set_xlabel("Problem Complexity Level")
        ax1.set_ylabel("Success Rate (%)")
        ax1.legend(title="Configuration", bbox_to_anchor=(1.05, 1), loc="upper left")
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)

        # Heatmap of success rate
        if not complexity_data.empty:
            pivot_heatmap = complexity_data.pivot_table(
                values="success",
                index="complexity_level",
                columns="config_type_display",
                aggfunc="mean",
                fill_value=0,
                observed=False,
            )

            if not pivot_heatmap.empty:
                sns.heatmap(
                    pivot_heatmap,
                    annot=True,
                    fmt=".2f",
                    cmap="RdYlGn",
                    ax=ax2,
                    cbar_kws={"label": "Success Rate"},
                )
            else:
                ax2.text(
                    0.5,
                    0.5,
                    "No classified complexity data available",
                    ha="center",
                    va="center",
                    transform=ax2.transAxes,
                )
        else:
            ax2.text(
                0.5,
                0.5,
                "No classified complexity data available",
                ha="center",
                va="center",
                transform=ax2.transAxes,
            )
        ax2.set_title("Success Rate Heatmap by Complexity", fontweight="bold")
        ax2.set_xlabel("Configuration Type")
        ax2.set_ylabel("Problem Complexity Level")

        plt.tight_layout()
        plt.savefig(
            output_path / "8_success_by_complexity.png", dpi=300, bbox_inches="tight"
        )
        plt.close()

    def _plot_success_by_algorithm_type(self, output_path: Path) -> None:
        """Plot success rate by algorithm type."""
        if "algorithm_type" not in self.df.columns:
            print(
                "Warning: algorithm_type not found in data. Skipping algorithm type analysis."
            )
            return

        fig, ax = plt.subplots(figsize=(16, 8))

        # Success rate by algorithm type
        success_by_algo = (
            self.df.groupby(["algorithm_type", "config_type_display"], observed=False)[
                "success"
            ]
            .agg(["mean", "count"])
            .reset_index()
        )
        success_by_algo["success_rate"] = success_by_algo["mean"] * 100

        # Only show algorithm types with sufficient data
        algo_counts_filtered = success_by_algo.groupby("algorithm_type")["count"].sum()
        sufficient_algos = algo_counts_filtered[algo_counts_filtered >= 2].index
        filtered_data = success_by_algo[
            success_by_algo["algorithm_type"].isin(sufficient_algos)
        ]

        if not filtered_data.empty:
            pivot_algo = filtered_data.pivot(
                index="algorithm_type",
                columns="config_type_display",
                values="success_rate",
            ).fillna(0)

            # Reorder rows according to our algorithm type order
            ordered_algos = [
                t for t in self.algorithm_type_order if t in pivot_algo.index
            ]
            pivot_algo_ordered = pivot_algo.reindex(ordered_algos)

            pivot_algo_ordered.plot(kind="bar", ax=ax, width=0.8)
            ax.set_title(
                "Success Rate by Algorithm Type and Configuration", fontweight="bold"
            )
            ax.set_xlabel("Algorithm Type")
            ax.set_ylabel("Success Rate (%)")
            ax.legend(title="Configuration", bbox_to_anchor=(1.05, 1), loc="upper left")
            ax.tick_params(axis="x", rotation=45)

        plt.tight_layout()
        plt.savefig(
            output_path / "9_success_by_algorithm_type.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    def _plot_config_performance_by_complexity(self, output_path: Path) -> None:
        """Plot configuration performance across different complexity levels."""
        if "complexity_level" not in self.df.columns:
            print(
                "Warning: complexity_level not found in data. Skipping complexity performance analysis."
            )
            return

        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.ravel()

        complexity_order = ["simple", "medium", "complex"]
        complexity_data = self.df[self.df["complexity_level"].isin(complexity_order)]

        # Ensure proper ordering
        complexity_data["complexity_level"] = pd.Categorical(
            complexity_data["complexity_level"],
            categories=complexity_order,
            ordered=True,
        )

        metrics = [
            ("success", "Success Rate (%)", lambda x: x * 100),
            ("code_coverage_percent", "Code Coverage (%)", lambda x: x),
            ("total_cost_usd", "Average Cost (USD)", lambda x: x),
            ("fix_attempts_used", "Fix Attempts Used", lambda x: x),
        ]

        for idx, (metric, ylabel, transform_func) in enumerate(metrics):
            if metric not in complexity_data.columns:
                continue

            stats = (
                complexity_data.groupby(
                    ["complexity_level", "config_type_display"], observed=False
                )[metric]
                .agg(["mean", "std"])
                .reset_index()
            )
            stats["transformed_mean"] = stats["mean"].apply(transform_func)
            stats["transformed_std"] = (
                stats["std"].apply(transform_func)
                if metric != "success"
                else stats["std"] * 100
            )

            pivot_data = stats.pivot(
                index="complexity_level",
                columns="config_type_display",
                values="transformed_mean",
            ).fillna(0)

            pivot_data.plot(kind="bar", ax=axes[idx], width=0.8)
            axes[idx].set_title(f"{ylabel} by Complexity Level", fontweight="bold")
            axes[idx].set_xlabel("Problem Complexity Level")
            axes[idx].set_ylabel(ylabel)
            axes[idx].legend(
                title="Configuration", bbox_to_anchor=(1.05, 1), loc="upper left"
            )
            axes[idx].set_xticklabels(axes[idx].get_xticklabels(), rotation=0)

        plt.tight_layout()
        plt.savefig(
            output_path / "10_config_performance_by_complexity.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    def _plot_cost_vs_complexity(self, output_path: Path) -> None:
        """Plot cost vs complexity relationship."""
        if "complexity_score" not in self.df.columns:
            print(
                "Warning: complexity_score not found in data. Skipping cost vs complexity analysis."
            )
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Scatter plot of cost vs complexity score
        for config_type in self.df["config_type_display"].unique():
            data = self.df[self.df["config_type_display"] == config_type]
            ax1.scatter(
                data["complexity_score"],
                data["total_cost_usd"],
                label=config_type,
                alpha=0.7,
                s=60,
            )

        ax1.set_title("Cost vs Problem Complexity Score", fontweight="bold")
        ax1.set_xlabel("Complexity Score")
        ax1.set_ylabel("Total Cost (USD)")
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Box plot of cost by complexity level
        if "complexity_level" in self.df.columns:
            complexity_order = ["simple", "medium", "complex"]
            complexity_data = self.df[
                self.df["complexity_level"].isin(complexity_order)
            ]

            # Ensure proper ordering
            complexity_data["complexity_level"] = pd.Categorical(
                complexity_data["complexity_level"],
                categories=complexity_order,
                ordered=True,
            )

            sns.boxplot(
                data=complexity_data,
                x="complexity_level",
                y="total_cost_usd",
                hue="config_type_display",
                ax=ax2,
            )
            ax2.set_title("Cost Distribution by Complexity Level", fontweight="bold")
            ax2.set_xlabel("Problem Complexity Level")
            ax2.set_ylabel("Total Cost (USD)")
            ax2.legend(
                title="Configuration", bbox_to_anchor=(1.05, 1), loc="upper left"
            )

        plt.tight_layout()
        plt.savefig(
            output_path / "11_cost_vs_complexity.png", dpi=300, bbox_inches="tight"
        )
        plt.close()

    def _plot_algorithm_type_distribution(self, output_path: Path) -> None:
        """Plot distribution and success rates of different algorithm types."""
        if "algorithm_type" not in self.df.columns:
            print(
                "Warning: algorithm_type not found in data. Skipping algorithm distribution analysis."
            )
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # Pie chart of algorithm type distribution
        algo_counts = self.df["algorithm_type"].value_counts()
        # Only show types with more than 1% of data
        threshold = len(self.df) * 0.01
        major_algos = algo_counts[algo_counts >= threshold]
        other_count = algo_counts[algo_counts < threshold].sum()

        if other_count > 0:
            major_algos["other"] = other_count

        ax1.pie(
            major_algos.values,
            labels=major_algos.index,
            autopct="%1.1f%%",
            startangle=90,
        )
        ax1.set_title("Distribution of Algorithm Types in Dataset", fontweight="bold")

        # Success rate by algorithm type (only for types with sufficient data)
        success_by_algo = (
            self.df.groupby("algorithm_type")["success"]
            .agg(["mean", "count"])
            .reset_index()
        )
        success_by_algo["success_rate"] = success_by_algo["mean"] * 100

        # Filter for algorithm types with at least 3 samples
        sufficient_data = success_by_algo[success_by_algo["count"] >= 3]

        # Order by our defined algorithm type order, then by success rate for consistent display
        sufficient_data["type_order"] = sufficient_data["algorithm_type"].apply(
            lambda x: (
                self.algorithm_type_order.index(x)
                if x in self.algorithm_type_order
                else 999
            )
        )
        sufficient_data = sufficient_data.sort_values(
            ["type_order", "success_rate"], ascending=[True, True]
        )

        if not sufficient_data.empty:
            bars = ax2.barh(
                sufficient_data["algorithm_type"], sufficient_data["success_rate"]
            )
            ax2.set_title(
                "Success Rate by Algorithm Type\n(Types with ≥3 samples)",
                fontweight="bold",
            )
            ax2.set_xlabel("Success Rate (%)")
            ax2.set_ylabel("Algorithm Type")

            # Add value labels
            for bar, rate, count in zip(
                bars, sufficient_data["success_rate"], sufficient_data["count"]
            ):
                ax2.text(
                    bar.get_width() + 1,
                    bar.get_y() + bar.get_height() / 2,
                    f"{rate:.1f}% (n={count})",
                    ha="left",
                    va="center",
                )

        plt.tight_layout()
        plt.savefig(
            output_path / "12_algorithm_type_distribution.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    def print_summary_stats(self) -> None:
        """Print summary statistics for all configurations."""
        if not self.data:
            print("No data loaded. Call load_data() first.")
            return

        print("\n" + "=" * 80)
        print("SUMMARY STATISTICS")
        print("=" * 80)

        summary = (
            self.df.groupby("config_type")
            .agg(
                {
                    "success": ["count", "mean"],
                    "total_input_tokens": ["mean", "std"],
                    "total_cost_usd": ["mean", "std"],
                    "code_coverage_percent": ["mean", "std"],
                    "fix_attempts_used": ["mean", "std"],
                }
            )
            .round(3)
        )

        print(summary)

        print("\n" + "=" * 80)
        print("CONFIGURATION TYPE ANALYSIS")
        print("=" * 80)

        for config_type in sorted(self.df["config_type"].unique()):
            data = self.df[self.df["config_type"] == config_type]
            print(f"\n{config_type.upper()}:")
            print(f"  Samples: {len(data)}")
            print(f"  Success Rate: {data['success'].mean()*100:.1f}%")
            print(
                f"  Avg Input Tokens: {data['total_input_tokens'].mean():.0f} ± {data['total_input_tokens'].std():.0f}"
            )
            print(
                f"  Avg Cost: ${data['total_cost_usd'].mean():.4f} ± ${data['total_cost_usd'].std():.4f}"
            )
            print(
                f"  Avg Coverage: {data['code_coverage_percent'].mean():.1f}% ± {data['code_coverage_percent'].std():.1f}%"
            )
            print(
                f"  Avg Fix Attempts: {data['fix_attempts_used'].mean():.2f} ± {data['fix_attempts_used'].std():.2f}"
            )

        # Add dataset-aware analysis
        self.print_dataset_analysis()

    def print_dataset_analysis(self) -> None:
        """Print dataset-aware analysis including complexity and algorithm type breakdown."""
        if "complexity_level" not in self.df.columns:
            print("\nDataset classification not available.")
            return

        print("\n" + "=" * 80)
        print("DATASET COMPLEXITY ANALYSIS")
        print("=" * 80)

        # Overall complexity distribution
        complexity_dist = self.df["complexity_level"].value_counts()
        print("\nProblem Complexity Distribution:")
        for level, count in complexity_dist.items():
            percentage = (count / len(self.df)) * 100
            print(f"  {level.capitalize()}: {count} problems ({percentage:.1f}%)")

        # Success rates by complexity
        print("\nSuccess Rate by Complexity Level:")
        complexity_success = (
            self.df.groupby(
                ["complexity_level", "config_type_display"], observed=False
            )["success"]
            .agg(["mean", "count"])
            .reset_index()
        )
        complexity_success["success_rate"] = complexity_success["mean"] * 100

        for complexity in ["simple", "medium", "complex"]:
            complexity_data = complexity_success[
                complexity_success["complexity_level"] == complexity
            ]
            if not complexity_data.empty:
                print(f"\n  {complexity.capitalize()} Problems:")
                for _, row in complexity_data.iterrows():
                    config = row["config_type_display"]
                    rate = row["success_rate"]
                    count = row["count"]
                    print(f"    {config}: {rate:.1f}% ({count} samples)")

        # Algorithm type analysis
        if "algorithm_type" in self.df.columns:
            print("\n" + "=" * 80)
            print("ALGORITHM TYPE ANALYSIS")
            print("=" * 80)

            # Algorithm type distribution
            algo_dist = self.df["algorithm_type"].value_counts()
            print("\nAlgorithm Type Distribution:")
            for algo_type, count in algo_dist.head(10).items():  # Show top 10
                percentage = (count / len(self.df)) * 100
                print(
                    f"  {algo_type.replace('_', ' ').title()}: {count} problems ({percentage:.1f}%)"
                )

            # Success rates by algorithm type (for types with sufficient data)
            algo_success = (
                self.df.groupby("algorithm_type")["success"]
                .agg(["mean", "count"])
                .reset_index()
            )
            algo_success["success_rate"] = algo_success["mean"] * 100
            sufficient_algos = algo_success[algo_success["count"] >= 3].sort_values(
                "success_rate", ascending=False
            )

            if not sufficient_algos.empty:
                print("\nSuccess Rate by Algorithm Type (≥3 samples):")
                for _, row in sufficient_algos.iterrows():
                    algo = row["algorithm_type"].replace("_", " ").title()
                    rate = row["success_rate"]
                    count = row["count"]
                    print(f"  {algo}: {rate:.1f}% ({count} samples)")

        # Configuration effectiveness analysis
        print("\n" + "=" * 80)
        print("CONFIGURATION EFFECTIVENESS BY PROBLEM TYPE")
        print("=" * 80)

        # Best configuration for each complexity level
        if "complexity_level" in self.df.columns:
            print("\nBest Configuration by Complexity Level:")
            for complexity in ["simple", "medium", "complex"]:
                complexity_data = self.df[self.df["complexity_level"] == complexity]
                if not complexity_data.empty:
                    config_performance = (
                        complexity_data.groupby("config_type_display")["success"]
                        .agg(["mean", "count"])
                        .reset_index()
                    )
                    config_performance = config_performance[
                        config_performance["count"] >= 2
                    ]  # At least 2 samples
                    if not config_performance.empty:
                        best_config = config_performance.loc[
                            config_performance["mean"].idxmax()
                        ]
                        print(
                            f"  {complexity.capitalize()}: {best_config['config_type_display']} "
                            + f"({best_config['mean']*100:.1f}% success rate, {best_config['count']} samples)"
                        )
                    else:
                        print(f"  {complexity.capitalize()}: Insufficient data")


def main():
    """Main function to run the analysis."""
    analyzer = TestResultsAnalyzer()

    # Load data
    analyzer.load_data()

    if not analyzer.data:
        print("No data found to analyze.")
        return

    # Print summary statistics
    analyzer.print_summary_stats()

    # Create visualizations
    analyzer.create_visualizations()

    print(f"\nAnalysis complete! Check the 'visualizations/' directory for graphs.")


if __name__ == "__main__":
    main()
