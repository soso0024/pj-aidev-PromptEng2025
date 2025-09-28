# HumanEval Test Case Generator

A Python tool that automatically generates comprehensive pytest test cases for HumanEval problems using multiple LLM providers (Claude, Ollama). The generated test cases include automatic evaluation, error fixing, and comprehensive analysis.

## Features

- **Multi-model support**: Claude (Sonnet, Haiku) and Ollama models
- **Automatic test evaluation**: Runs pytest and fixes errors using LLM feedback
- **Batch processing**: Generate tests for multiple problems at once
- **Comprehensive analysis**: Visualizations and statistics for different configurations
- **AST-based error fixing**: Enhanced error fixing with code structure analysis
- **Cost tracking**: Token usage and API cost monitoring
- **Code coverage analysis**: Tracks test coverage percentages

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys (see Configuration)

## Configuration

### API Key Setup

Choose one method:

**Environment Variable:**

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**.env File (Recommended):**

```
ANTHROPIC_API_KEY=your-api-key-here
```

**Command Line:**

```bash
python run_test_case_generator.py --api-key "your-api-key-here"
```

### Model Configuration

Models are configured in `models_config.json`. Available models:

- **Claude**: `claude-4-sonnet`, `claude-3-5-haiku`, `claude-3-haiku`
- **Ollama**: `ollama-gpt-oss` (local, free)

## Usage

### Basic Usage

```bash
# Generate test for random problem
python run_test_case_generator.py

# Generate test for specific problem
python run_test_case_generator.py --task-id "HumanEval/0"

# Use specific model
python run_test_case_generator.py --models claude-4-sonnet

# Include docstring for more context
python run_test_case_generator.py --include-docstring

# Include AST representation
python run_test_case_generator.py --include-ast

# Enable AST-based error fixing
python run_test_case_generator.py --ast-fix
```

### Command Line Options

| Option                 | Description                       | Default                   |
| ---------------------- | --------------------------------- | ------------------------- |
| `--dataset`            | Path to HumanEval dataset         | `dataset/HumanEval.jsonl` |
| `--output-dir`         | Output directory                  | `generated_tests`         |
| `--task-id`            | Specific task ID                  | Random selection          |
| `--models`             | Model(s) to use                   | `ollama-gpt-oss`          |
| `--include-docstring`  | Include function docstring        | `False`                   |
| `--include-ast`        | Include AST representation        | `False`                   |
| `--show-prompt`        | Display prompt preview            | `True`                    |
| `--disable-evaluation` | Skip automatic evaluation         | `False`                   |
| `--max-pytest-runs`    | Max pytest runs (initial + fixes) | `3`                       |
| `--quiet-evaluation`   | Less verbose output               | `False`                   |
| `--ast-fix`            | Enable AST-based error fixing     | `False`                   |

### Batch Processing

For generating tests for multiple problems:

```bash
cd batch

# Generate for range
python run_batch_test_case_generator.py --start 0 --end 10

# Generate for specific problems
python run_batch_test_case_generator.py --task-ids "HumanEval/0,HumanEval/5,HumanEval/10"

# Use multiple models
python run_batch_test_case_generator.py --start 0 --end 5 --models claude-4-sonnet claude-3-5-haiku

# Include full context
python run_batch_test_case_generator.py --start 0 --end 10 --include-docstring --include-ast
```

### Analysis and Visualization

Generate comprehensive analysis of test results:

```bash
python run_analysis.py
```

This creates visualizations in model-specific folders (e.g., `claude-4-sonnet_viz/`) showing:

- Success rates by configuration
- Code coverage analysis
- Cost analysis
- Problem difficulty heatmaps
- Algorithm type performance
- And more...

## Output Structure

### Generated Files

Each test generation creates:

- **Test file**: `test_humaneval_X_[config]_[status].py`
- **Statistics file**: `test_humaneval_X_[config]_[status].stats.json`

### Filename Conventions

- `test_humaneval_0_success.py` - Tests passed
- `test_humaneval_0_false.py` - Tests failed
- `test_humaneval_0_docstring_ast_success.py` - Multiple options, passed

### Project Structure

```
project/
├── analysis/                    # Analysis modules
│   ├── data_loader.py
│   ├── problem_classifier.py
│   ├── traditional_plots.py
│   ├── dataset_aware_plots.py
│   └── analysis_reporter.py
├── batch/                       # Batch processing
│   ├── run_batch_test_case_generator.py
│   └── README.md
├── dataset/
│   ├── HumanEval.jsonl         # Main dataset
│   ├── HumanEval_formatted.json
│   └── HumanEval_formatted.yaml
├── generated_tests/             # Generated test files
├── [model]_viz/                # Visualization outputs
├── run_test_case_generator.py   # Main script
├── run_analysis.py             # Analysis script
├── models_config.json          # Model configuration
└── requirements.txt
```

## Configuration Options Comparison

| Configuration | Cost    | Quality  | Use Case                       |
| ------------- | ------- | -------- | ------------------------------ |
| Basic         | Lowest  | Variable | Simple problems                |
| + Docstring   | Medium  | Better   | Complex problems with examples |
| + AST         | Higher  | Good     | Structure-heavy algorithms     |
| + Both        | Highest | Best     | Most challenging problems      |

## Running Generated Tests

```bash
cd generated_tests

# Run specific test
pytest test_humaneval_0.py -v --cov

# Run all tests
pytest -v --cov

# HTML coverage report
pytest --cov --cov-report=html
```

## Statistics File Format

Each `.stats.json` contains:

```json
{
  "total_input_tokens": 3876,
  "total_output_tokens": 2038,
  "total_cost_usd": 0.042198,
  "task_id": "HumanEval/4",
  "evaluation_success": true,
  "fix_attempts_used": 2,
  "code_coverage_percent": 85.7
}
```

## Troubleshooting

**Common Issues:**

1. **API key not found**: Set your API key using one of the configuration methods
2. **Import errors**: Run pytest from the `generated_tests` directory
3. **EOF when reading a line**: Use `--no-show-prompt` for non-interactive environments
4. **Evaluation fails**: Check pytest installation or use `--disable-evaluation`

**Getting Help:**

```bash
python run_test_case_generator.py --help
python batch/run_batch_test_case_generator.py --help
```

## Cost Optimization

- **Basic generation**: ~$0.01-0.05 per problem
- **With evaluation**: ~$0.02-0.08 per problem (includes fix attempts)
- **Use Ollama models for free local processing**
- **Start with basic configuration, add options for difficult problems**

## Requirements

- Python 3.8+
- anthropic >= 0.7.0
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- python-dotenv >= 1.0.0
- pandas, matplotlib, seaborn, numpy (for visualization)

## License

This project is for educational and research purposes.
