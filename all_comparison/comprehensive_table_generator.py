#!/usr/bin/env python3
"""
Comprehensive Model-Configuration Table Generator

Creates a detailed summary table showing metrics for all combinations of
models and configurations as requested in the requirements.

Usage:
    python comprehensive_table_generator.py
"""

import sys
import json
import csv
from pathlib import Path
from typing import Dict, List, Any, Tuple
import pandas as pd
import numpy as np

# Add parent directory to path to import analysis modules
sys.path.append(str(Path(__file__).parent.parent))
from analysis.data_loader import DataLoader
from analysis.problem_classifier import ProblemClassifier


class ComprehensiveTableGenerator:
    """Creates comprehensive summary tables of all model-configuration combinations."""

    def __init__(self, base_dir: str = None):
        """Initialize with base directory containing model data."""
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent
        else:
            self.base_dir = Path(base_dir)

        self.data = []

        # Define the models and configurations we expect
        self.expected_models = [
            "claude-3-5-haiku",
            "claude-3-haiku",
            "claude-4-sonnet",
            "claude-4-5-sonnet",
            "claude-opus-4-1",
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
            "basic": "Basic",
            "ast": "AST",
            "docstring": "Docstring",
            "docstring_ast": "Docstring + AST",
        }
        return config_display_names.get(config_name, config_name.title())

    def load_all_model_data(self) -> None:
        """Load data from all model directories."""
        print("=" * 80)
        print("LOADING DATA FROM ALL MODELS FOR COMPREHENSIVE TABLE")
        print("=" * 80)

        # Find all model-specific directories in the data folder
        data_dir = self.base_dir / "data"
        model_dirs = []
        for path in data_dir.glob("generated_tests_*"):
            if path.is_dir():
                model_dirs.append(path)

        if not model_dirs:
            print(f"No model directories found (generated_tests_*) in {data_dir}")
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
        configs = set()
        for record in self.data:
            model = record.get("model", "unknown")
            config = record.get("config_type", "unknown")
            if model != "unknown":
                models.add(model)
            if config != "unknown":
                configs.add(config)

        print(f"Models found: {sorted(models)}")
        print(f"Configurations found: {sorted(configs)}")

    def calculate_comprehensive_metrics(self) -> pd.DataFrame:
        """
        Calculate comprehensive metrics for all model-configuration combinations.

        Returns DataFrame with columns:
        - Model, Configuration, Average Cost (USD), Average Code Coverage (%),
          Success Rate (%), Average Fix Attempts, Sample Size
        """
        if not self.data:
            print("No data loaded. Call load_all_model_data() first.")
            return pd.DataFrame()

        df = pd.DataFrame(self.data)

        # Filter out 'unknown' models and focus on expected configurations
        df = df[df["model"] != "unknown"]
        df = df[df["config_type"].isin(self.expected_configs)]

        print(f"\nProcessing {len(df)} records for comprehensive analysis...")

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
                    # Add empty row for missing combinations
                    results.append(
                        {
                            "Model": self._format_model_name(model),
                            "Configuration": self._format_config_name(config),
                            "Average Cost (USD)": 0.0,
                            "Average Code Coverage (%)": 0.0,
                            "Success Rate (%)": 0.0,
                            "Average Fix Attempts": 0.0,
                            "Sample Size": 0,
                        }
                    )
                    print(f"  {config}: No data available")
                    continue

                # Calculate metrics
                avg_cost = config_data["total_cost_usd"].mean()
                avg_coverage = config_data["code_coverage_percent"].mean()
                success_rate = config_data["success"].mean() * 100

                # Handle fix attempts - use fix_attempts_used field from stats
                if "fix_attempts_used" in config_data.columns:
                    avg_fix_attempts = config_data["fix_attempts_used"].mean()
                else:
                    # If fix_attempts_used is not available, check for legacy field names
                    if "fix_attempts" in config_data.columns:
                        avg_fix_attempts = config_data["fix_attempts"].mean()
                    else:
                        # Fallback: try to infer from available data or use 0 as default
                        print(
                            f"    Warning: No fix attempts data found for {model} - {config}"
                        )
                        avg_fix_attempts = 0.0

                sample_size = len(config_data)

                results.append(
                    {
                        "Model": self._format_model_name(model),
                        "Configuration": self._format_config_name(config),
                        "Average Cost (USD)": avg_cost,
                        "Average Code Coverage (%)": avg_coverage,
                        "Success Rate (%)": success_rate,
                        "Average Fix Attempts": avg_fix_attempts,
                        "Sample Size": sample_size,
                    }
                )

                print(
                    f"  {config}: Cost=${avg_cost:.4f}, Coverage={avg_coverage:.1f}%, Success={success_rate:.1f}%, Fix Attempts={avg_fix_attempts:.2f}, Samples={sample_size}"
                )

        return pd.DataFrame(results)

    def generate_comprehensive_table(self, output_dir: Path = None) -> None:
        """Generate and display the comprehensive summary table."""
        if output_dir is None:
            output_dir = Path("all_comparison")

        output_dir.mkdir(exist_ok=True)

        # Calculate metrics
        metrics_df = self.calculate_comprehensive_metrics()

        if metrics_df.empty:
            print("Warning: No data available for comprehensive table.")
            return

        print("\n" + "=" * 120)
        print("COMPREHENSIVE MODEL-CONFIGURATION SUMMARY TABLE (Table 1)")
        print("=" * 120)

        # Create a formatted table for display
        self._display_formatted_table(metrics_df)

        # Save to CSV
        csv_path = output_dir / "comprehensive_summary_table.csv"
        metrics_df.to_csv(csv_path, index=False, float_format="%.4f")
        print(f"\n✅ Table saved to CSV: {csv_path}")

        # Save formatted table to text file
        txt_path = output_dir / "comprehensive_summary_table.txt"
        with open(txt_path, "w") as f:
            f.write("COMPREHENSIVE MODEL-CONFIGURATION SUMMARY TABLE (Table 1)\n")
            f.write("=" * 120 + "\n\n")
            f.write(self._format_table_for_text(metrics_df))
        print(f"✅ Formatted table saved to: {txt_path}")

    def _display_formatted_table(self, df: pd.DataFrame) -> None:
        """Display a nicely formatted table in the console."""
        if df.empty:
            print("No data to display.")
            return

        # Print header
        print(
            f"{'Model':<20} {'Configuration':<15} {'Avg Cost (USD)':<15} {'Avg Coverage (%)':<17} {'Success Rate (%)':<17} {'Avg Fix Attempts':<17} {'Sample Size':<12}"
        )
        print("-" * 120)

        # Group by model for better readability
        for model in self.expected_models:
            model_display = self._format_model_name(model)
            model_data = df[df["Model"] == model_display]

            if model_data.empty:
                continue

            for _, row in model_data.iterrows():
                print(
                    f"{row['Model']:<20} {row['Configuration']:<15} ${row['Average Cost (USD)']:<14.4f} {row['Average Code Coverage (%)']:<16.1f} {row['Success Rate (%)']:<16.1f} {row['Average Fix Attempts']:<16.2f} {row['Sample Size']:<12.0f}"
                )

            print()  # Add spacing between models

    def _format_table_for_text(self, df: pd.DataFrame) -> str:
        """Format table for text file output."""
        if df.empty:
            return "No data to display."

        lines = []

        # Header
        lines.append(
            f"{'Model':<20} {'Configuration':<15} {'Avg Cost (USD)':<15} {'Avg Coverage (%)':<17} {'Success Rate (%)':<17} {'Avg Fix Attempts':<17} {'Sample Size':<12}"
        )
        lines.append("-" * 120)

        # Data rows grouped by model
        for model in self.expected_models:
            model_display = self._format_model_name(model)
            model_data = df[df["Model"] == model_display]

            if model_data.empty:
                continue

            for _, row in model_data.iterrows():
                lines.append(
                    f"{row['Model']:<20} {row['Configuration']:<15} ${row['Average Cost (USD)']:<14.4f} {row['Average Code Coverage (%)']:<16.1f} {row['Success Rate (%)']:<16.1f} {row['Average Fix Attempts']:<16.2f} {row['Sample Size']:<12.0f}"
                )

            lines.append("")  # Add spacing between models

        return "\n".join(lines)

    def generate_summary_statistics(self, df: pd.DataFrame) -> None:
        """Generate and display summary statistics."""
        if df.empty:
            return

        print("\n" + "=" * 80)
        print("SUMMARY STATISTICS")
        print("=" * 80)

        # Overall averages
        total_records = df[df["Sample Size"] > 0]
        if not total_records.empty:
            weighted_avg_cost = (
                total_records["Average Cost (USD)"] * total_records["Sample Size"]
            ).sum() / total_records["Sample Size"].sum()
            weighted_avg_coverage = (
                total_records["Average Code Coverage (%)"]
                * total_records["Sample Size"]
            ).sum() / total_records["Sample Size"].sum()
            weighted_avg_success = (
                total_records["Success Rate (%)"] * total_records["Sample Size"]
            ).sum() / total_records["Sample Size"].sum()

            print(f"Weighted Overall Averages:")
            print(f"  Average Cost: ${weighted_avg_cost:.4f}")
            print(f"  Average Coverage: {weighted_avg_coverage:.1f}%")
            print(f"  Average Success Rate: {weighted_avg_success:.1f}%")
            print(f"  Total Sample Size: {total_records['Sample Size'].sum():.0f}")

        # Best performing combinations
        print(f"\nBest Performing Combinations:")
        if not total_records.empty:
            best_coverage = total_records.loc[
                total_records["Average Code Coverage (%)"].idxmax()
            ]
            best_success = total_records.loc[total_records["Success Rate (%)"].idxmax()]
            lowest_cost = total_records.loc[
                total_records["Average Cost (USD)"].idxmin()
            ]

            print(
                f"  Highest Coverage: {best_coverage['Model']} - {best_coverage['Configuration']} ({best_coverage['Average Code Coverage (%)']:.1f}%)"
            )
            print(
                f"  Highest Success Rate: {best_success['Model']} - {best_success['Configuration']} ({best_success['Success Rate (%)']:.1f}%)"
            )
            print(
                f"  Lowest Cost: {lowest_cost['Model']} - {lowest_cost['Configuration']} (${lowest_cost['Average Cost (USD)']:.4f})"
            )


def main():
    """Main function to generate the comprehensive table."""
    print("📊 Comprehensive Model-Configuration Table Generator")
    print("=" * 60)

    # Initialize table generator
    generator = ComprehensiveTableGenerator()

    # Load data from all models
    generator.load_all_model_data()

    # Generate comprehensive table
    generator.generate_comprehensive_table()

    # Calculate and generate the table
    metrics_df = generator.calculate_comprehensive_metrics()
    generator.generate_summary_statistics(metrics_df)

    print("\n🎉 Comprehensive table generation complete!")


if __name__ == "__main__":
    main()
