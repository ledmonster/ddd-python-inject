# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class User(object):
    u""" ユーザを表現した Value Object

    :param int user_id: ユーザID
    :param str name: ユーザ名

    コンテキスト内でライフサイクルを管理しないオブジェクトは、
    利用する属性を最低限に絞った上で Entity ではなく Value Object として
    定義するとメンテナンスしやすい。
    """

    def __init__(self, user_id, name):
        assert isinstance(user_id, int)
        assert isinstance(name, str)
        self.__user_id = user_id
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name


class UserService(object):
    u""" ユーザに関連した機能を提供するサービス """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_current_user(self):
        u""" 現在ログイン中のユーザを返す

        :rtype: User
        """
