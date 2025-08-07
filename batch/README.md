# Batch Test Case Generator

A batch processing tool that automates running the test case generator for multiple HumanEval problems, making it easy to generate test cases for many problems at once.

## Features

- **Range-based generation**: Generate tests for HumanEval/0 through HumanEval/N
- **Specific task selection**: Generate tests for comma-separated specific task IDs
- **Multi-model support**: Generate tests using multiple Claude models simultaneously
- **Progress tracking**: Real-time progress updates and statistics
- **Error handling**: Robust error handling with user-controlled continuation
- **Timeout protection**: 5-minute timeout per task to prevent hanging
- **Comprehensive reporting**: Detailed success/failure statistics

## Usage

### Basic Usage

Generate test cases for a range of problems:

```bash
# Generate tests for HumanEval/0 through HumanEval/10
python batch_test_generator.py --start 0 --end 10

# Generate with docstrings and AST for range 0-5
python batch_test_generator.py --start 0 --end 5 --include-docstring --include-ast

# Generate specific task IDs
python batch_test_generator.py --task-ids "HumanEval/0,HumanEval/5,HumanEval/10"

# Fast generation without evaluation for range 0-20
python batch_test_generator.py --start 0 --end 20 --disable-evaluation
```

### Command Line Options

| Option                   | Description                                   | Default                    |
| ------------------------ | --------------------------------------------- | -------------------------- |
| `--start N`              | Start task ID number                          | 0                          |
| `--end N`                | End task ID number                            | 50                         |
| `--task-ids "X,Y,Z"`     | Comma-separated specific task IDs             | None (use range)           |
| `--models MODEL1 MODEL2` | Claude model(s) to use (can specify multiple) | claude-3-5-sonnet-20241022 |
| `--dataset PATH`         | Path to HumanEval dataset file                | dataset/HumanEval.jsonl    |
| `--output-dir DIR`       | Output directory for test files               | generated_tests            |
| `--include-docstring`    | Include function docstring in prompt          | False                      |
| `--include-ast`          | Include AST of canonical solution in prompt   | False                      |
| `--disable-evaluation`   | Skip automatic test evaluation                | False                      |
| `--quiet-evaluation`     | Less verbose evaluation output                | False                      |
| `--max-fix-attempts N`   | Maximum fix attempts per task                 | 3                          |
| `--task-timeout N`       | Timeout in seconds for each task              | 300 (5 minutes)            |

### Multi-Model Generation

Generate tests using multiple Claude models simultaneously:

```bash
# Use multiple models for comprehensive testing
python batch_test_generator.py --start 0 --end 5 --models claude-3-5-sonnet-20241022 claude-3-5-haiku-20241022

# Compare model performance across a range
python batch_test_generator.py --start 0 --end 10 --models claude-3-5-sonnet-20241022 claude-3-opus-20240229
```

## Examples

### Generate test for problems 0-10 with full context:

```bash
python batch_test_generator.py --start 0 --end 10 --include-docstring --include-ast
```

### Generate specific problems with evaluation disabled:

```bash
python batch_test_generator.py --task-ids "HumanEval/0,HumanEval/15,HumanEval/30" --disable-evaluation
```

### Quiet batch processing for automation:

```bash
python batch_test_generator.py --start 0 --end 50 --quiet-evaluation --max-fix-attempts 1
```

### Custom timeout for complex problems:

```bash
python batch_test_generator.py --start 0 --end 10 --task-timeout 600 --include-docstring
```

## Interactive Features

### Error Handling

When a task fails during batch processing, you'll be prompted:

```
❓ Task HumanEval/5 failed. Continue with remaining tasks? (y/n/q):
```

Options:

- `y` (yes): Continue with the next task
- `n` (no): Stop batch processing
- `q` (quit): Immediately quit the program

**Note**: When using `--quiet-evaluation`, failed tasks automatically continue to the next task without prompting, making it suitable for automation.

### Progress Tracking

Real-time progress updates:

```
📊 Progress: 3/10 (30.0%)
🚀 Processing HumanEval/2
```

### Final Summary

Comprehensive batch processing report:

```
🏁 BATCH PROCESSING COMPLETE
📊 Summary:
  Total tasks: 10
  ✅ Successful: 8
  ❌ Failed: 2
  ⏭️  Skipped: 0
  ⏱️  Duration: 145.3 seconds
  📁 Output directory: generated_tests
```

## Output Structure

The batch generator creates the same file structure as the single generator, organized by task ID:

```
generated_tests/
   test_humaneval_0_success.py
   test_humaneval_0_success.stats.json
   test_humaneval_1_docstring_false.py
   test_humaneval_1_docstring_false.stats.json
   ...
```

## Performance Considerations

- **Timeout**: Each task has a configurable timeout (default 5 minutes) to prevent hanging
- **Memory**: Processes run sequentially to manage memory usage
- **API Limits**: Respects Claude API rate limits automatically
- **Disk Space**: Monitor available space for large batch generations

### Timeout Configuration

Use `--task-timeout` to adjust the per-task timeout based on your needs:

- **Simple problems**: `--task-timeout 180` (3 minutes)
- **Complex problems**: `--task-timeout 600` (10 minutes)
- **Very complex problems**: `--task-timeout 900` (15 minutes)

## Error Recovery

The batch generator includes robust error handling:

1. **Subprocess Errors**: Captures and reports command failures
2. **Timeout Protection**: Prevents infinite hanging on problematic tasks
3. **User Control**: Allows continuation or stopping on failures
4. **Graceful Shutdown**: Handles Ctrl+C interruption cleanly

## Integration with Main Tool

The batch generator wraps the main `run_test_case_generator.py` tool, passing through all supported options. Ensure the main generator is in the same directory.

## Requirements

- Python 3.8+
- All dependencies from main test generator
- `run_test_case_generator.py` in the same directory
- Valid HumanEval dataset file

## Tips for Effective Batch Processing

1. **Start Small**: Test with a small range first (e.g., --start 0 --end 5)
2. **Use Quiet Mode**: Add `--quiet-evaluation` for large batches
3. **Monitor Progress**: Keep an eye on success/failure patterns
4. **Check Disk Space**: Large batches generate many files
5. **Consider Cost**: Batch processing with full options can be expensive
