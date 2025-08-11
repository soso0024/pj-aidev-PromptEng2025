"""
Ollama client wrapper that mimics the Anthropic API interface for compatibility.
"""

import json
import requests
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class Usage:
    """Token usage information."""

    input_tokens: int
    output_tokens: int


@dataclass
class MessageContent:
    """Message content."""

    text: str


@dataclass
class Message:
    """Response message."""

    content: List[MessageContent]
    usage: Usage


class Messages:
    """Messages API wrapper for Ollama."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/generate"

    def create(
        self,
        model: str,
        messages: List[Dict[str, str]],
        max_tokens: int = 2000,
        temperature: float = 0.0,
        **kwargs,
    ) -> Message:
        """Create a completion using Ollama API.

        Args:
            model: The model name to use (e.g., "llama2", "mistral", etc.)
            messages: List of message dictionaries with 'role' and 'content'
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            **kwargs: Additional parameters (ignored for compatibility)

        Returns:
            Message object with content and usage information
        """
        # Convert messages to a single prompt
        # Ollama expects a simple prompt string, not chat messages
        prompt = self._convert_messages_to_prompt(messages)

        # Prepare the request payload
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }

        try:
            # Make the request to Ollama
            response = requests.post(self.api_endpoint, json=payload)
            response.raise_for_status()

            data = response.json()

            # Extract the generated text
            generated_text = data.get("response", "")

            # Remove thinking tags if present (common in some models like deepseek-r1)
            if "<think>" in generated_text and "</think>" in generated_text:
                # Extract content after </think>
                parts = generated_text.split("</think>")
                if len(parts) > 1:
                    generated_text = parts[1].strip()

            # Token counting for Ollama (simplified since it's free)
            # We just return 0 for both since Ollama is free and we don't need accurate counts
            usage = Usage(
                input_tokens=0,
                output_tokens=0
            )

            content = [MessageContent(text=generated_text)]

            return Message(content=content, usage=usage)

        except requests.exceptions.RequestException as e:
            raise Exception(f"Ollama API request failed: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse Ollama response: {str(e)}")
    
    def _convert_messages_to_prompt(self, messages: List[Dict[str, str]]) -> str:
        """Convert chat messages to a single prompt string."""
        prompt_parts = []
        
        for message in messages:
            role = message.get("role")
            content = message.get("content", "")
            
            if role and content:
                # Include role information for better context
                if role == "system":
                    prompt_parts.append(f"System: {content}")
                elif role == "user":
                    prompt_parts.append(f"Human: {content}")
                elif role == "assistant":
                    prompt_parts.append(f"Assistant: {content}")
        
        if not prompt_parts:
            return ""
        
        # Join all messages with newlines for context
        full_prompt = "\n\n".join(prompt_parts)
        
        # Add a final prompt indicator if the last message was from user
        if messages and messages[-1].get("role") == "user":
            full_prompt += "\n\nAssistant:"
        
        return full_prompt


class Ollama:
    """Ollama client that mimics Anthropic's interface."""

    def __init__(self, base_url: str = "http://localhost:11434"):
        """Initialize Ollama client.

        Args:
            base_url: Base URL for Ollama API (default: http://localhost:11434)
        """
        self.base_url = base_url
        self.messages = Messages(base_url)
        
    def test_connection(self) -> bool:
        """Test if Ollama server is accessible."""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
    
    def list_models(self) -> List[str]:
        """List available models on the Ollama server."""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            response.raise_for_status()
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            return []
