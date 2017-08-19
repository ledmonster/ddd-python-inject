# -*- coding: utf-8 -*-
import redis

from todolist.domain_model.task import TaskRepository
from todolist.adapter.repo.task import TaskMemoryRepository


def config(binder):
    binder.bind(redis.StrictRedis, redis.StrictRedis("localhost", 6379, 14))
    binder.bind(TaskRepository, TaskMemoryRepository())
