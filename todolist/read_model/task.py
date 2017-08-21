# -*- coding: utf-8 -*-
u""" 読み出し用のモデル (DTO: Data Transfer Object) """
import inject
import json
import redis

from todolist.adapter.redis.task import TaskDao
from todolist.domain_model.task import TaskStatus


class TaskDto(object):
    u""" 読み出し用のタスク """

    def __init__(self, task_id, user_id, name, status):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name
        self.status = status


class TaskQuery(object):
    u""" タスク用の Query クラス """

    _redis_client = inject.attr(redis.StrictRedis)

    def __init__(self):
        self._dao = TaskDao(self._redis_client)

    def find_by_user_id(self, user_id):
        u""" ユーザのタスク一覧を取得する

        :type user_id: int
        :rtype: list[TaskDto]
        """
        assert isinstance(user_id, int)
        tasks = []
        json_strs = self._dao.tasks(user_id=user_id).hgetall()
        values = [json.loads(x.decode('utf-8')) for x in json_strs.values()]
        return [self._from_dict(x) for x in values]

    def find_todo_by_user_id(self, user_id):
        u""" ユーザの未完了タスク一覧を取得する

        :type user_id: int
        :rtype: list[TaskDto]
        """
        assert isinstance(user_id, int)
        keys = self._dao.todo(user_id=user_id).smembers()
        tasks = []
        if not keys:
            return []
        json_strs = self._dao.tasks(user_id=user_id).hmget(*keys)
        values = [json.loads(x.decode('utf-8')) for x in json_strs]
        return [self._from_dict(x) for x in values]

    def find_done_by_user_id(self, user_id):
        u""" ユーザの完了タスク一覧を取得する

        :type user_id: int
        :rtype: list[TaskDto]
        """
        assert isinstance(user_id, int)
        keys = self._dao.done(user_id=user_id).smembers()
        tasks = []
        if not keys:
            return []
        json_strs = self._dao.tasks(user_id=user_id).hmget(*keys)
        values = [json.loads(x.decode('utf-8')) for x in json_strs]
        return [self._from_dict(x) for x in values]

    def _from_dict(self, value):
        return TaskDto(
            task_id=value['task_id'],
            user_id=value.get('user_id', 1),
            name=value['name'],
            status=TaskStatus(value['status']))
