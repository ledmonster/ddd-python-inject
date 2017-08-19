# -*- coding: utf-8 -*-
from todolist.domain_model.task import TaskRepository
from todolist.adapter.repo.task import TaskMemoryRepository


def config(binder):
    binder.bind(TaskRepository, TaskMemoryRepository())
