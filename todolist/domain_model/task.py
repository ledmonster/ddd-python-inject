# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

import inject
from enum import Enum

from todolist.port.eventbus import EventBus


class TaskStatus(Enum):
    u""" タスクステータス """
    todo = "todo"
    done = "done"


class TaskCreated(object):
    u""" タスク作成イベント """
    def __init__(self, task_id, user_id, name):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id)


class TaskDone(object):
    u""" タスク完了イベント """
    def __init__(self, task_id, user_id):
        self.task_id = task_id
        self.user_id = user_id

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id)


class TaskRenamed(object):
    u""" タスク名変更イベント """
    def __init__(self, task_id, user_id, name):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id)


class TaskRepository(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_id(self):
        u""" タスクIDを生成する

        :rtype: int
        """

    @abstractmethod
    def get(self, user_id, task_id):
        u""" タスクを取得する

        :type user_id: int
        :type task_id: int
        :rtype: (Task|None)
        """

    @abstractmethod
    def save(self, task):
        u""" タスクを保存する

        :type task: Task
        """


class Task(object):
    u""" タスク

    :param int task_id: タスクID
    :param int user_id: ユーザID
    :param (str|unicode) name: タスク名
    :param TaskStatus status: ステータス
    """
    _eventbus = inject.attr(EventBus)
    _repo = inject.attr(TaskRepository)

    def __init__(self, task_id, user_id, name, status):
        u""" コンストラクタ

        :param int task_id: タスクID
        :param int user_id: ユーザID
        :param (str|unicode) name: タスク名
        :param TaskStatus status: ステータス

        新規のタスクを作成する際には create メソッドを利用すること
        """
        assert isinstance(task_id, int)
        assert isinstance(user_id, int)
        assert isinstance(name, basestring)
        assert isinstance(status, TaskStatus)
        self._task_id = task_id
        self._user_id = user_id
        self._name = name
        self._status = status

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id)

    @classmethod
    def create(cls, user_id, name):
        u""" タスクを生成する

        :type user_id: int
        :type name: str|unicode
        :rtype: Task
        """
        repo = inject.instance(TaskRepository)
        eventbus = inject.instance(EventBus)

        # タスクを生成して保存する
        task_id = repo.generate_id()
        task = cls(task_id, user_id, name, TaskStatus.todo)
        repo.save(task)

        # タスク生成イベントを通知する
        event = TaskCreated(task_id, user_id, name)
        eventbus.publish(event)
        return task

    @property
    def task_id(self):
        return self._task_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    def rename(self, name):
        u""" タスク名を変更する """
        self._name = name
        self._repo.save(self)

        # 名前の変更を通知する
        event = TaskRenamed(self.task_id, self._user_id, self.name)
        self._eventbus.publish(event)

    def done(self):
        u""" タスクを終了させる """
        self._status = TaskStatus.done
        self._repo.save(self)

        # タスクの終了を通知する
        event = TaskDone(self.task_id, self.user_id)
        self._eventbus.publish(event)
