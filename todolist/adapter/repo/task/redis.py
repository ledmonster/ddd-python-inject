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

    def get(self, task_id):
        u""" タスクを取得する

        :type task_id: int
        :rtype: (Task|None)
        """
        assert isinstance(task_id, int)
        json_str = self._dao.tasks.hget(task_id)
        if json_str is None:
            return None
        value = json.loads(json_str.decode('utf-8'))
        return self._from_dict(value)

    def save(self, task):
        u""" タスクを保存する

        :type task: Task
        """
        assert isinstance(task, Task)
        json_str = json.dumps(self._to_dict(task), ensure_ascii=False)
        self._dao.tasks.hset(task.task_id, json_str)

    def _from_dict(self, value):
        return Task(
            task_id=value['task_id'],
            user_id=value.get('user_id', 1),
            name=value['name'],
            status=TaskStatus(value['status']))

    def _to_dict(self, task):
        return {
            "task_id": task.task_id,
            "user_id": task.user_id,
            "name": task.name,
            "status": task.status.value,
        }

    def _clear(self):
        u""" 全データを削除(テスト用) """
        self._redis_client.flushdb()
