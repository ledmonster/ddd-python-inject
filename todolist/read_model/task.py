# -*- coding: utf-8 -*-
u""" 読み出し用のモデル (DTO: Data Transfer Object) """


class TaskDto(object):
    u""" 読み出し用のタスク """

    def __init__(self, task_id, user_id, name, status):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name
        self.status = status
