from agents.base import Agent


class EchoAgent(Agent):
    """Simple plugin agent that echoes tasks."""

    def perform_task(self, task: str):
        result = f"Echo {self.name}: {task}"
        self.remember(task, result)
        return result
