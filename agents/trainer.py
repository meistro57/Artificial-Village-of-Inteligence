from __future__ import annotations

from typing import TYPE_CHECKING

from .base import Agent

if TYPE_CHECKING:
    from memory.storage import Memory
    from knowledge_base.local_kb import KnowledgeBase


class TrainerAgent(Agent):
    """Agent that teaches new facts to the knowledge base."""

    def __init__(self, name: str, memory: "Memory", kb: "KnowledgeBase"):
        super().__init__(name, memory)
        self.kb = kb

    def perform_task(self, task: str):
        if self.kb.query(task):
            result = f"Trainer {self.name} already knew '{task}'"
        else:
            self.kb.add_fact(task, f"taught by {self.name}")
            result = f"Trainer {self.name} taught '{task}'"
        self.remember(task, result)
        return result
