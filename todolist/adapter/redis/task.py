# -*- coding: utf-8 -*-
from __future__ import absolute_import

from gxredis import RedisDao, RedisString, RedisHash, RedisSet


class TaskDao(RedisDao):
    u""" Task 用の DAO """
    # task_id を管理する
    counter = RedisString("todolist:task:counter")

    # タスクの一覧(ハッシュ)
    tasks = RedisHash("todolist:task:tasks")

    # ユーザのタスクの task_id 一覧
    user_tasks = RedisSet("todolist:task:{user_id}:tasks")

    # ユーザの todo タスクの task_id 一覧
    todo = RedisSet("todolist:task:{user_id}:todo")

    # ユーザの done タスクの task_id 一覧
    done = RedisSet("todolist:task:{user_id}:done")
