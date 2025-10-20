#!/usr/bin/env python3
"""
Pareto Front Analysis: Cost vs Effective Coverage

Introduces Effective Coverage = Coverage * Success Rate / 100
Creates a Pareto Front plot showing all model-configuration combinations,
highlighting the optimal trade-offs between cost and effective coverage.

Usage:
    python pareto_front_analysis.py
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Add parent directory to path to import analysis modules
sys.path.append(str(Path(__file__).parent.parent))
from analysis.data_loader import DataLoader
from analysis.problem_classifier import ProblemClassifier


class ParetoFrontAnalysis:
    """Creates Pareto Front analysis plot comparing all model-configuration combinations."""

    def __init__(self, base_dir: str = None):
        """Initialize with base directory containing model data."""
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent
        else:
            self.base_dir = Path(base_dir)

        self.data = []

        # Define the models and configurations we expect
        # Focused on 3 main models for better visualization
        self.expected_models = [
            "claude-3-5-haiku",
            "claude-4-sonnet",
            "claude-4-5-sonnet",
            # "claude-opus-4-1",
            # "claude-3-haiku",
        ]

        self.expected_configs = ["basic", "ast", "docstring", "docstring_ast"]

    def _format_model_name(self, model_name: str) -> str:
        """Format model name for display."""
        model_display_names = {
            "claude-3-5-haiku": "Claude 3.5 Haiku",
            "claude-opus-4-1": "Claude 4.1 Opus",
            "claude-4-sonnet": "Claude 4 Sonnet",
            "claude-4-5-sonnet": "Claude 4.5 Sonnet",
            "claude-3-haiku": "Claude 3 Haiku",
        }
        return model_display_names.get(model_name, model_name.replace("-", " ").title())

    def _format_config_name(self, config_name: str) -> str:
        """Format configuration name for display."""
        config_display_names = {
            "basic": "basic",
            "ast": "ast",
            "docstring": "docstring",
            "docstring_ast": "docstring_ast",
        }
        return config_display_names.get(config_name, config_name.title())

    def load_all_model_data(self) -> None:
        """Load data only from expected model directories for efficiency."""
        print("=" * 80)
        print("LOADING DATA FROM EXPECTED MODELS FOR PARETO FRONT ANALYSIS")
        print("=" * 80)

        # Find only the model directories for expected models
        data_dir = self.base_dir / "data"
        model_dirs = []

        print(f"Looking for expected models: {self.expected_models}")

        for model_name in self.expected_models:
            model_dir = data_dir / f"generated_tests_{model_name}"
            if model_dir.is_dir():
                model_dirs.append(model_dir)
            else:
                print(f"Warning: Model directory not found: {model_dir.name}")

        if not model_dirs:
            print(f"No expected model directories found in {data_dir}")
            print(f"Expected directories: {[f'generated_tests_{m}' for m in self.expected_models]}")
            return

        print(f"\nFound {len(model_dirs)} of {len(self.expected_models)} expected model directories:")
        for model_dir in model_dirs:
            print(f"  - {model_dir.name}")

        # Load data from each expected model directory
        dataset_path = self.base_dir / "dataset" / "HumanEval.jsonl"

        for model_dir in model_dirs:
            print(f"\nLoading data from {model_dir.name}...")

            # Create data loader for this model
            loader = DataLoader(str(model_dir), str(dataset_path))
            model_data = loader.load_data()

            print(f"  Loaded {len(model_data)} records")
            self.data.extend(model_data)

        print(f"\nTotal loaded {len(self.data)} records from {len(model_dirs)} models")

        # Show summary of models found
        models = set()
        for record in self.data:
            model = record.get("model", "unknown")
            if model != "unknown":
                models.add(model)

        print(f"Models found: {sorted(models)}")

    def calculate_all_metrics(self) -> pd.DataFrame:
        """
        Calculate metrics for all model-configuration combinations.

        Calculates:
        - Average Cost (USD)
        - Average Code Coverage (%)
        - Success Rate (%)
        - Effective Coverage (%) = Coverage * Success Rate / 100
        """
        if not self.data:
            print("No data loaded. Call load_all_model_data() first.")
            return pd.DataFrame()

        df = pd.DataFrame(self.data)

        # Filter out 'unknown' models and focus on expected configurations
        df = df[df["model"] != "unknown"]
        df = df[df["config_type"].isin(self.expected_configs)]

        print(f"\nProcessing {len(df)} records for metrics calculation...")

        # Calculate metrics for each model-configuration combination
        results = []

        for model in self.expected_models:
            model_data = df[df["model"] == model]

            if model_data.empty:
                print(f"Warning: No data found for model {model}")
                continue

            print(f"\nProcessing {model} ({len(model_data)} records)...")

            for config in self.expected_configs:
                config_data = model_data[model_data["config_type"] == config]

                if config_data.empty:
                    print(f"  {config}: No data available")
                    continue

                # Calculate metrics (same as comprehensive_table_generator.py)
                avg_cost = config_data["total_cost_usd"].mean()
                avg_coverage = config_data["code_coverage_percent"].mean()
                success_rate = config_data["success"].mean() * 100

                # Calculate Effective Coverage = Coverage * Success Rate / 100
                effective_coverage = (avg_coverage * success_rate) / 100

                sample_size = len(config_data)

                results.append(
                    {
                        "Model": self._format_model_name(model),
                        "ModelKey": model,  # Keep original for sorting
                        "Configuration": self._format_config_name(config),
                        "ConfigKey": config,  # Keep original for sorting
                        "Average Cost (USD)": avg_cost,
                        "Average Code Coverage (%)": avg_coverage,
                        "Success Rate (%)": success_rate,
                        "Effective Coverage (%)": effective_coverage,
                        "Sample Size": sample_size,
                    }
                )

                print(
                    f"  {config}: Cost=${avg_cost:.4f}, Coverage={avg_coverage:.1f}%, "
                    f"Success={success_rate:.1f}%, Effective Coverage={effective_coverage:.1f}%, "
                    f"Samples={sample_size}"
                )

        return pd.DataFrame(results)

    def find_pareto_front(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Find Pareto optimal points (minimize cost, maximize effective coverage).

        A point is Pareto optimal if no other point has both:
        - Lower or equal cost AND higher effective coverage
        """
        if df.empty:
            return df

        pareto_points = []

        for i, row_i in df.iterrows():
            is_dominated = False
            cost_i = row_i["Average Cost (USD)"]
            eff_cov_i = row_i["Effective Coverage (%)"]

            for j, row_j in df.iterrows():
                if i == j:
                    continue

                cost_j = row_j["Average Cost (USD)"]
                eff_cov_j = row_j["Effective Coverage (%)"]

                # Check if row_i is dominated by row_j
                # (row_j has lower/equal cost AND higher effective coverage)
                if cost_j <= cost_i and eff_cov_j > eff_cov_i:
                    is_dominated = True
                    break

            if not is_dominated:
                pareto_points.append(i)

        pareto_df = df.loc[pareto_points].sort_values("Average Cost (USD)")
        return pareto_df

    def create_pareto_front_plot_all(self, output_dir: Path = None) -> None:
        """
        Create Pareto Front plot for all model-configuration combinations.
        """
        if output_dir is None:
            output_dir = Path("all_comparison")

        output_dir.mkdir(exist_ok=True)

        # Calculate metrics for all combinations
        all_metrics = self.calculate_all_metrics()

        if all_metrics.empty:
            print("Warning: No data available for Pareto Front plot (all combinations).")
            return

        # Find Pareto front
        pareto_front = self.find_pareto_front(all_metrics)

        print("\n" + "=" * 80)
        print("PARETO FRONT POINTS (ALL COMBINATIONS)")
        print("=" * 80)
        for _, row in pareto_front.iterrows():
            print(
                f"{row['Model']} - {row['Configuration']}: "
                f"Cost=${row['Average Cost (USD)']:.4f}, "
                f"Effective Coverage={row['Effective Coverage (%)']:.1f}%"
            )

        # Create the plot with smaller size
        fig, ax = plt.subplots(1, 1, figsize=(10, 7))

        # Color map for different models (matching best_model_comparison.py)
        model_colors = {
            "claude-3-5-haiku": "#005AFF",   # Blue
            "claude-4-sonnet": "#03AF7A",    # Green
            "claude-4-5-sonnet": "#FF4B00",     # Red
        }

        # Marker shapes for different configurations
        config_markers = {
            "basic": "o",
            "ast": "s",
            "docstring": "^",
            "docstring_ast": "D",
        }

        # Plot all points
        for _, row in all_metrics.iterrows():
            model_key = row["ModelKey"]
            config = row["Configuration"]
            cost = row["Average Cost (USD)"]
            eff_cov = row["Effective Coverage (%)"]

            color = model_colors.get(model_key, "#95A5A6")
            marker = config_markers.get(config, "o")

            # Check if this point is on the Pareto front
            is_pareto = row.name in pareto_front.index

            if is_pareto:
                # Pareto front points: larger, with black edge
                ax.scatter(
                    cost,
                    eff_cov,
                    color=color,
                    marker=marker,
                    s=350,
                    alpha=0.95,
                    edgecolors="black",
                    linewidths=3,
                    zorder=3,
                )
            else:
                # Non-Pareto points: clearly visible
                ax.scatter(
                    cost,
                    eff_cov,
                    color=color,
                    marker=marker,
                    s=250,
                    alpha=0.85,
                    edgecolors="black",
                    linewidths=1.5,
                    zorder=2,
                )

        # Draw Pareto front line
        if len(pareto_front) > 1:
            pareto_sorted = pareto_front.sort_values("Average Cost (USD)")
            ax.plot(
                pareto_sorted["Average Cost (USD)"],
                pareto_sorted["Effective Coverage (%)"],
                "k--",
                linewidth=3,
                alpha=0.7,
                label="Pareto Front",
                zorder=1,
            )

        # Adjust axis limits to focus on data points and reduce empty space
        x_min = all_metrics["Average Cost (USD)"].min()
        x_max = all_metrics["Average Cost (USD)"].max()
        y_min = all_metrics["Effective Coverage (%)"].min()
        y_max = all_metrics["Effective Coverage (%)"].max()

        # Add small margins (5% on each side)
        x_margin = (x_max - x_min) * 0.05
        y_margin = (y_max - y_min) * 0.05

        ax.set_xlim(x_min - x_margin, x_max + x_margin)
        ax.set_ylim(y_min - y_margin, y_max + y_margin)

        # Formatting
        ax.set_xlabel("Average Total Cost (USD)", fontsize=22, fontweight="bold")
        ax.set_ylabel("Effective Coverage (%)", fontsize=22, fontweight="bold") # Effective Coverage (%) = Coverage × Success Rate / 100
        # ax.set_title(
        #     "Pareto Front: Cost vs Effective Coverage\n(All Model-Configuration Combinations)",
        #     fontsize=16,
        #     fontweight="bold",
        #     pad=20,
        # )

        # Set x-axis ticks to 0.01 intervals
        ax.xaxis.set_major_locator(MultipleLocator(0.01))

        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.grid(True, alpha=0.4, linestyle="-", linewidth=0.8)

        # Create custom legend for models
        from matplotlib.lines import Line2D
        model_legend_elements = []
        for model_key in self.expected_models:
            model_display = self._format_model_name(model_key)
            if model_key in model_colors:
                model_legend_elements.append(
                    Line2D(
                        [0],
                        [0],
                        marker="o",
                        color="w",
                        markerfacecolor=model_colors[model_key],
                        markersize=10,
                        label=model_display,
                    )
                )

        # Create custom legend for configurations
        config_legend_elements = []
        for config, marker in config_markers.items():
            config_legend_elements.append(
                Line2D(
                    [0],
                    [0],
                    marker=marker,
                    color="w",
                    markerfacecolor="gray",
                    markersize=10,
                    label=config,
                )
            )

        # Add legends with adjusted font sizes
        legend1 = ax.legend(
            handles=model_legend_elements,
            loc="upper left",
            title="Models",
            fontsize=18,
            title_fontsize=20,
            framealpha=0.9,
            fancybox=True,
            shadow=True,
        )
        ax.add_artist(legend1)

        ax.legend(
            handles=config_legend_elements,
            loc="lower right",
            title="Configurations",
            fontsize=18,
            title_fontsize=20,
            framealpha=0.9,
            fancybox=True,
            shadow=True,
        )

        plt.tight_layout()

        # Save the plot
        filename = "pareto_front_cost_vs_effective_coverage.png"
        plt.savefig(
            output_dir / filename,
            dpi=300,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
        )
        plt.close()

        print(f"\n✅ Pareto Front plot (all combinations) saved: {output_dir / filename}")


def main():
    """Main function to create the Pareto Front analysis."""
    print("🔍 Pareto Front Analysis: Cost vs Effective Coverage")
    print("=" * 70)

    # Initialize analysis tool
    analysis = ParetoFrontAnalysis()

    # Load data from all models
    analysis.load_all_model_data()

    # Create Pareto Front plot
    print("\n" + "=" * 70)
    print("CREATING PARETO FRONT PLOT")
    print("=" * 70)

    # All model-configuration combinations
    analysis.create_pareto_front_plot_all()

    print("\n🎉 Pareto Front analysis complete!")


if __name__ == "__main__":
    main()

