# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

import inject
from enum import Enum


class TaskStatus(Enum):
    u""" タスクステータス """
    todo = "todo"
    done = "done"


class Task(object):
    u""" タスク

    :param int task_id: タスクID
    :param (str|unicode) name: タスク名
    :param TaskStatus status: ステータス
    """

    def __init__(self, task_id, name, status):
        u""" コンストラクタ

        :param int task_id: タスクID
        :param (str|unicode) name: タスク名
        :param TaskStatus status: ステータス

        新規のタスクを作成する際には create メソッドを利用すること
        """
        assert isinstance(task_id, int)
        assert isinstance(name, basestring)
        assert isinstance(status, TaskStatus)
        self._task_id = task_id
        self._name = name
        self._status = status

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id)

    @classmethod
    def create(cls, name, repo=None):
        u""" タスクを生成する

        :type name: str|unicode
        :type status: TaskStatus
        :rtype: Task
        """
        repo = repo or inject.instance(TaskRepository)
        task_id = repo.generate_id()
        return cls(task_id, name, TaskStatus.todo)

    @property
    def task_id(self):
        return self._task_id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    def rename(self, name):
        u""" タスク名を変更する """
        self._name = name

    def done(self):
        u""" タスクを終了させる """
        self._status = TaskStatus.done


class TaskRepository(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_id(self):
        u""" タスクIDを生成する

        :rtype: int
        """

    @abstractmethod
    def get_list(self):
        u""" タスク一覧を取得する

        :rtype: list[Task]
        """

    @abstractmethod
    def get(self, task_id):
        u""" タスク一覧を取得する

        :type task_id: int
        :rtype: (Task|None)
        """

    @abstractmethod
    def save(self, task):
        u""" タスクを保存する

        :type task: Task
        """
