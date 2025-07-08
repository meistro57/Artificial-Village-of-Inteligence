from .base import Agent


class GuardianAgent(Agent):
    banned_keywords = {"harm", "malware", "attack"}

    @classmethod
    def add_banned_keyword(cls, word: str) -> None:
        """Add a new banned keyword to the shared list."""
        cls.banned_keywords.add(word.lower())

    def perform_task(self, task: str):
        if any(bad in task.lower() for bad in self.banned_keywords):
            result = f"Guardian {self.name} blocked unsafe task"
        else:
            result = f"Guardian {self.name} secured '{task}'"
        self.remember(task, result)
        return result
