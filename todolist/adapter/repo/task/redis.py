# -*- coding: utf-8 -*-
from __future__ import absolute_import

import inject
import json
import redis

from todolist.adapter.redis.task import TaskDao
from todolist.domain_model.task import Task, TaskStatus, TaskRepository


class TaskRedisRepository(TaskRepository):
    u""" TaskRepository のRedis実装 """

    _redis_client = inject.attr(redis.StrictRedis)

    def __init__(self):
        self._dao = TaskDao(self._redis_client)

    def generate_id(self):
        u""" タスクIDを生成する

        :rtype: int
        """
        return self._dao.counter.incr()

    def get_list(self):
        u""" タスク一覧を取得する

        :rtype: list[Task]
        """
        tasks = []
        json_strs = self._dao.tasks.hgetall()
        values = [json.loads(x.decode('utf-8')) for x in json_strs.values()]
        return [self._from_dict(x) for x in values]

    def get(self, task_id):
        u""" タスク一覧を取得する

        :type task_id: int
        :rtype: (Task|None)
        """
        if not isinstance(task_id, int):
            raise TypeError("task_id should be int")
        json_str = self._dao.tasks.hget(task_id)
        if json_str is None:
            return None
        value = json.loads(json_str.decode('utf-8'))
        return self._from_dict(value)

    def save(self, task):
        u""" タスクを保存する

        :type task: Task
        """
        if not isinstance(task, Task):
            raise TypeError("task should be Task")
        json_str = json.dumps(self._to_dict(task), ensure_ascii=False)
        self._dao.tasks.hset(task.task_id, json_str)

    def _from_dict(self, value):
        return Task(
            value['task_id'], value['name'], TaskStatus(value['status']))

    def _to_dict(self, task):
        return {
            "task_id": task.task_id,
            "name": task.name,
            "status": task.status.value,
        }

    def _clear(self):
        u""" 全データを削除(テスト用) """
        self._dao.counter.delete()
        self._dao.tasks.delete()
