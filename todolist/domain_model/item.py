# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

import inject
from enum import Enum


class ItemStatus(Enum):
    u""" アイテムステータス """
    todo = "todo"
    done = "done"


class Item(object):
    u""" アイテム

    :param int item_id: アイテムID
    :param (str|unicode) name: アイテム名
    :param ItemStatus status: ステータス
    """

    def __init__(self, item_id, name, status):
        u""" コンストラクタ

        :param int item_id: アイテムID
        :param (str|unicode) name: アイテム名
        :param ItemStatus status: ステータス

        新規のアイテムを作成する際には create メソッドを利用すること
        """
        assert isinstance(item_id, int)
        assert isinstance(name, basestring)
        assert isinstance(status, ItemStatus)
        self._item_id = item_id
        self._name = name
        self._status = status

    @classmethod
    def create(cls, name):
        u""" アイテムを生成する

        :type name: str|unicode
        :type status: ItemStatus
        :rtype: Item
        """
        repo = inject.instance(ItemRepository)
        item_id = repo.generate_id()
        return cls(item_id, name, ItemStatus.todo)

    @property
    def item_id(self):
        return self._item_id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    def done(self):
        u""" タスクを終了させる """
        self._status = ItemStatus.done


class ItemRepository(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_id(self):
        u""" アイテムIDを生成する

        :rtype: int
        """

    @abstractmethod
    def get_list(self):
        u""" アイテム一覧を取得する

        :rtype: list[Item]
        """

    @abstractmethod
    def get(self, item_id):
        u""" アイテム一覧を取得する

        :type item_id: int
        :rtype: Item
        """

    @abstractmethod
    def save(self, item):
        u""" アイテムを保存する

        :type item: Item
        """
