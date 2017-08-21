# -*- coding: utf-8 -*-
from __future__ import absolute_import

from gxredis import RedisDao, RedisString, RedisHash, RedisSet


class TaskDao(RedisDao):
    u""" Task 用の DAO """
    # task_id を管理する
    counter = RedisString("todolist:task:counter")

    # task の一覧をハッシュで保存
    tasks = RedisHash("todolist:task:tasks")

    # todo タスクの task_id 一覧
    todo = RedisSet("todolist:task:todo")

    # done タスクの task_id 一覧
    done = RedisSet("todolist:task:done")
