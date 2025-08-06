#!/usr/bin/env python3
"""
Analysis Module

Modular components for test results analysis and visualization.

This package contains:
- problem_classifier: Dataset classification logic
- data_loader: Data loading and processing
- traditional_plots: Original 7 visualization methods
- dataset_aware_plots: New 5 dataset-aware visualizations  
- analysis_reporter: Statistical analysis and reporting
"""

from .problem_classifier import ProblemClassifier
from .data_loader import DataLoader
from .traditional_plots import TraditionalPlots
from .dataset_aware_plots import DatasetAwarePlots
from .analysis_reporter import AnalysisReporter

__all__ = [
    "ProblemClassifier",
    "DataLoader", 
    "TraditionalPlots",
    "DatasetAwarePlots",
    "AnalysisReporter"
]