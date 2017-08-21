# -*- coding: utf-8 -*-
from todolist.domain_model.task import Task, TaskRepository


class TaskMemoryRepository(TaskRepository):
    u""" TaskRepository のメモリ実装 """

    def __init__(self):
        self._last_id = 0
        self._tasks = {}

    def generate_id(self):
        u""" タスクIDを生成する

        :rtype: int
        """
        self._last_id += 1
        return self._last_id

    def get_list(self, user_id):
        u""" タスク一覧を取得する

        :type user_id: int
        :rtype: list[Task]
        """
        assert isinstance(user_id, int)
        if user_id in self._tasks:
            return self._tasks[user_id].values()
        return []

    def get(self, user_id, task_id):
        u""" タスクを取得する

        :type user_id: int
        :type task_id: int
        :rtype: (Task|None)
        """
        assert isinstance(user_id, int)
        assert isinstance(task_id, int)
        if user_id in self._tasks:
            return self._tasks[user_id].get(task_id)
        return None

    def save(self, task):
        u""" タスクを保存する

        :type task: Task
        """
        assert isinstance(task, Task)
        self._tasks.setdefault(task.user_id, {})[task.task_id] = task

    def _clear(self):
        u""" 全データを削除(テスト用) """
        self._tasks = {}
