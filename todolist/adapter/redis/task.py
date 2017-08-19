# -*- coding: utf-8 -*-
from __future__ import absolute_import

from gxredis import RedisDao, RedisString, RedisHash


class TaskDao(RedisDao):
    u""" Task 用の DAO """
    counter = RedisString("todolist:task:counter")
    tasks = RedisHash("todolist:task:tasks")
