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

    def _format_model_name(self, model_name: str) -> str:
        """Format model name for display."""
        model_display_names = {
            "claude-3-5-haiku": "Claude 3.5 Haiku",
            "claude-opus-4-1": "Claude Opus 4.1",
            "claude-4-sonnet": "Claude 4 Sonnet",
            "claude-3-haiku": "Claude 3 Haiku",
        }
        return model_display_names.get(model_name, model_name.replace("-", " ").title())

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

        self._plot_cost_vs_coverage_by_model(output_path)
        print("  ✓ Created cost vs coverage by model analysis")

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
                heatmap = sns.heatmap(
                    pivot_heatmap,
                    annot=True,
                    fmt=".2f",
                    cmap="RdYlGn",
                    ax=ax,
                    cbar_kws={"label": "Success Rate"},
                    annot_kws={"fontsize": 16, "fontweight": "bold"},
                )
                # Increase colorbar label and tick label sizes
                cbar = heatmap.collections[0].colorbar
                cbar.ax.tick_params(labelsize=14)
                cbar.set_label("Success Rate", size=16)
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
        ax.set_xlabel("Configuration Type", fontsize=20, fontweight="bold")
        ax.set_ylabel("Problem Complexity Level", fontsize=20, fontweight="bold")
        ax.tick_params(axis="both", which="major", labelsize=16)

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
                "Success Rate by Algorithm Type and Configuration",
                fontsize=20,
                fontweight="bold",
            )
            ax.set_xlabel("Algorithm Type", fontsize=16, fontweight="bold")
            ax.set_ylabel("Success Rate (%)", fontsize=16, fontweight="bold")
            ax.legend(
                title="Configuration",
                bbox_to_anchor=(1.05, 1),
                loc="upper left",
                fontsize=12,
                title_fontsize=14,
            )
            ax.tick_params(axis="x", rotation=45, labelsize=12)
            ax.tick_params(axis="y", labelsize=12)

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
            axes[idx].set_title(
                f"{ylabel} by Complexity Level", fontsize=20, fontweight="bold"
            )
            axes[idx].set_xlabel(
                "Problem Complexity Level", fontsize=16, fontweight="bold"
            )
            axes[idx].set_ylabel(ylabel, fontsize=16, fontweight="bold")
            axes[idx].legend(
                title="Configuration",
                bbox_to_anchor=(1.05, 1),
                loc="upper left",
                fontsize=12,
                title_fontsize=14,
            )
            axes[idx].set_xticklabels(axes[idx].get_xticklabels(), rotation=0)
            axes[idx].tick_params(axis="both", which="major", labelsize=12)

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
            textprops={"fontsize": 14, "fontweight": "bold"},
        )
        ax.set_title(
            "Distribution of Algorithm Types in Dataset", fontsize=20, fontweight="bold"
        )

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
                fontsize=20,
                fontweight="bold",
            )
            ax.set_xlabel("Success Rate (%)", fontsize=16, fontweight="bold")
            ax.set_ylabel("Algorithm Type", fontsize=16, fontweight="bold")
            ax.tick_params(axis="both", which="major", labelsize=12)

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
                    fontsize=14,
                    fontweight="bold",
                )

        plt.tight_layout()
        plt.savefig(
            output_path / "10_algorithm_success_rates.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    def _plot_cost_vs_coverage_by_model(self, output_path: Path) -> None:
        """Plot cost vs coverage scatter plots for each model."""
        if "model" not in self.df.columns:
            print(
                "Warning: model information not found in data. Skipping cost vs coverage by model analysis."
            )
            return

        # Get unique models, excluding 'unknown'
        models = [model for model in self.df["model"].unique() if model != "unknown"]

        if not models:
            print(
                "Warning: No valid model data found. Skipping cost vs coverage by model analysis."
            )
            return

        # If only one model, create a single focused plot
        if len(models) == 1:
            model = models[0]
            fig, ax = plt.subplots(1, 1, figsize=(10, 8))

            model_data = self.df[self.df["model"] == model]

            # Color map for different configurations
            config_colors = {
                "basic": "#1f77b4",
                "ast": "#ff7f0e",
                "docstring": "#2ca02c",
                "docstring_ast": "#d62728",
                "ast-fix": "#9467bd",
            }

            # Calculate average cost and coverage by configuration
            avg_stats = (
                model_data.groupby("config_type_display", observed=False)
                .agg(
                    {
                        "total_cost_usd": "mean",
                        "code_coverage_percent": "mean",
                        "success": "mean",  # success rate
                        "config_type": "count",  # for sample size
                    }
                )
                .reset_index()
            )

            # Calculate efficiency score (coverage per $0.001)
            avg_stats["efficiency_score"] = avg_stats["code_coverage_percent"] / (
                avg_stats["total_cost_usd"] * 1000
            )

            # Plot scatter points for each configuration
            for _, row in avg_stats.iterrows():
                config = row["config_type_display"]
                cost = row["total_cost_usd"]
                coverage = row["code_coverage_percent"]
                count = row["config_type"]
                success_rate = row["success"] * 100
                efficiency = row["efficiency_score"]

                color = config_colors.get(config, "#888888")
                ax.scatter(
                    cost,
                    coverage,
                    color=color,
                    s=150,
                    alpha=0.8,
                    label=config,
                    edgecolors="black",
                    linewidths=1,
                )

                # Add text annotation with configuration name
                ax.annotate(
                    config,
                    (cost, coverage),
                    xytext=(8, 8),
                    textcoords="offset points",
                    fontsize=18,
                    fontweight="bold",
                    alpha=0.9,
                )

                # Add efficiency and success rate annotations
                # Position text on the left for 'ast' configuration, right for others
                x_offset = -8 if config == "ast" else 8
                h_align = "right" if config == "ast" else "left"
                # Adjust y_offset for better spacing, especially for docstring_ast
                y_offset = -30
                ax.annotate(
                    f"Efficiency: {efficiency:.1f}\nSuccess: {success_rate:.1f}%",
                    (cost, coverage),
                    xytext=(x_offset, y_offset),
                    textcoords="offset points",
                    fontsize=16,
                    fontweight="bold",
                    alpha=0.7,
                    ha=h_align,
                )

            # Formatting
            ax.set_xlabel("Average Total Cost (USD)", fontsize=20, fontweight="bold")
            ax.set_ylabel("Average Code Coverage (%)", fontsize=20, fontweight="bold")
            # Title removed for paper publication
            ax.tick_params(axis="both", which="major", labelsize=16)
            ax.grid(True, alpha=0.3)

            # Set axis limits based on actual data range with some padding
            if not avg_stats.empty:
                cost_min = avg_stats["total_cost_usd"].min()
                cost_max = avg_stats["total_cost_usd"].max()
                coverage_min = avg_stats["code_coverage_percent"].min()
                coverage_max = avg_stats["code_coverage_percent"].max()

                # Add padding (10% of range) for better visualization
                cost_range = cost_max - cost_min
                coverage_range = coverage_max - coverage_min

                cost_padding = max(
                    cost_range * 0.1, 0.001
                )  # Minimum padding for small ranges
                coverage_padding = max(
                    coverage_range * 0.1, 2
                )  # Minimum 2% padding for coverage

                ax.set_xlim(max(0, cost_min - cost_padding), cost_max + cost_padding)
                ax.set_ylim(
                    max(0, coverage_min - coverage_padding),
                    min(100, coverage_max + coverage_padding),
                )
            else:
                ax.set_xlim(left=0)
                ax.set_ylim(0, 100)

            # Add legend
            ax.legend(loc="upper right", fontsize=16)

            plt.tight_layout()

        else:
            # Multiple models - use subplot layout
            n_models = len(models)
            if n_models == 2:
                fig, axes = plt.subplots(1, 2, figsize=(16, 6))
            elif n_models <= 4:
                fig, axes = plt.subplots(2, 2, figsize=(16, 12))
                axes = axes.ravel()
            else:
                # For more than 4 models, use a larger grid
                cols = 3
                rows = (n_models + cols - 1) // cols
                fig, axes = plt.subplots(rows, cols, figsize=(6 * cols, 6 * rows))
                axes = axes.ravel()

            # Color map for different configurations
            config_colors = {
                "basic": "#1f77b4",
                "ast": "#ff7f0e",
                "docstring": "#2ca02c",
                "docstring_ast": "#d62728",
                "ast-fix": "#9467bd",
            }

            for idx, model in enumerate(models):
                if idx >= len(axes):
                    break

                ax = axes[idx]
                model_data = self.df[self.df["model"] == model]

                # Calculate average cost and coverage by configuration
                avg_stats = (
                    model_data.groupby("config_type_display", observed=False)
                    .agg(
                        {
                            "total_cost_usd": "mean",
                            "code_coverage_percent": "mean",
                            "success": "mean",  # success rate
                            "config_type": "count",  # for sample size
                        }
                    )
                    .reset_index()
                )

                # Calculate efficiency score (coverage per $0.001)
                avg_stats["efficiency_score"] = avg_stats["code_coverage_percent"] / (
                    avg_stats["total_cost_usd"] * 1000
                )

                # Plot scatter points for each configuration
                for _, row in avg_stats.iterrows():
                    config = row["config_type_display"]
                    cost = row["total_cost_usd"]
                    coverage = row["code_coverage_percent"]
                    count = row["config_type"]
                    success_rate = row["success"] * 100
                    efficiency = row["efficiency_score"]

                    color = config_colors.get(config, "#888888")
                    ax.scatter(
                        cost,
                        coverage,
                        color=color,
                        s=100,
                        alpha=0.8,
                        label=config,
                        edgecolors="black",
                        linewidths=0.5,
                    )

                    # Add text annotation with configuration name
                    ax.annotate(
                        config,
                        (cost, coverage),
                        xytext=(5, 5),
                        textcoords="offset points",
                        fontsize=18,
                        fontweight="bold",
                        alpha=0.8,
                    )

                    # Add efficiency and success rate annotations
                    ax.annotate(
                        f"Efficiency: {efficiency:.1f}\nSuccess: {success_rate:.1f}%",
                        (cost, coverage),
                        xytext=(5, -20),
                        textcoords="offset points",
                        fontsize=16,
                        fontweight="bold",
                        alpha=0.7,
                    )

                # Formatting
                ax.set_xlabel(
                    "Average Total Cost (USD)", fontsize=20, fontweight="bold"
                )
                ax.set_ylabel(
                    "Average Code Coverage (%)", fontsize=20, fontweight="bold"
                )
                # Individual subplot titles removed for paper publication
                ax.tick_params(axis="both", which="major", labelsize=16)
                ax.grid(True, alpha=0.3)

                # Set axis limits based on actual data range with some padding
                if not avg_stats.empty:
                    cost_min = avg_stats["total_cost_usd"].min()
                    cost_max = avg_stats["total_cost_usd"].max()
                    coverage_min = avg_stats["code_coverage_percent"].min()
                    coverage_max = avg_stats["code_coverage_percent"].max()

                    # Add padding (10% of range) for better visualization
                    cost_range = cost_max - cost_min
                    coverage_range = coverage_max - coverage_min

                    cost_padding = max(
                        cost_range * 0.1, 0.001
                    )  # Minimum padding for small ranges
                    coverage_padding = max(
                        coverage_range * 0.1, 2
                    )  # Minimum 2% padding for coverage

                    ax.set_xlim(
                        max(0, cost_min - cost_padding), cost_max + cost_padding
                    )
                    ax.set_ylim(
                        max(0, coverage_min - coverage_padding),
                        min(100, coverage_max + coverage_padding),
                    )
                else:
                    ax.set_xlim(left=0)
                    ax.set_ylim(0, 100)

                # Add legend
                ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=16)

            # Hide empty subplots if any
            for idx in range(n_models, len(axes)):
                axes[idx].set_visible(False)

            # Overall title removed for paper publication

            plt.tight_layout()

        plt.savefig(
            output_path / "11_cost_vs_coverage_by_model.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()
