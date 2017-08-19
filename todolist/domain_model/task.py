# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

import inject
from enum import Enum


class TaskStatus(Enum):
    u""" アイテムステータス """
    todo = "todo"
    done = "done"


class Task(object):
    u""" アイテム

    :param int task_id: アイテムID
    :param (str|unicode) name: アイテム名
    :param TaskStatus status: ステータス
    """

    def __init__(self, task_id, name, status):
        u""" コンストラクタ

        :param int task_id: アイテムID
        :param (str|unicode) name: アイテム名
        :param TaskStatus status: ステータス

        新規のアイテムを作成する際には create メソッドを利用すること
        """
        assert isinstance(task_id, int)
        assert isinstance(name, basestring)
        assert isinstance(status, TaskStatus)
        self._task_id = task_id
        self._name = name
        self._status = status

    @classmethod
    def create(cls, name):
        u""" アイテムを生成する

        :type name: str|unicode
        :type status: TaskStatus
        :rtype: Task
        """
        repo = inject.instance(TaskRepository)
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

    def done(self):
        u""" タスクを終了させる """
        self._status = TaskStatus.done


class TaskRepository(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_id(self):
        u""" アイテムIDを生成する

        :rtype: int
        """

    @abstractmethod
    def get_list(self):
        u""" アイテム一覧を取得する

        :rtype: list[Task]
        """

    @abstractmethod
    def get(self, task_id):
        u""" アイテム一覧を取得する

        :type task_id: int
        :rtype: Task
        """

    @abstractmethod
    def save(self, task):
        u""" アイテムを保存する

        :type task: Task
        """
