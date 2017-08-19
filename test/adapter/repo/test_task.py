# -*- coding: utf-8 -*-
import pytest

from todolist.adapter.repo.task import (
    TaskMemoryRepository, TaskRedisRepository,
)
from todolist.domain_model.task import Task


class TestTaskRepository(object):
    u""" TaskRepository のテスト """

    @pytest.fixture(
        params=[TaskMemoryRepository, TaskRedisRepository])
    def repo(self, request):
        repo = request.param()
        yield repo
        repo._clear()

    def test_generate_id(self, repo):
        task_id = repo.generate_id()
        assert isinstance(task_id, int)

        next_id = repo.generate_id()
        assert next_id == task_id + 1

    def test_create_and_save(self, repo):
        task = Task.create(u"タスク1", repo)
        assert isinstance(task, Task)
        repo.save(task)

        stored = repo.get(task.task_id)
        assert stored.task_id == task.task_id
        assert stored.name == task.name
        assert stored.status == task.status

    def test_create_and_get_list(self, repo):
        for i in range(10):
            task = Task.create("task{}".format(i), repo)
            repo.save(task)

        task_list = repo.get_list()
        assert len(task_list) == 10

    def test_rename(self, repo):
        task = Task.create(u"タスク1", repo)
        assert isinstance(task, Task)
        repo.save(task)

        task.rename(u"タスク名変更")
        repo.save(task)

        stored = repo.get(task.task_id)
        assert stored.task_id == task.task_id
        assert stored.name == u"タスク名変更"
