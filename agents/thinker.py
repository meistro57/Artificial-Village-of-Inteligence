from typing import TYPE_CHECKING

from .base import Agent
from llm.ollama_client import DEFAULT_MODEL, generate_response

if TYPE_CHECKING:
    from memory.storage import Memory


class ThinkerAgent(Agent):
    """Agent that reasons about a task using an LLM via Ollama."""

    def __init__(self, name: str, memory: "Memory", model: str = DEFAULT_MODEL):
        super().__init__(name, memory)
        self.model = model

    def perform_task(self, task: str):
        prompt = f"Please help with the following task: {task}"
        response = generate_response(prompt, model=self.model)
        result = f"Thinker {self.name} says: {response}"
        self.remember(task, result)
        return result
