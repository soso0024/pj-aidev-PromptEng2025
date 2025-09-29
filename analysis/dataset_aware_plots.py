#!/usr/bin/env python3
"""
Dataset-Aware Plotting Module

Contains the 6 enhanced visualization methods that analyze test generation
results by problem complexity and algorithm types.
"""

from pathlib import Path
from typing import List, Dict, Any
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DatasetAwarePlots:
    """Handles the 6 dataset-aware visualization methods for test result analysis."""

    def __init__(
        self,
        data: List[Dict[str, Any]],
        config_order: List[str],
        algorithm_type_order: List[str],
    ):
        """Initialize with loaded data and ordering configurations."""
        self.data = data
        self.config_order = config_order
        self.algorithm_type_order = algorithm_type_order
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
        """Create all dataset-aware visualization plots."""
        print("Creating dataset-aware visualizations...")

        self._plot_success_by_complexity(output_path)
        print("  ✓ Created success by complexity analysis")

        self._plot_success_by_algorithm_type(output_path)
        print("  ✓ Created success by algorithm type analysis")

        self._plot_config_performance_by_complexity(output_path)
        print("  ✓ Created configuration performance by complexity analysis")

        # self._plot_cost_vs_complexity(output_path)
        # print("  ✓ Created cost vs complexity analysis")

        self._plot_algorithm_type_distribution(output_path)
        print("  ✓ Created algorithm type distribution analysis")

        self._plot_algorithm_success_rates(output_path)
        print("  ✓ Created algorithm success rates analysis")

    def _plot_success_by_complexity(self, output_path: Path) -> None:
        """Plot success rate by problem complexity level."""
        if "complexity_level" not in self.df.columns:
            print(
                "Warning: complexity_level not found in data. Skipping complexity analysis."
            )
            return

        fig, ax = plt.subplots(figsize=(10, 6))

        # Success rate by complexity level
        complexity_order = ["simple", "medium", "complex"]
        complexity_data = self.df[self.df["complexity_level"].isin(complexity_order)]

        # Ensure proper ordering
        complexity_data["complexity_level"] = pd.Categorical(
            complexity_data["complexity_level"],
            categories=complexity_order,
            ordered=True,
        )

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
                    ax=ax,
                    cbar_kws={"label": "Success Rate"},
                )
            else:
                ax.text(
                    0.5,
                    0.5,
                    "No classified complexity data available",
                    ha="center",
                    va="center",
                    transform=ax.transAxes,
                )
        else:
            ax.text(
                0.5,
                0.5,
                "No classified complexity data available",
                ha="center",
                va="center",
                transform=ax.transAxes,
            )
        ax.set_title("Success Rate Heatmap by Complexity", fontweight="bold")
        ax.set_xlabel("Configuration Type")
        ax.set_ylabel("Problem Complexity Level")

        plt.tight_layout()
        plt.savefig(
            output_path / "6_success_by_complexity.png", dpi=300, bbox_inches="tight"
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
            output_path / "7_success_by_algorithm_type.png",
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
            output_path / "8_config_performance_by_complexity.png",
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
        # Both complexity score and cost should be non-negative
        ax1.set_xlim(left=0)
        ax1.set_ylim(bottom=0)
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
            # Cost cannot be negative
            ax2.set_ylim(bottom=0)
            ax2.legend(
                title="Configuration", bbox_to_anchor=(1.05, 1), loc="upper left"
            )

        plt.tight_layout()
        plt.savefig(
            output_path / "9_cost_vs_complexity.png", dpi=300, bbox_inches="tight"
        )
        plt.close()

    def _plot_algorithm_type_distribution(self, output_path: Path) -> None:
        """Plot distribution of different algorithm types."""
        if "algorithm_type" not in self.df.columns:
            print(
                "Warning: algorithm_type not found in data. Skipping algorithm distribution analysis."
            )
            return

        fig, ax = plt.subplots(figsize=(10, 8))

        # Pie chart of algorithm type distribution
        algo_counts = self.df["algorithm_type"].value_counts()
        # Only show types with more than 1% of data
        threshold = len(self.df) * 0.01
        major_algos = algo_counts[algo_counts >= threshold]
        other_count = algo_counts[algo_counts < threshold].sum()

        if other_count > 0:
            major_algos["other"] = other_count

        ax.pie(
            major_algos.values,
            labels=major_algos.index,
            autopct="%1.1f%%",
            startangle=90,
        )
        ax.set_title("Distribution of Algorithm Types in Dataset", fontweight="bold")

        plt.tight_layout()
        plt.savefig(
            output_path / "9_algorithm_type_distribution.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    def _plot_algorithm_success_rates(self, output_path: Path) -> None:
        """Plot success rates by algorithm type."""
        if "algorithm_type" not in self.df.columns:
            print(
                "Warning: algorithm_type not found in data. Skipping algorithm success rates analysis."
            )
            return

        fig, ax = plt.subplots(figsize=(12, 8))

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
            bars = ax.barh(
                sufficient_data["algorithm_type"], sufficient_data["success_rate"]
            )
            ax.set_title(
                "Success Rate by Algorithm Type\n(Types with ≥3 samples)",
                fontweight="bold",
            )
            ax.set_xlabel("Success Rate (%)")
            ax.set_ylabel("Algorithm Type")

            # Add value labels
            for bar, rate, count in zip(
                bars, sufficient_data["success_rate"], sufficient_data["count"]
            ):
                ax.text(
                    bar.get_width() + 1,
                    bar.get_y() + bar.get_height() / 2,
                    f"{rate:.1f}% (n={count})",
                    ha="left",
                    va="center",
                )

        plt.tight_layout()
        plt.savefig(
            output_path / "10_algorithm_success_rates.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()
