# -*- coding: utf-8 -*-
from todolist.domain_model.task import Task, TaskRepository


class TaskMemoryRepository(TaskRepository):
    u""" TaskRepository のメモリ実装 """

    def __init__(self):
        self._last_id = 0
        self._tasks = {}

    def generate_id(self):
        u""" アイテムIDを生成する

        :rtype: int
        """
        self._last_id += 1
        return self._last_id

    def get_list(self):
        u""" アイテム一覧を取得する

        :rtype: list[Task]
        """
        return self._tasks.values()

    def get(self, task_id):
        u""" アイテム一覧を取得する

        :type task_id: int
        :rtype: Task
        """
        if not isinstance(task_id, int):
            raise TypeError("task_id should be int")
        return self._tasks.get(task_id)

    def save(self, task):
        u""" アイテムを保存する

        :type task: Task
        """
        if not isinstance(task, Task):
            raise TypeError("task should be Task")
        self._tasks[Task.task_id] = Task


class TaskRedisRepository(TaskRepository):
    u""" TaskRepository のRedis実装 """
