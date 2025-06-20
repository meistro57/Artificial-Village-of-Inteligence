from .base import Agent


class BuilderAgent(Agent):
    def perform_task(self, task: str):
        # Very simple implementation
        result = f"Builder {self.name} executed '{task}'"
        self.remember(task, result)
        return result
