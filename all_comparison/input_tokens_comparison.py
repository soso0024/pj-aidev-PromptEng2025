#!/usr/bin/env python3
"""
Input Tokens Comparison Across All LLMs

Creates a grouped bar chart comparing average input tokens across all models
and configurations, similar to the individual 5_input_tokens.png files.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
from typing import Dict, List, Any

# Add parent directory to path to import analysis modules
sys.path.append(str(Path(__file__).parent.parent))
from analysis.data_loader import DataLoader


class InputTokensComparison:
    """Creates comprehensive input tokens comparison across all models."""

    def __init__(self, base_dir: str = None):
        """Initialize with base directory containing model data."""
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent
        else:
            self.base_dir = Path(base_dir)

        self.data = []

        # Define the models and configurations we expect
        self.expected_models = [
            "claude-3-haiku",
            "claude-3-5-haiku",
            "claude-4-sonnet",
            "claude-opus-4-1",
        ]

        self.expected_configs = ["basic", "ast", "docstring", "docstring_ast"]

        # Define colors for each configuration (colorblind-friendly palette)
        self.config_colors = {
            "basic": "#1f77b4",  # blue
            "ast": "#ff7f0e",  # orange
            "docstring": "#2ca02c",  # green
            "docstring_ast": "#d62728",  # red
        }

    def _format_model_name(self, model_name: str) -> str:
        """Format model name for display."""
        model_display_names = {
            "claude-3-5-haiku": "Claude 3.5 Haiku",
            "claude-opus-4-1": "Claude 4.1 Opus",
            "claude-4-sonnet": "Claude 4 Sonnet",
            "claude-3-haiku": "Claude 3 Haiku",
        }
        return model_display_names.get(model_name, model_name.replace("-", " ").title())

    def _format_config_name(self, config_name: str) -> str:
        """Format configuration name for display."""
        config_display_names = {
            "basic": "Basic",
            "ast": "AST",
            "docstring": "Docstring",
            "docstring_ast": "Docstring + AST",
        }
        return config_display_names.get(config_name, config_name.title())

    def load_all_model_data(self) -> None:
        """Load data from all model directories."""
        print("=" * 80)
        print("LOADING DATA FROM ALL MODELS FOR INPUT TOKENS COMPARISON")
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

    def calculate_input_tokens_metrics(self) -> pd.DataFrame:
        """Calculate input token metrics for all model-configuration combinations."""
        if not self.data:
            print("No data loaded. Call load_all_model_data() first.")
            return pd.DataFrame()

        df = pd.DataFrame(self.data)

        # Filter out 'unknown' models and focus on expected configurations
        df = df[df["model"] != "unknown"]
        df = df[df["config_type"].isin(self.expected_configs)]

        print(f"\nProcessing {len(df)} records for input tokens analysis...")

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

                # Calculate metrics - use total_input_tokens field
                avg_input_tokens = config_data["total_input_tokens"].mean()
                std_input_tokens = config_data["total_input_tokens"].std()
                sample_size = len(config_data)

                results.append(
                    {
                        "Model": self._format_model_name(model),
                        "ModelKey": model,  # Keep original key for sorting
                        "Configuration": self._format_config_name(config),
                        "ConfigKey": config,  # Keep original key for sorting
                        "Average Input Tokens": avg_input_tokens,
                        "Std Input Tokens": std_input_tokens,
                        "Sample Size": sample_size,
                    }
                )

                print(
                    f"  {config}: Avg Input Tokens={avg_input_tokens:.0f}, Samples={sample_size}"
                )

        return pd.DataFrame(results)

    def create_input_tokens_comparison(self, output_dir: Path = None) -> None:
        """Create and save the input tokens comparison chart."""
        if output_dir is None:
            output_dir = Path("all_comparison")

        output_dir.mkdir(exist_ok=True)

        # Calculate metrics
        metrics_df = self.calculate_input_tokens_metrics()

        if metrics_df.empty:
            print("Warning: No data available for input tokens comparison.")
            return

        print("\n" + "=" * 80)
        print("CREATING INPUT TOKENS COMPARISON CHART")
        print("=" * 80)

        # Create the grouped bar chart
        fig, ax = plt.subplots(figsize=(12, 8))

        # Prepare data for grouped bar chart
        models = [self._format_model_name(model) for model in self.expected_models]
        configs = [self._format_config_name(config) for config in self.expected_configs]

        # Set up bar positions
        x = np.arange(len(models))
        width = 0.2
        multiplier = 0

        # Create bars for each configuration
        for config_key in self.expected_configs:
            config_display = self._format_config_name(config_key)
            values = []
            errors = []

            for model_key in self.expected_models:
                model_display = self._format_model_name(model_key)

                # Find data for this model-config combination
                subset = metrics_df[
                    (metrics_df["ModelKey"] == model_key)
                    & (metrics_df["ConfigKey"] == config_key)
                ]

                if not subset.empty:
                    values.append(subset.iloc[0]["Average Input Tokens"])
                    errors.append(
                        subset.iloc[0]["Std Input Tokens"]
                        if pd.notna(subset.iloc[0]["Std Input Tokens"])
                        else 0
                    )
                else:
                    values.append(0)
                    errors.append(0)

            # Create bars for this configuration
            offset = width * multiplier
            bars = ax.bar(
                x + offset,
                values,
                width,
                label=config_display,
                color=self.config_colors[config_key],
                alpha=0.8,
            )

            # Add value labels on bars
            for i, (bar, value) in enumerate(zip(bars, values)):
                if value > 0:
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 100,
                        f"{value:.0f}",
                        ha="center",
                        va="bottom",
                        fontsize=10,
                        fontweight="bold",
                    )

            multiplier += 1

        ax.set_xlabel("LLM Models", fontsize=16, fontweight="bold")
        ax.set_ylabel("Average Input Tokens", fontsize=16, fontweight="bold")
        ax.set_xticks(x + width * 1.5)
        ax.set_xticklabels(models)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.set_ylim(bottom=0)

        # Add legend
        ax.legend(loc="upper right", fontsize=12)

        # Add grid for better readability
        ax.grid(True, alpha=0.3, axis="y")

        plt.tight_layout()

        # Save the chart
        output_path = output_dir / "input_tokens_comparison.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        print(f"✅ Input tokens comparison saved to: {output_path}")

        plt.close()

    def print_summary_statistics(self, df: pd.DataFrame) -> None:
        """Print summary statistics for input tokens."""
        if df.empty:
            return

        print("\n" + "=" * 80)
        print("INPUT TOKENS SUMMARY STATISTICS")
        print("=" * 80)

        # Overall statistics
        total_records = df[df["Sample Size"] > 0]
        if not total_records.empty:
            overall_avg = (
                total_records["Average Input Tokens"] * total_records["Sample Size"]
            ).sum() / total_records["Sample Size"].sum()
            print(f"Overall Average Input Tokens: {overall_avg:.0f}")
            print(f"Total Sample Size: {total_records['Sample Size'].sum():.0f}")

        # Best and worst performing combinations
        if not total_records.empty:
            lowest_tokens = total_records.loc[
                total_records["Average Input Tokens"].idxmin()
            ]
            highest_tokens = total_records.loc[
                total_records["Average Input Tokens"].idxmax()
            ]

            print(
                f"\nLowest Input Tokens: {lowest_tokens['Model']} - {lowest_tokens['Configuration']} ({lowest_tokens['Average Input Tokens']:.0f} tokens)"
            )
            print(
                f"Highest Input Tokens: {highest_tokens['Model']} - {highest_tokens['Configuration']} ({highest_tokens['Average Input Tokens']:.0f} tokens)"
            )


def main():
    """Main function to generate the input tokens comparison."""
    print("📊 Input Tokens Comparison Generator")
    print("=" * 60)

    # Initialize comparison generator
    generator = InputTokensComparison()

    # Load data from all models
    generator.load_all_model_data()

    # Generate input tokens comparison
    generator.create_input_tokens_comparison()

    # Calculate and print summary statistics
    metrics_df = generator.calculate_input_tokens_metrics()
    generator.print_summary_statistics(metrics_df)

    print("\n🎉 Input tokens comparison generation complete!")


if __name__ == "__main__":
    main()
