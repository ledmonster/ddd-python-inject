# -*- coding: utf-8 -*-
u""" Dependency Injection 用の設定関数を提供するモジュール """
import inject
import redis

from todolist.adapter.eventbus import SimpleEventBus
from todolist.adapter.repo.task import TaskRedisRepository
from todolist.domain_model.task import TaskRepository
from todolist.port.eventbus import EventBus


def create_config(params):
    u""" inject 用の config を生成する

    :param dict params: パラメータの辞書
    :return function: inject 用の config 関数
    """
    def config(binder):
        binder.bind(redis.StrictRedis, redis.StrictRedis(
            params['redis_host'], params['redis_port'], params['redis_db']))
        binder.bind_to_constructor(EventBus, SimpleEventBus)
        binder.bind_to_constructor(TaskRepository, TaskRedisRepository)
    return config
