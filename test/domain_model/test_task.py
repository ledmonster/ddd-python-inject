# -*- coding: utf-8 -*-
from todolist.domain_model.task import Task, TaskStatus


def test_create():
    task = Task.create(u'PyConJP の資料を作る')
    assert isinstance(task, Task)
    assert task.name == u'PyConJP の資料を作る'
    assert task.status == TaskStatus.todo


def test_done():
    task = Task.create(u'PyConJP の資料を作る')
    task.done()
