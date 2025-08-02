# HumanEval Test Case Generator

A Python tool that automatically generates comprehensive pytest test cases for HumanEval problems using Claude API. The generated test cases can be used for code coverage analysis and testing.

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
python test_case_generator.py --api-key "your-api-key-here"
```

## Usage

### Basic Usage

Generate test cases for a random problem:

```bash
python test_case_generator.py
```

### Command Line Options

| Option                | Description                                                   | Default                   |
| --------------------- | ------------------------------------------------------------- | ------------------------- |
| `--dataset`           | Path to HumanEval dataset file                                | `dataset/HumanEval.jsonl` |
| `--output-dir`        | Output directory for test files                               | `generated_tests`         |
| `--task-id`           | Specific task ID to generate tests for                        | Random selection          |
| `--api-key`           | Claude API key                                                | From .env or environment  |
| `--include-docstring` | Include function docstring in prompt                          | `False` (signature only)  |
| `--include-ast`       | Include AST of canonical solution in prompt                   | `False`                   |
| `--show-prompt`       | Display prompt before sending to LLM and ask for confirmation | `False`                   |
| `--disable-evaluation` | Disable automatic test evaluation and error fixing           | `False` (evaluation enabled) |
| `--max-fix-attempts`  | Maximum number of attempts to fix test errors                 | `3`                       |
| `--quiet-evaluation`  | Disable verbose output during error fixing process            | `False` (verbose enabled) |

### Examples

#### Generate test for a random problem:

```bash
python test_case_generator.py
```

#### Generate test for a specific problem:

```bash
python test_case_generator.py --task-id "HumanEval/0"
```

#### Include docstring for more context (uses more tokens):

```bash
python test_case_generator.py --include-docstring
```

#### Include AST representation for enhanced understanding:

```bash
python test_case_generator.py --include-ast
```

#### Preview prompt before sending to LLM:

```bash
python test_case_generator.py --show-prompt
```

#### Use custom dataset and output directory:

```bash
python test_case_generator.py --dataset path/to/custom.jsonl --output-dir my_tests
```

#### Combine options:

```bash
python test_case_generator.py --task-id "HumanEval/5" --include-docstring --include-ast --show-prompt --output-dir custom_tests
```

### Evaluation and Error Fixing

The tool automatically evaluates generated test cases and fixes errors using an intelligent feedback loop:

#### Generate with automatic evaluation (default):

```bash
python test_case_generator.py --task-id "HumanEval/0"
```

This will:
1. Generate initial test cases
2. Run `pytest test_humaneval_0.py --cov -v` automatically
3. If tests fail, analyze errors and send them to LLM for fixing
4. Repeat up to 3 times until tests pass
5. Show transparent debugging information throughout

#### Control evaluation behavior:

```bash
# Disable evaluation (original behavior)
python test_case_generator.py --task-id "HumanEval/0" --disable-evaluation

# Set maximum fix attempts 
python test_case_generator.py --task-id "HumanEval/0" --max-fix-attempts 5

# Quiet mode (less verbose output during fixing)
python test_case_generator.py --task-id "HumanEval/0" --quiet-evaluation

# Interactive mode (approve each fix attempt)
python test_case_generator.py --task-id "HumanEval/0" --show-prompt
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
✅ Tests passed on attempt 2
🎉 Test generation and evaluation completed successfully!
```

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

The tool automatically adjusts filenames based on options used:

- Default: `test_humaneval_0.py`
- With docstring: `test_humaneval_0_docstring.py`
- With AST: `test_humaneval_0_ast.py`
- With both: `test_humaneval_0_docstring_ast.py`

### Example Output Structure

```
generated_tests/
   test_humaneval_0.py                    # Basic generation
   test_humaneval_0.stats.json            # Usage statistics
   test_humaneval_1_docstring.py          # With docstring
   test_humaneval_1_docstring.stats.json  # Usage statistics
   test_humaneval_2_ast.py                # With AST
   test_humaneval_2_ast.stats.json        # Usage statistics
   test_humaneval_3_docstring_ast.py      # With both options
   test_humaneval_3_docstring_ast.stats.json # Usage statistics
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

| Option | Description |
|--------|-------------|
| `-v, --verbose` | Verbose output showing individual test names and results |
| `-s` | Don't capture output (show print statements) |
| `-x` | Stop on first failure |
| `--tb=short` | Shorter traceback format |
| `--tb=line` | One line per failure |
| `--tb=no` | No traceback |
| `-k EXPRESSION` | Run tests matching keyword expression |
| `--maxfail=N` | Stop after N failures |
| `-q, --quiet` | Quiet mode (less verbose) |
| `--collect-only` | Show which tests would be run without executing |
| `--lf, --last-failed` | Run only tests that failed in last run |
| `--ff, --failed-first` | Run failed tests first, then rest |

### Coverage Options

| Option | Description |
|--------|-------------|
| `--cov` | Generate coverage report |
| `--cov-report=term` | Terminal coverage report (default) |
| `--cov-report=html` | HTML coverage report |
| `--cov-report=xml` | XML coverage report |
| `--cov-fail-under=N` | Fail if coverage is under N% |

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
python test_case_generator.py
```

- Sends only function signature: `def function_name(params) -> return_type:`
- Lowest token usage = lowest cost
- Good for most cases

#### With Docstring - Medium Cost, More Context:

```bash
python test_case_generator.py --include-docstring
```

- Sends full function signature + docstring with examples
- Medium token usage = medium cost
- Better test quality with more context

#### With AST - Higher Cost, Enhanced Understanding:

```bash
python test_case_generator.py --include-ast
```

- Sends function signature + AST representation of canonical solution
- Higher token usage = higher cost
- Enhanced code structure understanding for better tests

#### With Both - Highest Cost, Maximum Context:

```bash
python test_case_generator.py --include-docstring --include-ast
```

- Sends full function signature + docstring + AST representation
- Highest token usage = highest cost
- Maximum context for highest quality tests

### Interactive Prompt Preview

Use `--show-prompt` to:

- Preview the exact prompt that will be sent to Claude
- See estimated token count and cost
- Decide whether to proceed, modify, or cancel
- Avoid unexpected API charges

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
   dataset/
      HumanEval.jsonl          # HumanEval dataset
   generated_tests/             # Generated test files
      test_humaneval_*.py      # Test cases (various naming patterns)
      test_humaneval_*.stats.json  # Usage statistics
   .env                         # API key configuration
   .gitignore                   # Git ignore rules
   requirements.txt             # Python dependencies
   test_case_generator.py       # Main script
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
  "generated_file": "generated_tests/test_humaneval_4.py",
  "evaluation_enabled": true,
  "evaluation_success": true,
  "fix_attempts_used": 3,
  "max_fix_attempts": 3
}
```

**New fields for evaluation tracking:**
- `evaluation_enabled`: Whether automatic evaluation was used
- `evaluation_success`: Whether tests finally passed after fixing
- `fix_attempts_used`: Number of fix attempts actually used
- `max_fix_attempts`: Maximum attempts that were configured
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

5. **EOF when reading a line (with --show-prompt)**

   - This happens when running non-interactively
   - Either run in an interactive terminal or omit `--show-prompt`

6. **Syntax errors in generated pytest code**
   - The tool now includes automatic error fixing with evaluation
   - Improved prompt instructions for proper quote escaping
   - If issues persist, try `--disable-evaluation` or `--max-fix-attempts 1`

7. **Evaluation fails or times out**
   - Check that pytest is installed: `pip install pytest pytest-cov`
   - Verify the generated test file has no import errors
   - Use `--quiet-evaluation` to reduce output noise
   - Try `--disable-evaluation` if evaluation keeps failing

8. **Fix attempts exceed maximum**
   - Some complex errors may require manual intervention
   - Check the final error output for specific issues
   - Try increasing `--max-fix-attempts` or use `--disable-evaluation`
   - Consider using different generation options (`--include-docstring`, `--include-ast`)

### Getting Help

For additional help:

```bash
python test_case_generator.py --help
```

## Advanced Usage Tips

### Batch Generation with Different Options

```bash
# Generate multiple variants of the same problem
python test_case_generator.py --task-id "HumanEval/0"
python test_case_generator.py --task-id "HumanEval/0" --include-docstring
python test_case_generator.py --task-id "HumanEval/0" --include-ast
python test_case_generator.py --task-id "HumanEval/0" --include-docstring --include-ast
```

### Cost-Effective Workflow

1. Start with `--show-prompt` to understand token usage
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

## Requirements

- Python 3.8+
- anthropic >= 0.7.0
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- python-dotenv >= 1.0.0

## License

This project is for educational and research purposes.
