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

    def get(self, task_id):
        u""" タスクを取得する

        :type task_id: int
        :rtype: (Task|None)
        """
        assert isinstance(task_id, int)
        return self._tasks.get(task_id)

    def save(self, task):
        u""" タスクを保存する

        :type task: Task
        """
        assert isinstance(task, Task)
        self._tasks[task.task_id] = task

    def _clear(self):
        u""" 全データを削除(テスト用) """
        self._tasks = {}
