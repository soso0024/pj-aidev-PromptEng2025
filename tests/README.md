# Test Suite for TestCaseGenerator

This directory contains comprehensive tests for the `run_test_case_generator.py` module, which generates pytest-compatible test cases for HumanEval problems using Claude API.

## 📁 Files

- `test_run_test_case_generator.py` - Complete test suite with 52 tests
- `README.md` - This documentation file

## 🎯 Test Coverage

The test suite provides **100% mock coverage** and validates all major functionality without making real API calls or external dependencies.

### Test Categories (52 tests total)

| Category               | Tests | Description                                            |
| ---------------------- | ----- | ------------------------------------------------------ |
| **Initialization**     | 6     | Configuration loading, model selection, error handling |
| **Dataset Operations** | 6     | JSONL loading, problem selection, error cases          |
| **Prompt Generation**  | 7     | Function signatures, docstrings, AST integration       |
| **Code Cleaning**      | 5     | Markdown removal, duplicate handling, validation       |
| **API Integration**    | 6     | Cost calculation, usage tracking, API calls            |
| **File Operations**    | 4     | File saving, renaming, statistics management           |
| **Pytest Evaluation**  | 7     | Test execution, error fixing, workflow                 |
| **Error Handling**     | 11    | Edge cases, user interactions, error scenarios         |

## 🚀 Running Tests

### Prerequisites

Install test dependencies:

```bash
uv add pytest-mock  # Already installed
```

### Basic Commands

**Run all tests:**

```bash
pytest tests/
```

**Run with verbose output:**

```bash
pytest tests/test_run_test_case_generator.py -v
```

**Run with coverage report:**

```bash
pytest tests/ --cov=test_case_generator --cov-report=html
```

### Specific Test Execution

**Run specific test class:**

```bash
pytest tests/test_run_test_case_generator.py::TestTestCaseGeneratorInitialization -v
pytest tests/test_run_test_case_generator.py::TestDatasetOperations -v
pytest tests/test_run_test_case_generator.py::TestPromptGeneration -v
pytest tests/test_run_test_case_generator.py::TestCodeCleaning -v
pytest tests/test_run_test_case_generator.py::TestAPIIntegrationAndCosts -v
pytest tests/test_run_test_case_generator.py::TestFileOperations -v
pytest tests/test_run_test_case_generator.py::TestPytestEvaluation -v
pytest tests/test_run_test_case_generator.py::TestErrorHandlingAndEdgeCases -v
```

**Run specific test:**

```bash
pytest tests/test_run_test_case_generator.py::TestTestCaseGeneratorInitialization::test_init_with_default_config -v
```

### Useful Options

| Command                        | Description                |
| ------------------------------ | -------------------------- |
| `pytest tests/ -v`             | Verbose output             |
| `pytest tests/ -s`             | Show print statements      |
| `pytest tests/ -x`             | Stop on first failure      |
| `pytest tests/ --lf`           | Run last failed tests only |
| `pytest tests/ --collect-only` | Show which tests would run |

## 🔧 Test Architecture

### Mocking Strategy

All tests use comprehensive mocking to avoid external dependencies:

- **API Calls**: No real Claude API requests
- **File I/O**: Mocked file operations
- **Network**: No external connections
- **Configuration**: Mocked config files

### Test Structure

Each test class follows this pattern:

```python
class TestCategoryName:
    """Test description."""

    def create_generator(self, mocker, **kwargs):
        """Helper to create mocked generator."""
        # Mock configuration and dependencies
        return TestCaseGenerator(api_key="test_key", **kwargs)

    def test_specific_functionality(self, mocker):
        """Test specific feature."""
        # Setup mocks
        # Execute functionality
        # Assert results
```

## 📊 Example Test Output

```bash
$ pytest tests/test_run_test_case_generator.py -v
============================= test session starts ==============================
platform darwin -- Python 3.12.11, pytest-8.4.1
collected 52 items

tests/test_run_test_case_generator.py::TestTestCaseGeneratorInitialization::test_init_with_default_config PASSED [  1%]
tests/test_run_test_case_generator.py::TestTestCaseGeneratorInitialization::test_init_with_custom_models PASSED [  3%]
tests/test_run_test_case_generator.py::TestTestCaseGeneratorInitialization::test_init_with_invalid_model PASSED [  5%]
...
tests/test_run_test_case_generator.py::TestErrorHandlingAndEdgeCases::test_print_model_summary PASSED [100%]

======================== 52 passed in 0.18s ===============================
```

## 🧪 What Gets Tested

### 1. Initialization & Configuration

- ✅ Default model loading from config
- ✅ Custom model selection and validation
- ✅ Invalid model error handling
- ✅ Missing/corrupt config file handling
- ✅ All initialization parameters

### 2. Dataset Operations

- ✅ HumanEval JSONL file loading
- ✅ Empty line handling in datasets
- ✅ Random problem selection
- ✅ Specific problem lookup
- ✅ Missing problem error handling

### 3. Prompt Generation

- ✅ Function signature extraction (simple & multiline)
- ✅ Docstring inclusion/exclusion
- ✅ AST representation generation
- ✅ Prompt template assembly
- ✅ Error handling for malformed code

### 4. Code Processing

- ✅ Markdown block removal from LLM responses
- ✅ Explanatory text filtering
- ✅ Duplicate import removal
- ✅ Syntax validation and fallback
- ✅ Test function detection

### 5. API Integration

- ✅ Cost calculation based on token usage
- ✅ Usage statistics tracking
- ✅ Model-specific configuration
- ✅ Successful API response handling
- ✅ API error scenarios

### 6. File Management

- ✅ Test file saving with proper structure
- ✅ File renaming with success/failure status
- ✅ Statistics file generation
- ✅ Directory structure creation

### 7. Test Evaluation

- ✅ pytest execution with success/failure
- ✅ Coverage percentage extraction
- ✅ Test timeout handling
- ✅ Error fixing prompts generation
- ✅ Multi-attempt fix workflow

### 8. Error Handling & Edge Cases

- ✅ User prompt confirmations
- ✅ Verbose/quiet mode operations
- ✅ Pytest error display formatting
- ✅ Function signature edge cases
- ✅ Model results summary display

## 💡 Key Benefits

### 🚀 **Fast Execution**

Tests run in ~0.18 seconds (no API calls)

### 💰 **Zero Cost**

No API tokens consumed during testing

### 🔒 **Secure**

No real API keys needed for testing

### 🎯 **Comprehensive**

Tests all code paths and error conditions

### ⚡ **Reliable**

Deterministic results every time

### 🌐 **Offline**

Works without internet connection

## 🔍 Test Development Guidelines

When adding new tests:

1. **Use the helper methods** - Each test class has `create_generator()` helper
2. **Mock external dependencies** - API calls, file I/O, network requests
3. **Test both success and failure** - Happy path and error scenarios
4. **Use descriptive test names** - Clear what functionality is being tested
5. **Follow existing patterns** - Consistent with current test structure
6. **Add docstrings** - Explain what each test validates

## 🛠 Troubleshooting

### Common Issues

**Missing pytest-mock:**

```bash
uv add pytest-mock
```

**Tests not found:**

```bash
# Run from project root
pytest tests/
```

**Import errors:**

```bash
# Ensure you're in the correct directory with test_case_generator.py
ls -la | grep test_case_generator.py
```

## 📈 Future Enhancements

Potential test improvements:

- [ ] Integration tests with real API (optional)
- [ ] Performance benchmarks
- [ ] Property-based testing with Hypothesis
- [ ] Test data fixtures for complex scenarios
- [ ] Parallel test execution
- [ ] Test report generation

---

## 📞 Support

For questions about the test suite:

1. Check this README
2. Review existing test patterns
3. Run tests with `-v` flag for details

**Happy Testing! 🎉**
