#!/usr/bin/env python3
"""
Traditional Plotting Module

Contains the original 7 visualization methods for analyzing test generation
results across different configuration types.
"""

from pathlib import Path
from typing import List, Dict, Any
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class TraditionalPlots:
    """Handles the original 7 visualization methods for test result analysis."""

    def __init__(self, data: List[Dict[str, Any]], config_order: List[str]):
        """Initialize with loaded data and configuration order."""
        self.data = data
        self.config_order = config_order
        self.df = self._prepare_dataframe()

    def _prepare_dataframe(self) -> pd.DataFrame:
        """Prepare pandas DataFrame from loaded data."""
        df = pd.DataFrame(self.data)

        # Create ordered categorical for consistent display
        df["config_type_display"] = pd.Categorical(
            df["config_type"], categories=self.config_order, ordered=True
        )

        return df

    def create_all_plots(self, output_path: Path) -> None:
        """Create all traditional visualization plots."""
        print("Creating traditional visualizations...")

        self._plot_success_rate(output_path)
        print("  ✓ Created success rate analysis")

        self._plot_code_coverage(output_path)
        print("  ✓ Created code coverage analysis")

        self._plot_cost_analysis(output_path)
        print("  ✓ Created cost analysis")

        self._plot_fix_attempts(output_path)
        print("  ✓ Created fix attempts analysis")

        self._plot_success_by_problem(output_path)
        print("  ✓ Created success by problem heatmap")

        self._plot_cost_vs_quality(output_path)
        print("  ✓ Created cost vs quality scatter plot")

        self._plot_input_tokens(output_path)
        print("  ✓ Created input token analysis")

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
