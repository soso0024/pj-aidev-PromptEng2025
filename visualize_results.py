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


class TestResultsAnalyzer:
    def __init__(self, results_dir: str = "generated_tests"):
        """Initialize the analyzer with the results directory."""
        self.results_dir = Path(results_dir)
        self.data = []
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

    def load_data(self) -> None:
        """Load all stats.json files and parse them."""
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
