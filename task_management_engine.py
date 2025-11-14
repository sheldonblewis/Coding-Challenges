import json
from simple_task_management_system import SimpleTaskManagementSystem


class SimpleTaskManagementSystemImpl(SimpleTaskManagementSystem):

    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        self.users = {}
        self.task_versions = {}
        self.user_backups = {}

    def add_task(self, name: str, priority: int) -> str:
        task_id = f"task_id_{self.next_id}"
        self.tasks[task_id] = {"name": name, "priority": priority}
        self.task_versions[task_id] = [
            {"name": name, "priority": priority, "version": 0}
        ]
        self.next_id += 1
        return task_id

    def update_task(self, task_id: str, name: str, priority: int) -> bool:
        if task_id not in self.tasks:
            return False
        self.tasks[task_id]["name"] = name
        self.tasks[task_id]["priority"] = priority
        v = len(self.task_versions[task_id])
        self.task_versions[task_id].append(
            {"name": name, "priority": priority, "version": v}
        )
        return True

    def get_task(self, task_id: str) -> str | None:
        if task_id not in self.tasks:
            return None
        return json.dumps(self.tasks[task_id])

    def _creation_index(self, task_id: str) -> int:
        return int(task_id.split("_")[-1])

    def search_tasks(self, name_filter: str, max_results: int) -> list[str]:
        if max_results <= 0:
            return []
        ids = [tid for tid, d in self.tasks.items() if name_filter in d["name"]]
        ids.sort(key=lambda tid: (-self.tasks[tid]["priority"], self._creation_index(tid)))
        return ids[:max_results]

    def list_tasks_sorted(self, limit: int) -> list[str]:
        if limit <= 0:
            return []
        ids = list(self.tasks.keys())
        ids.sort(key=lambda tid: (-self.tasks[tid]["priority"], self._creation_index(tid)))
        return ids[:limit]

    def add_user(self, user_id: str, quota: int) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = {"quota": quota, "assignments": []}
        return True

    def assign_task(self, task_id: str, user_id: str, deadline: int) -> bool:
        if task_id not in self.tasks or user_id not in self.users:
            return False
        user = self.users[user_id]
        if len(user["assignments"]) >= user["quota"]:
            return False
        user["assignments"].append((task_id, deadline))
        return True

    def get_user_tasks(self, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []
        a = self.users[user_id]["assignments"]
        a.sort(key=lambda x: (x[1], self._creation_index(x[0])))
        return [t for t, _ in a]

    def view_task_versions(self, task_id: str) -> list[str]:
        if task_id not in self.task_versions:
            return []
        return [json.dumps(v) for v in self.task_versions[task_id]]

    def backup_user_tasks(self, user_id: str) -> int | None:
        if user_id not in self.users:
            return None
        assignments = self.users[user_id]["assignments"]
        self.user_backups[user_id] = assignments.copy()
        return len(assignments)

    def restore_user_tasks(self, user_id: str) -> int | None:
        if user_id not in self.users:
            return None
        if user_id not in self.user_backups:
            return 0
        backup = self.user_backups[user_id]
        quota = self.users[user_id]["quota"]
        if len(backup) > quota:
            restored = backup[:quota]
        else:
            restored = backup.copy()
        self.users[user_id]["assignments"] = restored
        return len(restored)
