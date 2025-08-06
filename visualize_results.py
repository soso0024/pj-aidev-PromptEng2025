#!/usr/bin/env python3
"""
Test Results Visualization Tool (Refactored)

Analyzes generated test results from stats.json files and creates visualizations
comparing different configurations (basic, docstring, AST, both).

This is a refactored version with modular architecture for better maintainability:
- problem_classifier.py: Dataset classification logic
- data_loader.py: Data loading and processing
- traditional_plots.py: Original 7 visualization methods
- dataset_aware_plots.py: New 5 dataset-aware visualizations
- analysis_reporter.py: Statistical analysis and reporting
"""

import os
from pathlib import Path
from typing import Dict, List, Any

# Import our modular components from analysis folder
from analysis.data_loader import DataLoader
from analysis.traditional_plots import TraditionalPlots
from analysis.dataset_aware_plots import DatasetAwarePlots
from analysis.analysis_reporter import AnalysisReporter


class TestResultsAnalyzer:
    """Main orchestrator class for test results analysis and visualization."""

    def __init__(
        self,
        results_dir: str = "generated_tests",
        dataset_path: str = "dataset/HumanEval.jsonl",
    ):
        """Initialize the analyzer with the results directory."""
        self.results_dir = Path(results_dir)
        self.dataset_path = dataset_path

        # Define the desired order for configuration types
        self.config_order = ["basic", "ast", "docstring", "docstring_ast"]

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

        # Initialize components
        self.data_loader = DataLoader(results_dir, dataset_path)
        self.data = []

        # Plotting and reporting components (initialized after data loading)
        self.traditional_plots = None
        self.dataset_aware_plots = None
        self.reporter = None

    def load_data(self) -> None:
        """Load all data using the DataLoader component."""
        print("=" * 80)
        print("LOADING TEST RESULTS DATA")
        print("=" * 80)

        self.data = self.data_loader.load_data()

        # Initialize plotting and reporting components with loaded data
        if self.data:
            self.traditional_plots = TraditionalPlots(self.data, self.config_order)
            self.dataset_aware_plots = DatasetAwarePlots(
                self.data, self.config_order, self.algorithm_type_order
            )
            self.reporter = AnalysisReporter(self.data, self.config_order)
        else:
            print(
                "Warning: No data loaded. Plotting and reporting will not be available."
            )

    def create_visualizations(self, output_dir: str = "visualizations") -> None:
        """Create all visualization plots."""
        if not self.data:
            print("No data loaded. Call load_data() first.")
            return

        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        print("\n" + "=" * 80)
        print("CREATING VISUALIZATIONS")
        print("=" * 80)
        print(f"Output directory: {output_path}")

        # Create traditional plots (charts 1-7)
        if self.traditional_plots:
            self.traditional_plots.create_all_plots(output_path)

        # Create dataset-aware plots (charts 8-12)
        if self.dataset_aware_plots:
            self.dataset_aware_plots.create_all_plots(output_path)

        print(f"\n✅ All visualizations saved to '{output_path}/' directory")
        print(f"Created 12 visualization charts (1-12)")

    def print_summary_stats(self) -> None:
        """Print comprehensive analysis reports."""
        if not self.data:
            print("No data loaded. Call load_data() first.")
            return

        if self.reporter:
            self.reporter.generate_all_reports()
        else:
            print("Reporter not initialized. Cannot generate reports.")

    def print_dataset_analysis(self) -> None:
        """Print dataset-aware analysis (included in summary_stats)."""
        if self.reporter:
            self.reporter.print_dataset_analysis()
        else:
            print("Reporter not initialized or no data loaded.")

    def get_data_summary(self) -> Dict[str, Any]:
        """Get summary information about loaded data."""
        if not self.data:
            return {
                "total_records": 0,
                "configurations": [],
                "message": "No data loaded",
            }

        config_counts = {}
        for record in self.data:
            config = record.get("config_type", "unknown")
            config_counts[config] = config_counts.get(config, 0) + 1

        return {
            "total_records": len(self.data),
            "configurations": config_counts,
            "has_dataset_classification": any(
                "complexity_level" in record for record in self.data
            ),
            "has_algorithm_types": any(
                "algorithm_type" in record for record in self.data
            ),
        }


def main():
    """Main entry point for the visualization tool."""
    print("🔍 Test Results Visualization Tool (Refactored)")
    print("=" * 50)

    # Initialize analyzer
    analyzer = TestResultsAnalyzer()

    # Load data
    analyzer.load_data()

    # Print data summary
    summary = analyzer.get_data_summary()
    print(f"\n📊 Data Summary:")
    print(f"  Total records: {summary['total_records']}")
    print(f"  Configurations: {summary['configurations']}")
    print(
        f"  Dataset classification: {'✅' if summary['has_dataset_classification'] else '❌'}"
    )
    print(f"  Algorithm types: {'✅' if summary['has_algorithm_types'] else '❌'}")

    if summary["total_records"] == 0:
        print(
            "\n❌ No data found. Make sure you have .stats.json files in the generated_tests/ directory."
        )
        return

    # Create visualizations
    analyzer.create_visualizations()

    # Print analysis reports
    analyzer.print_summary_stats()

    print(f"\n🎉 Analysis complete! Check the 'visualizations/' directory for graphs.")


if __name__ == "__main__":
    main()
