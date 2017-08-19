# -*- coding: utf-8 -*-
from todolist.domain_model.task import Task, TaskStatus


def test_create():
    task = Task.create(u'PyConJP の資料を作る')
    assert isinstance(task, Task)
    assert task.name == u'PyConJP の資料を作る'
    assert task.status == TaskStatus.todo


def test_rename():
    task = Task.create(u'PyConJP の資料を作る')
    task.rename(u'PyConJP のスライドを作る')
    assert task.name == u'PyConJP のスライドを作る'


def test_done():
    task = Task.create(u'PyConJP の資料を作る')
    task.done()
    assert task.status == TaskStatus.done
