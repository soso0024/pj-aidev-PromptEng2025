# HumanEval Test Case Generator

A Python tool that automatically generates comprehensive pytest test cases for HumanEval problems using Claude API. The generated test cases can be used for code coverage analysis and testing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
  - [API Key Setup](#api-key-setup)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Batch Generation](#batch-generation)
  - [Command Line Options](#command-line-options)
  - [Examples](#examples)
  - [Evaluation and Error Fixing](#evaluation-and-error-fixing)
  - [AST-Based Error Fixing](#ast-based-error-fixing)
- [Output](#output)
  - [Generated Files](#generated-files)
  - [Filename Conventions](#filename-conventions)
  - [Example Output Structure](#example-output-structure)
  - [Console Output Example](#console-output-example)
- [Running Generated Tests](#running-generated-tests)
  - [Common pytest Options](#common-pytest-options)
  - [Coverage Options](#coverage-options)
  - [Example Usage](#example-usage)
- [Cost Optimization](#cost-optimization)
  - [Token Usage Control](#token-usage-control)
  - [Interactive Prompt Preview](#interactive-prompt-preview)
  - [Pricing Information](#pricing-information)
- [File Structure](#file-structure)
- [Statistics File Format](#statistics-file-format)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Getting Help](#getting-help)
- [Advanced Usage Tips](#advanced-usage-tips)
  - [Batch Generation with Different Options](#batch-generation-with-different-options)
  - [Cost-Effective Workflow](#cost-effective-workflow)
  - [Quality Comparison](#quality-comparison)
- [Dataset Analysis and Classification](#dataset-analysis-and-classification)
  - [Problem Classification Methodology](#problem-classification-methodology)
  - [Dataset Distribution Analysis](#dataset-distribution-analysis)
  - [Configuration Effectiveness by Problem Type](#configuration-effectiveness-by-problem-type)
  - [Practical Applications](#practical-applications)
- [Results Visualization](#results-visualization)
  - [Overview](#overview)
  - [Usage](#usage-1)
  - [Output](#output-1)
  - [Generated Visualizations](#generated-visualizations)
  - [Example Console Output](#example-console-output)
  - [Data Analysis Features](#data-analysis-features)
  - [Interpretation Guide](#interpretation-guide)
- [Requirements](#requirements)
- [License](#license)

## Features

- **Random or specific problem selection** from HumanEval dataset
- **Pytest-compatible test cases** ready for coverage analysis
- **Token usage and cost tracking** for API calls
- **Configurable docstring inclusion** to control token usage
- **AST representation inclusion** for enhanced code understanding
- **Interactive prompt preview** with cost estimation and confirmation
- **Automatic test evaluation** with pytest execution and error detection
- **Intelligent error fixing** using LLM feedback loop with white box testing
- **Transparent debugging** with detailed error analysis and fix tracking
- **Complete cost tracking** including all evaluation and fix attempts
- **Comprehensive statistics** saved alongside test files
- **Automatic file naming** with success/failure status based on test results
- **Code coverage tracking** with percentage calculation in statistics
- **Clean Python output** without markdown or explanations

## Installation

1. **Clone or download** the repository
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API key** (see Configuration section)

## Configuration

### API Key Setup

Choose one of these methods:

#### Method 1: Environment Variable

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

#### Method 2: .env File (Recommended)

1. Edit the `.env` file:
   ```bash
   ANTHROPIC_API_KEY=your-api-key-here
   ```

#### Method 3: Command Line

```bash
python run_test_case_generator.py --api-key "your-api-key-here"
```

```bash
# AST-focused error fixing mode (adds relevant AST snippet)
python run_test_case_generator.py --ast-fix
```

## Usage

### Basic Usage

Generate test cases for a random problem:

```bash
python run_test_case_generator.py
```

### Batch Generation

For generating test cases for multiple HumanEval problems automatically, use the batch generator in the `batch/` folder:

```bash
# See batch/readme.md for detailed usage
cd batch
python run_batch_test_case_generator.py --start 0 --end 10
```

### Command Line Options

| Option                 | Description                                                                                                  | Default                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| `--dataset`            | Path to HumanEval dataset file                                                                               | `dataset/HumanEval.jsonl`    |
| `--output-dir`         | Output directory for test files                                                                              | `generated_tests`            |
| `--task-id`            | Specific task ID to generate tests for                                                                       | Random selection             |
| `--api-key`            | Claude API key                                                                                               | From .env or environment     |
| `--include-docstring`  | Include function docstring in prompt                                                                         | `False` (signature only)     |
| `--include-ast`        | Include AST of canonical solution in prompt                                                                  | `False`                      |
| `--show-prompt`        | Display prompt before sending to LLM and ask for confirmation (use `--no-show-prompt` to disable)            | `True`                       |
| `--disable-evaluation` | Disable automatic test evaluation and error fixing                                                           | `False` (evaluation enabled) |
| `--max-pytest-runs`    | Total pytest runs (initial + fixes)                                                                          | `3`                          |
| `--quiet-evaluation`   | Disable verbose output during error fixing process                                                           | `False` (verbose enabled)    |
| `--ast-fix`            | Enable AST-focused error fixing - adds relevant AST nodes to fix prompts for better structural understanding | `False`                      |

### Examples

#### Generate test for a random problem:

```bash
python run_test_case_generator.py
```

#### Generate test for a specific problem:

```bash
python run_test_case_generator.py --task-id "HumanEval/0"
```

#### Include docstring for more context (uses more tokens):

```bash
python run_test_case_generator.py --include-docstring
```

#### Include AST representation for enhanced understanding:

```bash
python run_test_case_generator.py --include-ast
```

#### Enable AST-focused error fixing (uses relevant AST snippet during retries):

```bash
python run_test_case_generator.py --ast-fix
```

#### Disable prompt preview for automation:

```bash
python run_test_case_generator.py --no-show-prompt
```

#### Use custom dataset and output directory:

```bash
python run_test_case_generator.py --dataset path/to/custom.jsonl --output-dir my_tests
```

#### Combine options:

```bash
python run_test_case_generator.py --task-id "HumanEval/5" --include-docstring --include-ast --no-show-prompt --output-dir custom_tests
```

#### Combine with AST-focused error fixing:

```bash
python run_test_case_generator.py --task-id "HumanEval/5" --include-ast --ast-fix
```

### Evaluation and Error Fixing

The tool automatically evaluates generated test cases and fixes errors using an intelligent feedback loop:

#### Generate with automatic evaluation (default):

```bash
python run_test_case_generator.py --task-id "HumanEval/0"
```

This will:

1. Generate initial test cases
2. Run `pytest test_humaneval_0.py --cov -v` automatically
3. If tests fail, analyze errors and send them to LLM for fixing
4. Repeat up to the configured maximum attempts until tests pass
5. Show transparent debugging information throughout

Fix attempt semantics (important):

- The CLI option `--max-pytest-runs N` controls total pytest runs N.
- The number of LLM fix attempts is `N - 1` (since the first run is the initial, unfixed attempt).
- For example, with `--max-pytest-runs 3`, there are 2 fix attempts: Fix attempt 1 of 2, Fix attempt 2 of 2.
- The UI and prompts now explicitly display “Fix attempt X of Y”.

#### Control evaluation behavior:

```bash
# Disable evaluation (original behavior)
python run_test_case_generator.py --task-id "HumanEval/0" --disable-evaluation

# Set total pytest runs (initial + fixes)
python run_test_case_generator.py --task-id "HumanEval/0" --max-pytest-runs 5

# Quiet mode (less verbose output during fixing)
python run_test_case_generator.py --task-id "HumanEval/0" --quiet-evaluation

# Non-interactive mode (skip confirmations)
python run_test_case_generator.py --task-id "HumanEval/0" --no-show-prompt
```

#### White Box Error Fixing

When evaluation is enabled (default), you'll see transparent debugging:

```
🧪 Evaluating test file: test_humaneval_0.py
❌ Tests failed on attempt 1

================================================================================
📋 PYTEST ERROR DETAILS - Attempt 1
================================================================================
✅ test_function_valid_inputs[case1] PASSED
❌ test_function_valid_inputs[case2] FAILED
🔍 FAILURE DETAILS:
AssertionError: assert [1, 2] == [1]
================================================================================

🔧 Attempting to fix errors...

================================================================================
🤖 LLM FIX PROMPT - Attempt 1
================================================================================
[Complete fix prompt with function implementation and error details shown]
================================================================================

🤖 Sending fix request to LLM (attempt 1)...
💰 Fix attempt 1 cost: $0.022434 (Input: 4043, Output: 687)

================================================================================
🔧 LLM FIX RESPONSE - Attempt 1
================================================================================
[LLM's corrected test code shown]
================================================================================

📝 Updated test file with fixes
✅ Tests passed on attempt 2 (Coverage: 85.7%)
📝 Renamed test_humaneval_0.py → test_humaneval_0_success.py
🎉 Test generation and evaluation completed successfully!
```

### AST-Based Error Fixing

The `--ast-fix` option enables intelligent error fixing by analyzing the Abstract Syntax Tree (AST) of the function and identifying nodes most relevant to the error. This provides the LLM with focused context about the problematic code structure.

#### How AST-Based Error Fixing Works

When a test fails and `--ast-fix` is enabled:

1. **Error Analysis**: The system parses the error output to identify error types and affected code lines
2. **AST Parsing**: The canonical solution is parsed into an AST representation
3. **Relevant Node Selection**: A sophisticated algorithm identifies AST nodes most likely related to the error
4. **Context Generation**: The relevant AST nodes are included in the fix prompt to help the LLM understand the code structure

#### Node Selection Algorithm

The AST snippet generator uses multiple heuristics to identify relevant nodes:

**Error-Specific Pattern Matching**:

- **ZeroDivisionError**: Focuses on `BinOp` nodes with division operators (`Div`, `Mod`, `FloorDiv`)
- **IndexError**: Targets `Subscript` nodes (list/string indexing operations)
- **KeyError**: Also targets `Subscript` nodes (dictionary key access)
- **AttributeError**: Identifies `Attribute` nodes (object attribute access)
- **TypeError (operators)**: Focuses on `BinOp` nodes when "operand" is mentioned
- **TypeError (calls)**: Targets `Call` nodes when function arguments are involved
- **ValueError**: Looks for `Raise` and `Call` nodes
- **RecursionError**: Identifies recursive `Call` nodes matching the function name
- **NameError**: Focuses on `Name` nodes (variable references)
- **ImportError**: Targets `Import` and `ImportFrom` nodes

**Line-Based Matching**:

- Extracts code lines from error output
- Finds AST nodes whose line ranges overlap with error lines
- Helps locate the exact error location in complex functions

**Priority Scoring System**:

- Nodes matching error patterns: +10 points (highest priority)
- Nodes overlapping with error lines: +5 points
- Common error-prone operations (`Call`, `BinOp`, `Subscript`, `Attribute`): +2 points
- Nodes are sorted by score and top 15 most relevant are selected

#### Example AST Output

For a ZeroDivisionError in `return a / b`:

```
Line 2: BinOp (Div)
BinOp(
  left=Name(id='a', ctx=Load()),
  op=Div(),
  right=Name(id='b', ctx=Load())
)
```

This focused AST snippet helps the LLM understand:

- The exact operation causing the error (division)
- The operands involved (`a` and `b`)
- The code structure around the error

#### Benefits of AST-Based Fixing

1. **Focused Context**: Instead of sending the entire AST, only relevant nodes are included
2. **Better Error Understanding**: The LLM sees the exact code structure causing issues
3. **Improved Fix Quality**: Structural understanding leads to more accurate fixes
4. **Efficient Token Usage**: Only essential AST information is sent

#### How AST Information is Provided to the LLM

When `--ast-fix` is enabled and a test fails, the system enhances the fix prompt sent to the LLM:

1. **Standard Fix Prompt Components**:

   - The original function being tested (white box approach)
   - The current test code with errors
   - The pytest error output
   - Clear instructions to fix the code

2. **Additional AST Context** (when `--ast-fix` is enabled):
   - A focused AST snippet is inserted between the function and test code
   - Only AST nodes relevant to the error are included
   - The AST is presented in a readable format with line numbers

**Example Fix Prompt Structure**:

```
FUNCTION BEING TESTED:
def divide(a, b):
    return a / b

RELEVANT AST SNIPPET OF FUNCTION (focus on error):
Line 2: BinOp (Div)
BinOp(
  left=Name(id='a', ctx=Load()),
  op=Div(),
  right=Name(id='b', ctx=Load())
)

CURRENT TEST CODE WITH ERRORS:
[test code here]

PYTEST ERROR OUTPUT:
ZeroDivisionError: division by zero

This is fix attempt 1 of 2.
```

The LLM receives this enhanced context and can better understand:

- The structure of the code that's causing the error
- The specific operation types involved (e.g., division, indexing)
- The relationship between variables and operations
- The exact location and nature of the problem

This structural information helps the LLM generate more accurate fixes by understanding not just the error message, but the underlying code patterns that need to be addressed in the test cases.

#### Comparison: Regular vs AST-Based Error Fixing

**Without `--ast-fix`** (Regular fixing):

- LLM sees: function code + test code + error message
- Must infer the problem from error text alone
- May miss structural issues or edge cases

**With `--ast-fix`** (AST-enhanced fixing):

- LLM sees: function code + **relevant AST nodes** + test code + error message
- Gets explicit structural information about error-prone operations
- Can identify patterns like division operations, list indexing, attribute access
- Better understanding leads to more comprehensive test fixes

For example, with a `ZeroDivisionError`:

- Regular: LLM sees "division by zero" error
- AST-enhanced: LLM also sees the `BinOp(op=Div())` node, understanding it's specifically a division operation between variables `a` and `b`

#### Usage Example

```bash
# Enable AST-focused error fixing
python run_test_case_generator.py --task-id "HumanEval/0" --ast-fix

# Combine with AST in initial generation for maximum effectiveness
python run_test_case_generator.py --task-id "HumanEval/0" --include-ast --ast-fix
```

#### When to Use `--ast-fix`

Consider enabling `--ast-fix` when:

- Working with complex algorithms that have multiple error-prone operations
- Dealing with functions that handle edge cases (division by zero, empty lists, null checks)
- Test generation fails repeatedly with type errors or runtime exceptions
- You want more thorough test coverage of error conditions

The option is particularly effective for problems involving:

- Mathematical operations (division, modulo)
- List/array operations (indexing, slicing)
- Dictionary operations (key access)
- Object attribute access
- Recursive functions

## Output

### Generated Files

For each test generation, the tool creates:

1. **Test file**: `test_humaneval_X.py` (or `test_humaneval_X_docstring.py`, `test_humaneval_X_ast.py`, `test_humaneval_X_docstring_ast.py`)

   - Contains the original function implementation
   - Comprehensive pytest test cases
   - Ready to run with pytest

2. **Statistics file**: `test_humaneval_X.stats.json`
   - Token usage information
   - API costs
   - Generation metadata

### Filename Conventions

The tool automatically adjusts filenames based on options used and evaluation results:

- Default: `test_humaneval_0.py` → `test_humaneval_0_success.py` (if tests pass)
- With docstring: `test_humaneval_0_docstring.py` → `test_humaneval_0_docstring_false.py` (if tests fail)
- With AST: `test_humaneval_0_ast.py` → `test_humaneval_0_ast_success.py` (if tests pass)
- With AST-focused fixing: `test_humaneval_0_ast-fix.py` → `test_humaneval_0_ast-fix_success.py` (if tests pass)
- With both: `test_humaneval_0_docstring_ast.py` → `test_humaneval_0_docstring_ast_success.py` (if tests pass)

**Automatic Status Suffixes:**

- `_success`: Tests passed during evaluation
- `_false`: Tests failed during evaluation (even after fix attempts)

Note: When multiple options are combined, the filename includes all active tags, e.g. `test_humaneval_5_docstring_ast_ast-fix.py`.

### Example Output Structure

```
generated_tests/
   test_humaneval_0_success.py                    # Basic generation (tests passed)
   test_humaneval_0_success.stats.json            # Usage statistics with coverage
   test_humaneval_1_docstring_false.py            # With docstring (tests failed)
   test_humaneval_1_docstring_false.stats.json    # Usage statistics with coverage
   test_humaneval_2_ast_success.py                # With AST (tests passed)
   test_humaneval_2_ast_success.stats.json        # Usage statistics with coverage
   test_humaneval_3_docstring_ast_success.py      # With both options (tests passed)
   test_humaneval_3_docstring_ast_success.stats.json # Usage statistics with coverage
```

### Console Output Example

```
Loading dataset from dataset/HumanEval.jsonl...
Loaded 164 problems from dataset
Selected problem: HumanEval/139
Generating test cases for HumanEval/139...

================================================================================
PROMPT PREVIEW
================================================================================
Generate pytest test cases for this function...
[Full prompt displayed here]
================================================================================
Estimated input tokens: 1,234
Estimated input cost: $0.003702
================================================================================

Proceed with this prompt? (y/n/q): y
Test cases saved to generated_tests/test_humaneval_139_ast.py

✅ Successfully generated test cases!
📁 Output file: generated_tests/test_humaneval_139_ast.py

📊 Token Usage & Cost:
  Input tokens: 1,234
  Output tokens: 567
  Total tokens: 1,801
  Total cost: $0.012345

To run the tests:
  cd generated_tests
  pytest test_humaneval_139_ast.py -v --cov
```

## Running Generated Tests

Navigate to the output directory and run pytest:

```bash
cd generated_tests
```

### Common pytest Options

| Option                 | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| `-v, --verbose`        | Verbose output showing individual test names and results |
| `-s`                   | Don't capture output (show print statements)             |
| `-x`                   | Stop on first failure                                    |
| `--tb=short`           | Shorter traceback format                                 |
| `--tb=line`            | One line per failure                                     |
| `--tb=no`              | No traceback                                             |
| `-k EXPRESSION`        | Run tests matching keyword expression                    |
| `--maxfail=N`          | Stop after N failures                                    |
| `-q, --quiet`          | Quiet mode (less verbose)                                |
| `--collect-only`       | Show which tests would be run without executing          |
| `--lf, --last-failed`  | Run only tests that failed in last run                   |
| `--ff, --failed-first` | Run failed tests first, then rest                        |

### Coverage Options

| Option               | Description                        |
| -------------------- | ---------------------------------- |
| `--cov`              | Generate coverage report           |
| `--cov-report=term`  | Terminal coverage report (default) |
| `--cov-report=html`  | HTML coverage report               |
| `--cov-report=xml`   | XML coverage report                |
| `--cov-fail-under=N` | Fail if coverage is under N%       |

### Example Usage

#### Run specific test file:

```bash
pytest test_humaneval_0.py -v
```

#### Run with coverage:

```bash
pytest test_humaneval_0.py -v --cov
```

#### Run with detailed coverage report:

```bash
pytest test_humaneval_0.py -v --cov --cov-report=html
```

#### Stop on first failure with short traceback:

```bash
pytest test_humaneval_0.py -v -x --tb=short
```

#### Run only failed tests from last run:

```bash
pytest --lf -v
```

#### Run tests matching a keyword:

```bash
pytest -k "edge_case" -v
```

#### Run all generated tests:

```bash
pytest -v --cov
```

## Cost Optimization

### Token Usage Control

The new options provide different levels of context and cost:

#### Default (Signature Only) - Lowest Cost:

```bash
python run_test_case_generator.py
```

- Sends only function signature: `def function_name(params) -> return_type:`
- Lowest token usage = lowest cost
- Good for most cases

#### With Docstring - Medium Cost, More Context:

```bash
python run_test_case_generator.py --include-docstring
```

- Sends full function signature + docstring with examples
- Medium token usage = medium cost
- Better test quality with more context

#### With AST - Higher Cost, Enhanced Understanding:

```bash
python run_test_case_generator.py --include-ast
```

- Sends function signature + AST representation of canonical solution
- Higher token usage = higher cost
- Enhanced code structure understanding for better tests

#### With Both - Highest Cost, Maximum Context:

```bash
python run_test_case_generator.py --include-docstring --include-ast
```

- Sends full function signature + docstring + AST representation
- Highest token usage = highest cost
- Maximum context for highest quality tests

### Interactive Prompt Preview

By default, prompt preview is enabled. Use `--no-show-prompt` to:

- Skip the preview of the prompt sent to Claude
- Avoid interactive confirmations in automated contexts
- Prevent "EOF when reading a line" in non-interactive environments

### Pricing Information

Current Claude 3.5 Sonnet pricing:

- **Input tokens**: $3 per 1M tokens
- **Output tokens**: $15 per 1M tokens

Typical usage per problem:

**Initial Generation:**

- **Signature only**: ~800-1,200 input tokens
- **With docstring**: ~1,500-2,500 input tokens
- **With AST**: ~1,000-1,800 input tokens
- **With both**: ~2,000-3,500 input tokens
- **Generated output**: ~500-1,000 tokens

**With Evaluation and Error Fixing:**

- **Additional input per fix**: ~1,500-4,000 tokens (includes error output + function implementation)
- **Additional output per fix**: ~500-1,500 tokens
- **Total fix attempts**: 0-3 (average: 1-2)

**Total Cost Examples:**

- **No evaluation**: ~$0.01-0.05 per problem
- **With evaluation (no fixes needed)**: ~$0.01-0.05 per problem
- **With evaluation (1-2 fix attempts)**: ~$0.02-0.08 per problem
- **With evaluation (3 fix attempts)**: ~$0.03-0.12 per problem

## File Structure

```
project/
   batch/                       # Batch processing tools
      run_batch_test_case_generator.py   # Batch test generation script
      readme.md                 # Batch processing documentation
   dataset/
      HumanEval.jsonl          # HumanEval dataset
   generated_tests/             # Generated test files
      test_humaneval_*.py      # Test cases (various naming patterns)
      test_humaneval_*.stats.json  # Usage statistics
   visualizations/              # Generated visualization graphs (created by visualize_results.py)
      1_success_rate.png       # Success rate comparison
      2_code_coverage.png      # Coverage analysis
      3_cost_analysis.png      # Cost comparison
      4_fix_attempts.png       # Fix attempts analysis
      5_success_by_problem.png # Problem difficulty heatmap
      6_cost_vs_quality.png    # Cost vs quality scatter plot
      7_input_tokens.png       # Input token usage comparison
      8_success_by_complexity.png        # Dataset-aware: Success by complexity level
      9_success_by_algorithm_type.png    # Dataset-aware: Success by algorithm type
      10_config_performance_by_complexity.png # Dataset-aware: Multi-metric complexity analysis
      11_cost_vs_complexity.png          # Dataset-aware: Cost vs complexity relationship
      12_algorithm_type_distribution.png # Dataset-aware: Algorithm type distribution
   .env                         # API key configuration
   .gitignore                   # Git ignore rules
   requirements.txt             # Python dependencies
   run_test_case_generator.py       # Main test generation script
   visualize_results.py         # Results analysis and visualization tool
   README.md                    # This file
```

## Statistics File Format

Each `.stats.json` file contains:

```json
{
  "total_input_tokens": 3876,
  "total_output_tokens": 2038,
  "total_tokens": 5914,
  "total_cost_usd": 0.042198,
  "task_id": "HumanEval/4",
  "generated_file": "generated_tests/test_humaneval_4_success.py",
  "evaluation_enabled": true,
  "evaluation_success": true,
  "fix_attempts_used": 3,
  "max_pytest_runs": 3,
  "code_coverage_percent": 85.7
}
```

**Fields for evaluation and quality tracking:**

- `evaluation_enabled`: Whether automatic evaluation was used
- `evaluation_success`: Whether tests finally passed after fixing
- `fix_attempts_used`: Number of fix attempts actually used
- `max_pytest_runs`: Maximum pytest runs that were configured (kept as max_pytest_runs for backward compatibility)
- `code_coverage_percent`: Final code coverage percentage from pytest --cov
- `generated_file`: Final filename (includes success/failure suffix)
- `total_cost_usd`: Now includes costs from all fix attempts, not just initial generation

## Troubleshooting

### Common Issues

1. **"No such file or directory: 'HumanEval.jsonl'"**

   - Make sure the dataset file exists in the correct location
   - Use `--dataset` option to specify the correct path

2. **"API key not found"**

   - Set your API key using one of the configuration methods above
   - Make sure the `.env` file is in the same directory as the script

3. **"Permission denied"**

   - Check file permissions for the output directory
   - Make sure you have write access to the target location

4. **Import errors in generated tests**

   - The generated tests import the function from the same file
   - Make sure to run pytest from the correct directory

5. **EOF when reading a line (prompt preview enabled)**

   - This happens when running non-interactively
   - Either run in an interactive terminal or add `--no-show-prompt`

6. **Syntax errors in generated pytest code**

   - The tool now includes automatic error fixing with evaluation
   - Improved prompt instructions for proper quote escaping
   - If issues persist, try `--disable-evaluation` or `--max-pytest-runs 1`

7. **Evaluation fails or times out**

   - Check that pytest is installed: `pip install pytest pytest-cov`
   - Verify the generated test file has no import errors
   - Use `--quiet-evaluation` to reduce output noise
   - Try `--disable-evaluation` if evaluation keeps failing

8. **Fix attempts exceed maximum**
   - Some complex errors may require manual intervention
   - Check the final error output for specific issues
   - Try increasing `--max-pytest-runs` or use `--disable-evaluation`
   - Consider using different generation options (`--include-docstring`, `--include-ast`)

### Getting Help

For additional help:

```bash
python run_test_case_generator.py --help
```

## Advanced Usage Tips

### Batch Generation with Different Options

```bash
# Generate multiple variants of the same problem
python run_test_case_generator.py --task-id "HumanEval/0"
python run_test_case_generator.py --task-id "HumanEval/0" --include-docstring
python run_test_case_generator.py --task-id "HumanEval/0" --include-ast
python run_test_case_generator.py --task-id "HumanEval/0" --include-docstring --include-ast
```

### Cost-Effective Workflow

1. By default, prompt preview helps you understand token usage
2. Use basic generation for simple functions
3. Add `--include-docstring` for complex functions needing examples
4. Add `--include-ast` for functions with complex logic structure
5. Use both options only for the most challenging problems

### Quality Comparison

Test the same problem with different options to compare:

- Test coverage percentage
- Edge case detection
- Code quality and readability
- Execution time and performance

## Dataset Analysis and Classification

The enhanced visualization system automatically analyzes the HumanEval dataset to understand the complexity and characteristics of each programming problem. This enables dataset-aware analysis that provides insights into how different configurations perform across various types of coding challenges.

### Problem Classification Methodology

#### Complexity Level Classification

Each HumanEval problem is automatically classified into complexity levels based on code structure analysis:

**Algorithm:** AST (Abstract Syntax Tree) parsing of canonical solutions

**Complexity Scoring Formula:**

```
complexity_score = (
    loop_count × 2 +
    condition_count × 1.5 +
    max_loop_depth × 3 +
    max_condition_depth × 2 +
    function_calls × 0.5 +
    list_comprehensions × 1.5 +
    (total_ast_nodes / 10)
)
```

**Classification Thresholds:**

- **Simple** (score ≤ 5): Basic operations, minimal control flow

  - Examples: String length, arithmetic operations, simple transformations
  - Characteristics: Linear execution, single operations, direct calculations

- **Medium** (5 < score ≤ 15): Moderate algorithmic complexity

  - Examples: List processing with conditions, simple loops, basic algorithms
  - Characteristics: Single loops, conditional branching, moderate logic

- **Complex** (score > 15): Advanced algorithmic challenges
  - Examples: Nested loops, complex state management, multi-step algorithms
  - Characteristics: Multiple control structures, nested operations, complex logic flow

#### Algorithm Type Classification

Problems are categorized by their primary algorithmic approach based on prompt analysis and code patterns:

**Classification Categories:**

1. **String Manipulation**: Text processing, character operations, string transformations
2. **Mathematical**: Numerical computations, arithmetic operations, mathematical formulas
3. **Number Theory**: Prime numbers, factorization, mathematical sequences
4. **List Operations**:
   - List Manipulation: General list processing
   - List Sorting: Ordering and arrangement algorithms
   - List Search: Finding and indexing operations
5. **Mathematical Sequence**: Fibonacci, factorial, sequence generation
6. **General Logic**: Control flow, validation, pattern matching
7. **Data Structures**: Dictionary, set, and advanced data structure operations
8. **Validation**: Input checking, constraint verification, pattern validation

**Classification Process:**

- **Keyword Analysis**: Prompt text analyzed for algorithm-specific terms
- **Code Pattern Recognition**: AST structure examined for algorithmic patterns
- **Context Understanding**: Function purpose and examples considered
- **Hierarchical Classification**: Multiple patterns resolved to primary type

### Dataset Distribution Analysis

#### Complexity Distribution (Based on Current Analysis):

- **Complex Problems**: 46.3% (304 problems)
- **Medium Problems**: 35.4% (232 problems)
- **Simple Problems**: 18.3% (120 problems)

#### Algorithm Type Distribution (Top Categories):

- **String Manipulation**: 38.4% (252 problems)
- **Mathematical**: 34.1% (224 problems)
- **List Manipulation**: 7.3% (48 problems)
- **Number Theory**: 5.5% (36 problems)
- **Mathematical Sequence**: 4.9% (32 problems)

### Configuration Effectiveness by Problem Type

The analysis reveals how different test generation configurations perform across problem types:

#### Performance by Complexity:

- **Simple Problems**: Docstring config achieves 80% success rate
- **Medium Problems**: AST config performs best with 62.1% success rate
- **Complex Problems**: Docstring config leads with 60.5% success rate

#### Algorithm-Specific Success Rates:

- **List Search**: 100% success (easiest category)
- **String Sorting**: 68.8% success
- **Mathematical**: 61.6% success
- **Mathematical Sequence**: 31.2% success (most challenging)

### Practical Applications

This classification system enables:

1. **Targeted Configuration Selection**: Choose optimal prompt strategy based on problem type
2. **Cost Optimization**: Use expensive configurations only where they provide value
3. **Quality Prediction**: Anticipate which problems may require more attention
4. **Performance Analysis**: Understand systematic strengths and weaknesses of each approach

## Results Visualization

The repository includes a powerful visualization tool (`visualize_results.py`) that analyzes all generated test results and creates comprehensive graphs comparing different configuration options, now enhanced with dataset-aware analysis.

### Overview

The visualization tool automatically scans the `generated_tests/` directory, parses all `.stats.json` files, and generates 12 comprehensive visualization graphs to help you understand:

- **Performance comparison** between different configurations (basic, AST, docstring, AST+docstring)
- **Cost-effectiveness analysis** of different prompt strategies
- **Quality metrics** including success rates and code coverage
- **Problem difficulty patterns** across different HumanEval problems
- **Dataset-aware analysis** showing performance by problem complexity and algorithm type
- **Configuration effectiveness** across different categories of coding challenges

### Usage

#### Install Additional Dependencies

The visualization tool requires additional Python libraries:

```bash
pip install -r requirements.txt  # Includes: pandas, matplotlib, seaborn, numpy
```

#### Run Visualization Analysis

```bash
python visualize_results.py
```

#### Output

The tool creates:

- **12 PNG graphs** in the `visualizations/` directory (7 traditional + 5 dataset-aware)
- **Console statistics** with detailed numerical analysis including dataset classification
- **Configuration comparison** showing which approach works best for different problem types

### Generated Visualizations

The tool creates 12 comprehensive graphs (7 traditional + 5 dataset-aware):

#### 1. Success Rate by Configuration (`1_success_rate.png`)

- Bar chart showing test success percentage for each configuration
- Displays sample size (n=X) for statistical significance
- Ordered: basic → ast → docstring → ast+docstring

#### 2. Code Coverage by Configuration (`2_code_coverage.png`)

- Box plot showing coverage distribution + average coverage bar chart
- Helps identify which configurations achieve better test quality
- Shows both variability and mean performance

#### 3. Cost Analysis by Configuration (`3_cost_analysis.png`)

- Box plot and bar chart of total costs in USD
- Compares the financial efficiency of different prompt strategies
- Includes error bars showing cost variability

#### 4. Fix Attempts by Configuration (`4_fix_attempts.png`)

- Shows how many fix attempts each configuration typically requires
- Lower numbers indicate more reliable initial test generation
- Helps identify which approaches need less iteration

#### 5. Success Rate by Problem ID (`5_success_by_problem.png`)

- Heatmap showing success rates across different HumanEval problems
- Identifies which problems are more challenging
- Shows how different configurations perform on specific problems
- Green = high success rate, Red = low success rate

#### 6. Cost vs Quality Scatter Plot (`6_cost_vs_quality.png`)

- Scatter plot with cost (USD) on x-axis, coverage (%) on y-axis
- Different colors for each configuration type
- Includes trend line to show overall cost-quality relationship
- Helps identify the sweet spot for cost-effectiveness

#### 7. Input Token Usage by Configuration (`7_input_tokens.png`)

- Box plot and bar chart showing input token consumption
- **Key metric** for understanding prompt cost differences
- Shows exactly how much more expensive docstring/AST options are
- Essential for budget planning and cost optimization

### Dataset-Aware Visualizations (New)

#### 8. Success Rate by Problem Complexity (`8_success_by_complexity.png`)

- Bar chart and heatmap showing performance across simple/medium/complex problems
- Reveals which configurations excel at different difficulty levels
- Ordered complexity: simple → medium → complex (left to right)
- Enables targeted configuration selection based on problem difficulty

#### 9. Success Rate by Algorithm Type (`9_success_by_algorithm_type.png`)

- Distribution chart and performance analysis by algorithm category
- Shows which problem types are most/least challenging
- Identifies configuration strengths for specific algorithmic approaches
- Consistent algorithm ordering across all related charts

#### 10. Configuration Performance by Complexity (`10_config_performance_by_complexity.png`)

- Multi-metric analysis (success rate, coverage, cost, fix attempts) across complexity levels
- 2x2 subplot showing comprehensive performance comparison
- Helps understand trade-offs between configurations at different difficulty levels
- Essential for cost-benefit analysis in complex problem domains

#### 11. Cost vs Complexity Analysis (`11_cost_vs_complexity.png`)

- Scatter plot and box plot showing resource usage patterns by problem difficulty
- Reveals cost scaling behavior across complexity levels
- Helps predict budget requirements for different problem types
- Identifies whether complex problems actually cost more to solve

#### 12. Algorithm Type Distribution (`12_algorithm_type_distribution.png`)

- Pie chart showing dataset composition by algorithm type
- Horizontal bar chart of success rates by algorithm category
- Provides dataset overview and identifies systematic challenge areas
- Shows which algorithm types dominate the dataset

### How to see the Hakohigezu (箱ヒゲ図)

https://cacco.co.jp/datascience/blog/statistics/203/

### Example Console Output

```bash
Loading data from generated_tests...
Found 12 stats files
Successfully loaded 12 records

================================================================================
SUMMARY STATISTICS
================================================================================
                    success       total_input_tokens  total_cost_usd code_coverage_percent fix_attempts_used
config_type                count mean mean    std     mean    std    mean    std           mean    std
ast                        3     1.0  978.0   0.0     0.011   0.0    100.0   0.0           1.0     0.0
basic                      3     0.67 542.3   98.1    0.032   0.012  66.7    57.7          2.33    0.58
docstring                  3     1.0  1456.7  245.2   0.031   0.008  100.0   0.0           2.0     1.0
docstring_ast              3     1.0  3371.0  0.0     0.028   0.0    100.0   0.0           2.0     0.0

================================================================================
CONFIGURATION TYPE ANALYSIS
================================================================================

AST:
  Samples: 3
  Success Rate: 100.0%
  Avg Input Tokens: 978 ± 0
  Avg Cost: $0.0110 ± $0.0000
  Avg Coverage: 100.0% ± 0.0%
  Avg Fix Attempts: 1.00 ± 0.00

BASIC:
  Samples: 3
  Success Rate: 66.7%
  Avg Input Tokens: 542 ± 98
  Avg Cost: $0.0324 ± $0.0123
  Avg Coverage: 66.7% ± 57.7%
  Avg Fix Attempts: 2.33 ± 0.58

...

Analysis complete! Check the 'visualizations/' directory for graphs.
```

### Data Analysis Features

The visualization tool provides:

#### Smart Data Parsing

- Automatically detects configuration type from filenames
- Handles both old and new stats file formats
- Processes success/failure status from filename suffixes
- Groups data by problem ID and configuration type

#### Statistical Analysis

- Calculates means, standard deviations, and sample sizes
- Provides confidence intervals through error bars
- Shows distribution patterns with box plots
- Identifies trends and correlations

#### Comparative Insights

- **Cost Efficiency**: Compare input tokens across configurations
- **Quality Assessment**: Analyze success rates and coverage percentages
- **Reliability Metrics**: Examine fix attempt requirements
- **Problem Difficulty**: Identify challenging HumanEval problems

### Interpretation Guide

#### Configuration Comparison

- **Basic**: Lowest cost, variable success rate
- **AST**: Moderate cost, good structural understanding
- **Docstring**: Higher cost, benefits from examples and context
- **AST+Docstring**: Highest cost, maximum context and quality

#### Key Metrics to Watch

- **Success Rate**: Percentage of test generations that ultimately pass
- **Input Tokens**: Direct cost driver for API usage
- **Code Coverage**: Quality indicator of generated tests
- **Fix Attempts**: Reliability indicator (fewer is better)

#### Optimization Strategies

1. **Budget-Conscious**: Use basic configuration for simple problems
2. **Quality-Focused**: Use AST+docstring for complex problems
3. **Balanced Approach**: Start with AST, add docstring for difficult problems
4. **Problem-Specific**: Use heatmap to identify which problems need more context

## Requirements

- Python 3.8+
- anthropic >= 0.7.0
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- python-dotenv >= 1.0.0

## License

This project is for educational and research purposes.
