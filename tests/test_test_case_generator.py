"""
Comprehensive test suite for TestCaseGenerator module.

This test suite covers all major functionality of the TestCaseGenerator class
including initialization, dataset loading, prompt generation, API interactions,
file operations, and error handling.
"""

import pytest
import json
import tempfile
import shutil
import os
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch, mock_open, call
import anthropic

from test_case_generator import TestCaseGenerator


class TestTestCaseGeneratorInitialization:
    """Test TestCaseGenerator initialization and configuration."""

    def test_init_with_default_config(self, mocker):
        """Test initialization with default configuration."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }

        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mock_anthropic = mocker.patch("anthropic.Anthropic")

        generator = TestCaseGenerator(api_key="test_key")

        assert generator.models == ["claude-3-5-sonnet"]
        assert generator.include_docstring == False
        assert generator.include_ast == False
        assert generator.show_prompt == False
        assert generator.enable_evaluation == True
        assert generator.max_fix_attempts == 3
        assert generator.verbose_evaluation == True
        mock_anthropic.assert_called_once_with(api_key="test_key")

    def test_init_with_custom_models(self, mocker):
        """Test initialization with custom models."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                },
                "claude-3-haiku": {
                    "api_name": "claude-3-haiku-20240307",
                    "folder_name": "claude_3_haiku",
                    "pricing": {"input_per_1k": 0.00025, "output_per_1k": 0.00125},
                },
            },
        }

        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")

        generator = TestCaseGenerator(
            api_key="test_key", models=["claude-3-5-sonnet", "claude-3-haiku"]
        )

        assert generator.models == ["claude-3-5-sonnet", "claude-3-haiku"]

    def test_init_with_invalid_model(self, mocker):
        """Test initialization with invalid model raises error."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }

        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")

        with pytest.raises(ValueError, match="Unsupported model: invalid_model"):
            TestCaseGenerator(api_key="test_key", models=["invalid_model"])

    def test_init_with_missing_config_file(self, mocker):
        """Test initialization with missing config file raises error."""
        mocker.patch("builtins.open", side_effect=FileNotFoundError("File not found"))
        mocker.patch("anthropic.Anthropic")

        with pytest.raises(
            FileNotFoundError, match="Model configuration file not found"
        ):
            TestCaseGenerator(api_key="test_key")

    def test_init_with_invalid_json_config(self, mocker):
        """Test initialization with invalid JSON config raises error."""
        mocker.patch("builtins.open", mock_open(read_data="invalid json"))
        mocker.patch("anthropic.Anthropic")

        with pytest.raises(
            ValueError, match="Invalid JSON in model configuration file"
        ):
            TestCaseGenerator(api_key="test_key")

    def test_init_with_all_options(self, mocker):
        """Test initialization with all options set."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }

        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")

        generator = TestCaseGenerator(
            api_key="test_key",
            models=["claude-3-5-sonnet"],
            include_docstring=True,
            include_ast=True,
            show_prompt=True,
            enable_evaluation=False,
            max_fix_attempts=5,
            verbose_evaluation=False,
            config_path="custom_config.json",
        )

        assert generator.include_docstring == True
        assert generator.include_ast == True
        assert generator.show_prompt == True
        assert generator.enable_evaluation == False
        assert generator.max_fix_attempts == 5
        assert generator.verbose_evaluation == False


class TestDatasetOperations:
    """Test dataset loading and problem selection operations."""

    def create_generator(self, mocker):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key")

    def test_load_dataset_success(self, mocker):
        """Test successful dataset loading."""
        generator = self.create_generator(mocker)

        sample_data = [
            '{"task_id": "HumanEval/0", "prompt": "def has_close_elements(numbers, threshold):", "entry_point": "has_close_elements"}',
            '{"task_id": "HumanEval/1", "prompt": "def separate_paren_groups(paren_string):", "entry_point": "separate_paren_groups"}',
        ]

        mocker.patch("builtins.open", mock_open(read_data="\n".join(sample_data)))

        generator.load_dataset("test_dataset.jsonl")

        assert len(generator.problems) == 2
        assert generator.problems[0]["task_id"] == "HumanEval/0"
        assert generator.problems[1]["task_id"] == "HumanEval/1"

    def test_load_dataset_with_empty_lines(self, mocker):
        """Test dataset loading with empty lines."""
        generator = self.create_generator(mocker)

        sample_data = [
            '{"task_id": "HumanEval/0", "prompt": "def has_close_elements(numbers, threshold):", "entry_point": "has_close_elements"}',
            "",
            '{"task_id": "HumanEval/1", "prompt": "def separate_paren_groups(paren_string):", "entry_point": "separate_paren_groups"}',
            "",
        ]

        mocker.patch("builtins.open", mock_open(read_data="\n".join(sample_data)))

        generator.load_dataset("test_dataset.jsonl")

        assert len(generator.problems) == 2

    def test_select_random_problem(self, mocker):
        """Test random problem selection."""
        generator = self.create_generator(mocker)
        generator.problems = [
            {
                "task_id": "HumanEval/0",
                "prompt": "def test1():",
                "entry_point": "test1",
            },
            {
                "task_id": "HumanEval/1",
                "prompt": "def test2():",
                "entry_point": "test2",
            },
        ]

        mocker.patch("random.choice", return_value=generator.problems[0])

        selected = generator.select_random_problem()
        assert selected["task_id"] == "HumanEval/0"

    def test_generate_for_specific_problem_found(self, mocker):
        """Test generating for specific problem that exists."""
        generator = self.create_generator(mocker)
        generator.problems = [
            {
                "task_id": "HumanEval/0",
                "prompt": "def test1():",
                "entry_point": "test1",
            },
            {
                "task_id": "HumanEval/1",
                "prompt": "def test2():",
                "entry_point": "test2",
            },
        ]

        mock_generate = mocker.patch.object(
            generator,
            "_generate_and_evaluate_test_cases",
            return_value=["test_file.py"],
        )

        result = generator.generate_for_specific_problem("HumanEval/1", "output_dir")

        assert result == ["test_file.py"]
        mock_generate.assert_called_once_with(generator.problems[1], "output_dir")

    def test_generate_for_specific_problem_not_found(self, mocker):
        """Test generating for specific problem that doesn't exist."""
        generator = self.create_generator(mocker)
        generator.problems = [
            {"task_id": "HumanEval/0", "prompt": "def test1():", "entry_point": "test1"}
        ]

        with pytest.raises(
            ValueError, match="Problem HumanEval/999 not found in dataset"
        ):
            generator.generate_for_specific_problem("HumanEval/999", "output_dir")

    def test_generate_for_random_problem_no_problems(self, mocker):
        """Test generating for random problem with no problems loaded."""
        generator = self.create_generator(mocker)
        generator.problems = []

        with pytest.raises(
            ValueError, match="No problems loaded. Call load_dataset\\(\\) first."
        ):
            generator.generate_for_random_problem("output_dir")


class TestPromptGeneration:
    """Test prompt generation methods."""

    def create_generator(self, mocker, **kwargs):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key", **kwargs)

    def test_extract_function_signature_simple(self, mocker):
        """Test extracting simple function signature."""
        generator = self.create_generator(mocker)

        prompt = '''def has_close_elements(numbers, threshold):
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """'''

        signature = generator.extract_function_signature(prompt, "has_close_elements")
        expected = "def has_close_elements(numbers, threshold):"
        assert signature.strip() == expected

    def test_extract_function_signature_multiline(self, mocker):
        """Test extracting multiline function signature."""
        generator = self.create_generator(mocker)

        prompt = '''def complex_function(arg1,
                    arg2,
                    arg3):
    """Docstring here."""'''

        signature = generator.extract_function_signature(prompt, "complex_function")
        lines = signature.split("\n")
        assert lines[0] == "def complex_function(arg1,"
        assert "arg2," in lines[1]
        assert "arg3):" in lines[2]

    def test_generate_prompt_without_docstring(self, mocker):
        """Test prompt generation without docstring."""
        generator = self.create_generator(
            mocker, include_docstring=False, include_ast=False
        )

        problem = {
            "task_id": "HumanEval/0",
            "prompt": '''def has_close_elements(numbers, threshold):
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """''',
            "entry_point": "has_close_elements",
            "canonical_solution": "    return False",
        }

        prompt = generator.generate_prompt(problem)

        assert "Generate pytest test cases" in prompt
        assert "def has_close_elements(numbers, threshold):" in prompt
        assert (
            "Check if in given list" not in prompt
        )  # Docstring should not be included
        assert "return False" in prompt  # Canonical solution should be included
        assert "AST representation" not in prompt

    def test_generate_prompt_with_docstring(self, mocker):
        """Test prompt generation with docstring."""
        generator = self.create_generator(
            mocker, include_docstring=True, include_ast=False
        )

        problem = {
            "task_id": "HumanEval/0",
            "prompt": '''def has_close_elements(numbers, threshold):
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """''',
            "entry_point": "has_close_elements",
            "canonical_solution": "    return False",
        }

        prompt = generator.generate_prompt(problem)

        assert "Generate pytest test cases" in prompt
        assert "Check if in given list" in prompt  # Docstring should be included
        assert "return False" in prompt

    def test_generate_prompt_with_ast(self, mocker):
        """Test prompt generation with AST."""
        generator = self.create_generator(
            mocker, include_docstring=False, include_ast=True
        )

        problem = {
            "task_id": "HumanEval/0",
            "prompt": '''def has_close_elements(numbers, threshold):
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """''',
            "entry_point": "has_close_elements",
            "canonical_solution": "    return False",
        }

        prompt = generator.generate_prompt(problem)

        assert "AST representation of canonical solution" in prompt
        assert "```" in prompt  # AST should be in code blocks

    def test_generate_ast_string_success(self, mocker):
        """Test successful AST string generation."""
        generator = self.create_generator(mocker)

        prompt = "def test_func():"
        canonical_solution = "    return True"

        ast_string = generator.generate_ast_string(
            canonical_solution, prompt, "test_func"
        )

        assert "Module" in ast_string
        assert "FunctionDef" in ast_string

    def test_generate_ast_string_error(self, mocker):
        """Test AST string generation with syntax error."""
        generator = self.create_generator(mocker)

        prompt = "def test_func():"
        canonical_solution = "    return True\n    invalid syntax"

        ast_string = generator.generate_ast_string(
            canonical_solution, prompt, "test_func"
        )

        assert "Error generating AST" in ast_string


class TestCodeCleaning:
    """Test code cleaning and validation functions."""

    def create_generator(self, mocker):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key")

    def test_clean_generated_code_with_markdown(self, mocker):
        """Test cleaning code with markdown blocks."""
        generator = self.create_generator(mocker)

        raw_response = """```python
import pytest

def test_example():
    assert True
```"""

        cleaned = generator.clean_generated_code(raw_response)

        assert "```python" not in cleaned
        assert "```" not in cleaned
        assert "import pytest" in cleaned
        assert "def test_example():" in cleaned

    def test_clean_generated_code_with_explanation(self, mocker):
        """Test cleaning code with explanatory text."""
        generator = self.create_generator(mocker)

        raw_response = """Here's the test code:

import pytest

def test_example():
    assert True
"""

        cleaned = generator.clean_generated_code(raw_response)

        assert "Here's the test code:" not in cleaned
        assert "import pytest" in cleaned
        assert "def test_example():" in cleaned

    def test_clean_generated_code_removes_duplicates(self, mocker):
        """Test cleaning removes duplicate imports."""
        generator = self.create_generator(mocker)

        raw_response = """import pytest
import pytest
from unittest import mock

def test_example():
    assert True
"""

        cleaned = generator.clean_generated_code(raw_response)

        # Count occurrences of 'import pytest'
        import_count = cleaned.count("import pytest")
        assert import_count == 1
        assert "from unittest import mock" in cleaned

    def test_clean_generated_code_syntax_error_fallback(self, mocker):
        """Test fallback when cleaned code has syntax error."""
        generator = self.create_generator(mocker)

        raw_response = """import pytest

def test_example(:  # Syntax error
    assert True
"""

        cleaned = generator.clean_generated_code(raw_response)

        # Should return original response due to syntax error
        assert cleaned == raw_response

    def test_clean_generated_code_no_test_functions(self, mocker):
        """Test when cleaned code has no test functions."""
        generator = self.create_generator(mocker)

        raw_response = """import pytest

def regular_function():
    return True
"""

        cleaned = generator.clean_generated_code(raw_response)

        # Should return original response since no test functions found
        assert cleaned == raw_response


class TestAPIIntegrationAndCosts:
    """Test API integration and cost calculation methods."""

    def create_generator(self, mocker):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key")

    def test_calculate_cost(self, mocker):
        """Test cost calculation."""
        generator = self.create_generator(mocker)

        cost = generator.calculate_cost(1000, 500, "claude-3-5-sonnet")
        expected_cost = (1000 / 1000) * 0.003 + (500 / 1000) * 0.015
        assert cost == expected_cost

    def test_get_usage_stats_initial(self, mocker):
        """Test initial usage statistics."""
        generator = self.create_generator(mocker)

        stats = generator.get_usage_stats()

        assert stats["total_input_tokens"] == 0
        assert stats["total_output_tokens"] == 0
        assert stats["total_tokens"] == 0
        assert stats["total_cost_usd"] == 0.0

    def test_get_usage_stats_with_usage(self, mocker):
        """Test usage statistics after some usage."""
        generator = self.create_generator(mocker)
        generator.total_input_tokens = 1000
        generator.total_output_tokens = 500
        generator.total_cost = 0.01

        stats = generator.get_usage_stats()

        assert stats["total_input_tokens"] == 1000
        assert stats["total_output_tokens"] == 500
        assert stats["total_tokens"] == 1500
        assert stats["total_cost_usd"] == 0.01

    def test_get_model_folder_name(self, mocker):
        """Test getting model folder name."""
        generator = self.create_generator(mocker)

        folder_name = generator.get_model_folder_name("claude-3-5-sonnet")
        assert folder_name == "claude_35_sonnet"

    @patch("anthropic.Anthropic")
    def test_generate_test_cases_success(self, mock_anthropic_class, mocker):
        """Test successful test case generation."""
        # Mock the response
        mock_response = Mock()
        mock_response.content = [
            Mock(text="import pytest\n\ndef test_example():\n    assert True")
        ]
        mock_response.usage = Mock(input_tokens=100, output_tokens=50)

        mock_client = Mock()
        mock_client.messages.create.return_value = mock_response
        mock_anthropic_class.return_value = mock_client

        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))

        generator = TestCaseGenerator(api_key="test_key")

        problem = {
            "task_id": "HumanEval/0",
            "prompt": "def test_func():",
            "entry_point": "test_func",
            "canonical_solution": "    return True",
        }

        result = generator.generate_test_cases(problem, "claude-3-5-sonnet")

        assert "import pytest" in result
        assert "def test_example():" in result
        assert generator.total_input_tokens == 100
        assert generator.total_output_tokens == 50

    @patch("anthropic.Anthropic")
    def test_generate_test_cases_api_error(self, mock_anthropic_class, mocker):
        """Test test case generation with API error."""
        mock_client = Mock()
        mock_client.messages.create.side_effect = Exception("API Error")
        mock_anthropic_class.return_value = mock_client

        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))

        generator = TestCaseGenerator(api_key="test_key")

        problem = {
            "task_id": "HumanEval/0",
            "prompt": "def test_func():",
            "entry_point": "test_func",
            "canonical_solution": "    return True",
        }

        result = generator.generate_test_cases(problem, "claude-3-5-sonnet")

        assert result == ""


class TestFileOperations:
    """Test file operations and statistics tracking."""

    def create_generator(self, mocker):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key")

    def test_save_test_cases(self, mocker):
        """Test saving test cases to file."""
        generator = self.create_generator(mocker)

        # Mock the file operations to focus on the logic
        mock_mkdir = mocker.patch("pathlib.Path.mkdir")
        mock_write_text = mocker.patch("pathlib.Path.write_text")
        mock_open_builtin = mocker.patch("builtins.open", mock_open())

        problem = {
            "task_id": "HumanEval/0",
            "prompt": "def test_func():",
            "canonical_solution": "    return True",
        }

        test_cases = "import pytest\n\ndef test_example():\n    assert True"
        output_dir = "test_output"

        filepath = generator.save_test_cases(
            problem, test_cases, output_dir, "claude-3-5-sonnet"
        )

        # Verify return value structure
        assert filepath is not None
        assert isinstance(filepath, str)
        assert "claude_35_sonnet" in filepath  # Should contain model folder name
        assert "test_humaneval_0.py" in filepath  # Should contain expected filename

        # Verify directory creation was called
        mock_mkdir.assert_called_once_with(exist_ok=True)

        # Verify file writing was attempted
        assert mock_open_builtin.call_count >= 1  # At least one file write (test file)

        # Check that the content includes expected parts
        write_calls = mock_open_builtin.call_args_list
        test_file_call = None
        for call in write_calls:
            if ".py" in str(call[0]) and ".stats.json" not in str(call[0]):
                test_file_call = call
                break

        assert test_file_call is not None

    def test_rename_file_with_result_success(self, mocker):
        """Test renaming file with success result."""
        generator = self.create_generator(mocker)

        with tempfile.TemporaryDirectory() as temp_dir:
            original_file = Path(temp_dir) / "test_original.py"
            original_file.write_text("# Test content")

            new_filepath = generator.rename_file_with_result(str(original_file), True)

            assert "test_original_success.py" in new_filepath
            assert Path(new_filepath).exists()
            assert not original_file.exists()

    def test_rename_file_with_result_failure(self, mocker):
        """Test renaming file with failure result."""
        generator = self.create_generator(mocker)

        with tempfile.TemporaryDirectory() as temp_dir:
            original_file = Path(temp_dir) / "test_original.py"
            original_file.write_text("# Test content")

            new_filepath = generator.rename_file_with_result(str(original_file), False)

            assert "test_original_false.py" in new_filepath
            assert Path(new_filepath).exists()
            assert not original_file.exists()

    def test_update_final_stats(self, mocker):
        """Test updating final statistics."""
        generator = self.create_generator(mocker)
        generator.total_input_tokens = 1000
        generator.total_output_tokens = 500
        generator.total_cost = 0.01

        # Mock file operations
        mock_rename_file = mocker.patch.object(
            generator, "rename_file_with_result", return_value="test_file_success.py"
        )
        mock_open_builtin = mocker.patch("builtins.open", mock_open())
        mock_unlink = mocker.patch("pathlib.Path.unlink")

        problem = {"task_id": "HumanEval/0"}

        final_filepath = generator.update_final_stats(
            "test_file.py", problem, True, 2, 85.5
        )

        # Verify the rename method was called
        mock_rename_file.assert_called_once_with("test_file.py", True)

        # Verify the final filepath matches expected result
        assert final_filepath == "test_file_success.py"

        # Verify file writing was attempted
        assert mock_open_builtin.call_count >= 1

        # Check that get_usage_stats was used (indirectly verify the stats content)
        stats = generator.get_usage_stats()
        assert stats["total_input_tokens"] == 1000
        assert stats["total_output_tokens"] == 500
        assert stats["total_cost_usd"] == 0.01


class TestPytestEvaluation:
    """Test pytest evaluation and fix workflow."""

    def create_generator(self, mocker):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key")

    def test_run_pytest_success(self, mocker):
        """Test successful pytest run."""
        generator = self.create_generator(mocker)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "TOTAL    10    0    100%\n"
        mock_result.stderr = ""

        mocker.patch("subprocess.run", return_value=mock_result)

        success, output, coverage = generator.run_pytest("test_file.py")

        assert success == True
        assert coverage == 100.0
        assert "TOTAL" in output

    def test_run_pytest_failure(self, mocker):
        """Test failed pytest run."""
        generator = self.create_generator(mocker)

        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stdout = "FAILED test_file.py::test_example"
        mock_result.stderr = "AssertionError"

        mocker.patch("subprocess.run", return_value=mock_result)

        success, output, coverage = generator.run_pytest("test_file.py")

        assert success == False
        assert coverage == 0.0
        assert "FAILED" in output
        assert "AssertionError" in output

    def test_run_pytest_timeout(self, mocker):
        """Test pytest run with timeout."""
        generator = self.create_generator(mocker)

        import subprocess

        mocker.patch(
            "subprocess.run", side_effect=subprocess.TimeoutExpired("pytest", 60)
        )

        success, output, coverage = generator.run_pytest("test_file.py")

        assert success == False
        assert coverage == 0.0
        assert "timed out after 60 seconds" in output

    def test_generate_fix_prompt(self, mocker):
        """Test generating fix prompt."""
        generator = self.create_generator(mocker)

        problem = {
            "task_id": "HumanEval/0",
            "prompt": "def test_func():",
            "canonical_solution": "    return True",
        }

        original_code = "import pytest\n\ndef test_broken():\n    assert False"
        error_output = "FAILED test_file.py::test_broken - AssertionError"

        prompt = generator.generate_fix_prompt(original_code, error_output, 1, problem)

        assert "following test code has errors" in prompt
        assert "FUNCTION BEING TESTED" in prompt
        assert "def test_func():" in prompt
        assert "return True" in prompt
        assert "CURRENT TEST CODE WITH ERRORS" in prompt
        assert "import pytest" in prompt
        assert "PYTEST ERROR OUTPUT" in prompt
        assert "AssertionError" in prompt
        assert "attempt 1 of" in prompt

    def test_evaluate_and_fix_tests_disabled(self, mocker):
        """Test evaluation when disabled."""
        generator = self.create_generator(mocker)
        generator.enable_evaluation = False

        success, attempts, coverage = generator.evaluate_and_fix_tests(
            "test_file.py", {}, "claude-3-5-sonnet"
        )

        assert success == True
        assert attempts == 0
        assert coverage == 0.0

    def test_evaluate_and_fix_tests_success_first_try(self, mocker):
        """Test evaluation success on first try."""
        generator = self.create_generator(mocker)

        mocker.patch.object(generator, "run_pytest", return_value=(True, "", 95.0))

        success, attempts, coverage = generator.evaluate_and_fix_tests(
            "test_file.py", {}, "claude-3-5-sonnet"
        )

        assert success == True
        assert attempts == 0  # No fix attempts needed
        assert coverage == 95.0

    def test_evaluate_and_fix_tests_max_attempts(self, mocker):
        """Test evaluation reaching max attempts."""
        generator = self.create_generator(mocker)
        generator.max_fix_attempts = 2

        mocker.patch.object(generator, "run_pytest", return_value=(False, "Error", 0.0))
        mocker.patch.object(generator, "fix_test_cases", return_value="fixed code")

        problem = {
            "task_id": "HumanEval/0",
            "prompt": "def test_func():",
            "canonical_solution": "    return True",
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(
                "# Test cases for HumanEval/0\n# Generated test cases:\nimport pytest"
            )
            test_file = f.name

        try:
            success, attempts, coverage = generator.evaluate_and_fix_tests(
                test_file, problem, "claude-3-5-sonnet"
            )

            assert success == False
            assert attempts == 2
            assert coverage == 0.0
        finally:
            os.unlink(test_file)


class TestErrorHandlingAndEdgeCases:
    """Test error handling and edge cases."""

    def create_generator(self, mocker, **kwargs):
        """Helper to create a generator with mocked config."""
        mock_config = {
            "default_model": "claude-3-5-sonnet",
            "models": {
                "claude-3-5-sonnet": {
                    "api_name": "claude-3-5-sonnet-20241022",
                    "folder_name": "claude_35_sonnet",
                    "pricing": {"input_per_1k": 0.003, "output_per_1k": 0.015},
                }
            },
        }
        mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_config)))
        mocker.patch("anthropic.Anthropic")
        return TestCaseGenerator(api_key="test_key", **kwargs)

    def test_display_prompt_and_confirm_yes(self, mocker):
        """Test prompt confirmation with yes response."""
        generator = self.create_generator(mocker)

        mocker.patch("builtins.input", side_effect=["y"])

        result = generator.display_prompt_and_confirm("Test prompt")
        assert result == True

    def test_display_prompt_and_confirm_no(self, mocker):
        """Test prompt confirmation with no response."""
        generator = self.create_generator(mocker)

        mocker.patch("builtins.input", side_effect=["n"])

        result = generator.display_prompt_and_confirm("Test prompt")
        assert result == False

    def test_display_prompt_and_confirm_quit(self, mocker):
        """Test prompt confirmation with quit response."""
        generator = self.create_generator(mocker)

        mocker.patch("builtins.input", side_effect=["q"])

        result = generator.display_prompt_and_confirm("Test prompt")
        assert result == False

    def test_display_prompt_and_confirm_invalid_then_yes(self, mocker):
        """Test prompt confirmation with invalid then valid response."""
        generator = self.create_generator(mocker)

        mocker.patch("builtins.input", side_effect=["invalid", "yes"])

        result = generator.display_prompt_and_confirm("Test prompt")
        assert result == True

    def test_display_pytest_errors_verbose_enabled(self, mocker):
        """Test displaying pytest errors with verbose enabled."""
        generator = self.create_generator(mocker, verbose_evaluation=True)

        error_output = """
FAILED test_file.py::test_example - AssertionError: assert False
=== FAILURES ===
def test_example():
    assert False
E   AssertionError: assert False
"""

        # This should not raise an exception
        generator.display_pytest_errors(error_output, 1)

    def test_display_pytest_errors_verbose_disabled(self, mocker):
        """Test displaying pytest errors with verbose disabled."""
        generator = self.create_generator(mocker, verbose_evaluation=False)

        error_output = "FAILED test_file.py::test_example - AssertionError"

        # Should return immediately without processing
        generator.display_pytest_errors(error_output, 1)

    def test_display_fix_prompt_verbose_disabled(self, mocker):
        """Test displaying fix prompt with verbose disabled."""
        generator = self.create_generator(mocker, verbose_evaluation=False)

        result = generator.display_fix_prompt("Fix this", 1)
        assert result is None

    def test_display_fix_response_verbose_disabled(self, mocker):
        """Test displaying fix response with verbose disabled."""
        generator = self.create_generator(mocker, verbose_evaluation=False)

        # Should not raise an exception
        generator.display_fix_response("Fixed code", 1)

    def test_extract_function_signature_not_found(self, mocker):
        """Test extracting function signature when not found."""
        generator = self.create_generator(mocker)

        prompt = "Some random text without function definition"

        signature = generator.extract_function_signature(prompt, "nonexistent_func")
        assert signature == ""

    def test_generate_for_random_problem_success(self, mocker):
        """Test successful random problem generation."""
        generator = self.create_generator(mocker)
        generator.problems = [
            {"task_id": "HumanEval/0", "prompt": "def test():", "entry_point": "test"}
        ]

        mocker.patch.object(
            generator, "select_random_problem", return_value=generator.problems[0]
        )
        mocker.patch.object(
            generator,
            "_generate_and_evaluate_test_cases",
            return_value=["test_file.py"],
        )

        result = generator.generate_for_random_problem("output_dir")
        assert result == ["test_file.py"]

    def test_print_model_summary(self, mocker):
        """Test printing model summary."""
        generator = self.create_generator(mocker)

        model_results = {
            "claude-3-5-sonnet": {
                "status": "success",
                "coverage": 95.0,
                "filepath": "test1.py",
            },
            "claude-3-haiku": {
                "status": "evaluation_failed",
                "coverage": 60.0,
                "filepath": "test2.py",
            },
            "claude-opus": {"status": "generation_failed", "filepath": None},
            "claude-instant": {"status": "generated_no_eval", "filepath": "test3.py"},
        }

        # Should not raise an exception
        generator._print_model_summary(model_results)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
