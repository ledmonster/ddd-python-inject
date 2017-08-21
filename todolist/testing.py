# -*- coding: utf-8 -*-
import inject
import redis

from todolist.adapter.eventbus import SimpleEventBus
from todolist.adapter.repo.task import TaskMemoryRepository
from todolist.adapter.user import SimpleUserService
from todolist.domain_model.task import TaskRepository
from todolist.domain_model.user import UserService
from todolist.port.eventbus import EventBus


def config(binder):
    binder.bind(redis.StrictRedis, redis.StrictRedis("localhost", 6379, 14))
    binder.bind_to_constructor(EventBus, SimpleEventBus)
    binder.bind_to_constructor(TaskRepository, TaskMemoryRepository)
    binder.bind_to_constructor(UserService, SimpleUserService)


def overwrite_binding(key, constructor):
    injector = inject.get_injector()
    injector._bindings[key] = constructor
