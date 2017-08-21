# -*- coding: utf-8 -*-
import inject
import redis

from todolist.adapter.redis.task import TaskDao
from todolist.domain_model.task import TaskCreated, TaskDone
from todolist.port.eventbus import EventBus


def register_readmodel_updater():
    eventbus = inject.instance(EventBus)
    eventbus.register_listener(update_readmodel)


def update_readmodel(event):
    u""" ドメインイベントを入力として ReadModel を更新する """
    redis_client = inject.instance(redis.StrictRedis)
    dao = TaskDao(redis_client)
    if isinstance(event, TaskCreated):
        dao.user_tasks(user_id=event.user_id).sadd(event.task_id)
        dao.todo(user_id=event.user_id).sadd(event.task_id)
    elif isinstance(event, TaskDone):
        dao.done(user_id=event.user_id).sadd(event.task_id)
        dao.todo(user_id=event.user_id).srem(event.task_id)
