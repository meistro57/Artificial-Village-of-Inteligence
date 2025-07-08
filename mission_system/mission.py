from typing import Any, Callable, List, Optional


class Mission:
    def __init__(self, tasks: List[str], on_complete: Callable[[str, Any], None] | None = None):
        self.tasks = tasks
        self.completed = []
        self.on_complete = on_complete

    def next_task(self) -> Optional[str]:
        if not self.tasks:
            return None
        return self.tasks.pop(0)

    def complete_task(self, task: str, result: Any) -> None:
        self.completed.append((task, result))
        if self.on_complete:
            self.on_complete(task, result)

    def is_finished(self) -> bool:
        return not self.tasks

    def progress_summary(self) -> str:
        """Return a human readable summary of mission progress."""
        total = len(self.completed) + len(self.tasks)
        completed = len(self.completed)
        return f"{completed}/{total} tasks completed"

    def get_remaining_tasks(self) -> List[str]:
        """Return a copy of the remaining tasks."""
        return list(self.tasks)
