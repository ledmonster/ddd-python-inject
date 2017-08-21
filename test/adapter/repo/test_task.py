# -*- coding: utf-8 -*-
import inject
import pytest

from todolist import testing
from todolist.adapter.repo.task import (
    TaskMemoryRepository, TaskRedisRepository,
)
from todolist.domain_model.task import Task, TaskRepository


class TestTaskRepository(object):
    u""" TaskRepository のテスト """

    @pytest.fixture(
        params=[TaskMemoryRepository, TaskRedisRepository])
    def repo(self, request):
        repo = request.param()
        testing.overwrite_binding(TaskRepository, lambda: repo)
        yield repo
        repo._clear()

    def test_generate_id(self, repo):
        task_id = repo.generate_id()
        assert isinstance(task_id, int)

        next_id = repo.generate_id()
        assert next_id == task_id + 1

    def test_create(self, repo):
        task = Task.create(1, u"タスク1")
        assert isinstance(task, Task)

        stored = repo.get(1, task.task_id)
        assert stored.task_id == task.task_id
        assert stored.name == task.name
        assert stored.status == task.status

    def test_create_and_get_list(self, repo):
        for i in range(10):
            task = Task.create(1, "task{}".format(i))

        task_list = repo.get_list(user_id=1)
        assert len(task_list) == 10

    def test_rename(self, repo):
        task = Task.create(1, u"タスク1")
        assert isinstance(task, Task)

        task.rename(u"タスク名変更")

        stored = repo.get(1, task.task_id)
        assert stored.task_id == task.task_id
        assert stored.name == u"タスク名変更"
