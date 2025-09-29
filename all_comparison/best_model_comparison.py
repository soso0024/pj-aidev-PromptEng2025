#!/usr/bin/env python3
"""
Best Model Comparison Plot

Creates a scatter plot showing the best configuration from each model based on
cost-performance efficiency (coverage per $0.001).

Usage:
    python best_model_comparison.py
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import analysis modules
sys.path.append(str(Path(__file__).parent.parent))
from analysis.data_loader import DataLoader
from analysis.problem_classifier import ProblemClassifier


class BestModelComparison:
    """Creates comparison plots of best configurations across models."""

    def __init__(self, base_dir: str = None):
        """Initialize with base directory containing model data."""
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent
        else:
            self.base_dir = Path(base_dir)

        self.data = []

    def _format_model_name(self, model_name: str) -> str:
        """Format model name for display."""
        # Special cases for specific models
        if model_name == "claude-3-5-haiku":
            return "Claude 3.5 Haiku"
        elif model_name == "claude-opus-4-1":
            return "Claude 4.1 Opus"
        elif model_name == "claude-4-sonnet":
            return "Claude 4 Sonnet"
        elif model_name == "claude-3-haiku":
            return "Claude 3 Haiku"
        else:
            # Fallback: replace hyphens with spaces and title case
            return model_name.replace("-", " ").title()

    def load_all_model_data(self) -> None:
        """Load data from all model directories."""
        print("=" * 80)
        print("LOADING DATA FROM ALL MODELS")
        print("=" * 80)

        # Find all model-specific directories
        model_dirs = []
        for path in self.base_dir.glob("generated_tests_*"):
            if path.is_dir():
                model_dirs.append(path)

        if not model_dirs:
            print("No model directories found (generated_tests_*)")
            return

        print(f"Found {len(model_dirs)} model directories:")
        for model_dir in model_dirs:
            print(f"  - {model_dir.name}")

        # Load data from each model directory
        dataset_path = self.base_dir / "dataset" / "HumanEval.jsonl"

        for model_dir in model_dirs:
            print(f"\nLoading data from {model_dir.name}...")

            # Create data loader for this model
            loader = DataLoader(str(model_dir), str(dataset_path))
            model_data = loader.load_data()

            print(f"  Loaded {len(model_data)} records")
            self.data.extend(model_data)

        print(f"\nTotal loaded {len(self.data)} records from all models")

        # Show summary of models found
        models = set()
        for record in self.data:
            model = record.get("model", "unknown")
            if model != "unknown":
                models.add(model)

        print(f"Models found: {sorted(models)}")

    def calculate_best_configs(self) -> pd.DataFrame:
        """
        Calculate the best configuration for each model based on cost-performance efficiency.

        Formula: coverage_percent / (cost_usd * 1000) = coverage per $0.001
        """
        if not self.data:
            print("No data loaded. Call load_all_model_data() first.")
            return pd.DataFrame()

        df = pd.DataFrame(self.data)

        # Create config_type_display column with proper ordering
        config_order = ["basic", "ast", "docstring", "docstring_ast", "ast-fix"]
        df["config_type_display"] = pd.Categorical(
            df["config_type"], categories=config_order, ordered=True
        )

        # Get models, excluding 'unknown'
        valid_models = [model for model in df["model"].unique() if model != "unknown"]

        if not valid_models:
            print("Warning: No valid model data found.")
            return pd.DataFrame()

        best_configs = []

        for model in valid_models:
            model_data = df[df["model"] == model]

            # Calculate stats by configuration
            config_stats = (
                model_data.groupby("config_type_display", observed=False)
                .agg(
                    {
                        "total_cost_usd": "mean",
                        "code_coverage_percent": "mean",
                        "success": "mean",
                        "config_type": "count",  # for sample size
                    }
                )
                .reset_index()
            )

            # Calculate cost-performance efficiency: coverage per $0.001
            config_stats["efficiency_score"] = config_stats["code_coverage_percent"] / (
                config_stats["total_cost_usd"] * 1000
            )

            # Find the best configuration (highest efficiency score)
            best_idx = config_stats["efficiency_score"].idxmax()
            best_config = config_stats.loc[best_idx].copy()
            best_config["model"] = model

            print(f"\n{model} best configuration:")
            print(f"  Config: {best_config['config_type_display']}")
            print(f"  Coverage: {best_config['code_coverage_percent']:.1f}%")
            print(f"  Cost: ${best_config['total_cost_usd']:.4f}")
            print(
                f"  Efficiency Score: {best_config['efficiency_score']:.1f} coverage/$0.001"
            )
            print(f"  Success Rate: {best_config['success']*100:.1f}%")
            print(f"  Sample Size: {int(best_config['config_type'])}")

            best_configs.append(best_config)

        result_df = pd.DataFrame(best_configs) if best_configs else pd.DataFrame()
        if not result_df.empty:
            result_df = result_df.reset_index(drop=True)
        return result_df

    def create_comparison_plot(self, output_path: Path = None) -> None:
        """Create the best model comparison scatter plot."""
        if output_path is None:
            output_path = Path("all_comparison")

        output_path.mkdir(exist_ok=True)

        best_configs = self.calculate_best_configs()

        if best_configs.empty:
            print("Warning: No data available for comparison plot.")
            return

        # Create the plot
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))

        # Color map for different models
        model_colors = {
            "claude-4-sonnet": "#E74C3C",  # Red
            "claude-3-5-haiku": "#3498DB",  # Blue
            "claude-3-haiku": "#2ECC71",  # Green
            "claude-opus-4-1": "#9B59B6",  # Purple
            "gpt-4": "#F39C12",  # Orange
            "gpt-3.5": "#1ABC9C",  # Turquoise
        }

        # Plot each model's best configuration
        for _, row in best_configs.iterrows():
            model = row["model"]
            cost = row["total_cost_usd"]
            coverage = row["code_coverage_percent"]
            config = row["config_type_display"]
            count = row["config_type"]
            success_rate = row["success"] * 100
            efficiency = row["efficiency_score"]

            color = model_colors.get(model, "#95A5A6")  # Default gray

            # Plot point
            ax.scatter(
                cost,
                coverage,
                color=color,
                s=200,  # Large points for visibility
                alpha=0.8,
                edgecolors="black",
                linewidths=2,
                label=self._format_model_name(model),
            )

            # Add model name and config annotation
            ax.annotate(
                f"{self._format_model_name(model)}\n({config})",
                (cost, coverage),
                xytext=(10, 10),
                textcoords="offset points",
                fontsize=14,
                fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.3),
                ha="left",
            )

            # Add efficiency score in smaller text
            ax.annotate(
                f"Efficiency: {efficiency:.1f}\nSuccess: {success_rate:.1f}%",
                (cost, coverage),
                xytext=(10, -30),
                textcoords="offset points",
                fontsize=12,
                fontweight="bold",
                alpha=0.7,
                ha="left",
            )

        # Formatting
        ax.set_xlabel("Average Total Cost (USD)", fontsize=16, fontweight="bold")
        ax.set_ylabel("Average Code Coverage (%)", fontsize=16, fontweight="bold")

        # Set tick label font size
        ax.tick_params(axis="both", which="major", labelsize=12)

        ax.set_title(
            "Best Configuration Comparison Across Models\n"
            "Selection Criterion: Highest Cost-Performance Efficiency (Coverage per $0.001)",
            fontsize=20,
            fontweight="bold",
            pad=20,
        )

        ax.grid(True, alpha=0.3)

        # Set axis limits with padding based on actual data range
        if len(best_configs) > 0:
            cost_min = best_configs["total_cost_usd"].min()
            cost_max = best_configs["total_cost_usd"].max()
            coverage_min = best_configs["code_coverage_percent"].min()
            coverage_max = best_configs["code_coverage_percent"].max()

            cost_range = cost_max - cost_min
            coverage_range = coverage_max - coverage_min

            cost_padding = max(cost_range * 0.15, 0.002)
            coverage_padding = max(coverage_range * 0.15, 3)

            ax.set_xlim(max(0, cost_min - cost_padding), cost_max + cost_padding)
            ax.set_ylim(
                max(0, coverage_min - coverage_padding),
                min(100, coverage_max + coverage_padding),
            )

        # Add legend inside the plot area
        ax.legend(
            loc="center right",
            fontsize=12,
            title="Models",
            title_fontsize=14,
            framealpha=0.9,
            fancybox=True,
            shadow=True,
        )

        # Add summary statistics
        stats_text = self._generate_summary_stats(best_configs)
        ax.text(
            0.98,
            0.02,
            stats_text,
            transform=ax.transAxes,
            fontsize=12,
            fontweight="bold",
            verticalalignment="bottom",
            horizontalalignment="right",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.8),
        )

        # Adjust layout with extra space for annotations
        plt.subplots_adjust(left=0.08, right=0.85, top=0.88, bottom=0.12)

        # Save the plot
        filename = "best_model_comparison.png"
        plt.savefig(
            output_path / filename,
            dpi=300,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
        )
        plt.close()

        print(f"\n✅ Comparison plot saved: {output_path / filename}")

    def _generate_summary_stats(self, best_configs: pd.DataFrame) -> str:
        """Generate summary statistics text for the plot."""
        if best_configs.empty:
            return "No data available"

        # Find best performing models using argmax/argmin for iloc compatibility
        best_coverage_idx = best_configs["code_coverage_percent"].argmax()
        lowest_cost_idx = best_configs["total_cost_usd"].argmin()
        best_efficiency_idx = best_configs["efficiency_score"].argmax()

        # Get the actual values using iloc to avoid Series formatting issues
        best_coverage_row = best_configs.iloc[best_coverage_idx]
        lowest_cost_row = best_configs.iloc[lowest_cost_idx]
        best_efficiency_row = best_configs.iloc[best_efficiency_idx]

        stats_text = "SUMMARY:\n"
        stats_text += f"Best Coverage: {self._format_model_name(best_coverage_row['model'])} ({best_coverage_row['code_coverage_percent']:.1f}%)\n"
        stats_text += f"Lowest Cost: {self._format_model_name(lowest_cost_row['model'])} (${lowest_cost_row['total_cost_usd']:.4f})\n"
        stats_text += f"Best Efficiency: {self._format_model_name(best_efficiency_row['model'])} ({best_efficiency_row['efficiency_score']:.1f})"

        return stats_text


def main():
    """Main function to create the comparison plot."""
    print("🔍 Best Model Configuration Comparison Tool")
    print("=" * 50)

    # Initialize comparison tool
    comparison = BestModelComparison()

    # Load data from all models
    comparison.load_all_model_data()

    # Create comparison plot
    comparison.create_comparison_plot()

    print("\n🎉 Comparison analysis complete!")


if __name__ == "__main__":
    main()
