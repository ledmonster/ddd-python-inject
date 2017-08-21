# -*- coding: utf-8 -*-
import time

import inject
import pytest
import redis

from todolist import testing
from todolist.app.read_model.updater import register_readmodel_updater
from todolist.adapter.repo.task import TaskRedisRepository
from todolist.domain_model.task import Task, TaskRepository
from todolist.read_model.task import TaskQuery


class TestTaskQuery(object):
    u""" TaskQuery のテスト """

    def setup(self):
        register_readmodel_updater()

    def teardown(self):
        redis_client = inject.instance(redis.StrictRedis)
        redis_client.flushdb()

    @pytest.fixture
    def repo(self):
        repo = TaskRedisRepository()
        testing.overwrite_binding(TaskRepository, lambda: repo)
        return repo

    @pytest.fixture
    def query(self):
        return TaskQuery()

    def test_find_by_user_id(self, repo, query):
        for i in range(10):
            task = Task.create(1, "task{}".format(i))

        task_list = query.find_by_user_id(user_id=1)
        assert len(task_list) == 10

    def test_two_users(self, repo, query):
        for i in range(10):
            task = Task.create(1, "task{}".format(i))
        for i in range(20):
            task = Task.create(2, "task{}".format(i))

        task_list = query.find_all()
        assert len(task_list) == 30
        task_list = query.find_by_user_id(user_id=1)
        assert len(task_list) == 10
        task_list = query.find_by_user_id(user_id=2)
        assert len(task_list) == 20

    def test_find_todo_and_done_by_user_id(self, repo, query):
        tasks = []
        for i in range(10):
            tasks.append(Task.create(1, "task{}".format(i)))
        tasks[0].done()

        # redis が更新されるのを待つ
        for i in range(10):
            todo_list = query.find_todo_by_user_id(user_id=1)
            if len(todo_list) == 9:
                break
            time.sleep(0.01)
        else:
            assert False

        task_list = query.find_by_user_id(user_id=1)
        assert len(task_list) == 10
        done_list = query.find_done_by_user_id(user_id=1)
        assert len(done_list) == 1
