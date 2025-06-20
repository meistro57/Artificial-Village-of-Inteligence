from .base import Agent


class ArtistAgent(Agent):
    def perform_task(self, task: str):
        result = f"Artist {self.name} created art for '{task}'"
        self.remember(task, result)
        return result
