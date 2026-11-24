"""JSON persistence for task records."""

import json
from pathlib import Path


class TaskStorage:
    def __init__(self, path="tasks.json"):
        self.path = Path(path)

    def load(self):
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []
        return data if isinstance(data, list) else []

    def save(self, tasks):
        self.path.write_text(
            json.dumps(tasks, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
