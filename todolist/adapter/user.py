# -*- coding: utf-8 -*-
from todolist.domain_model.user import User, UserService


class SimpleUserService(UserService):

    def get_current_user(self):
        u""" 現在ログイン中のユーザを返す

        :rtype: User
        """
        # 常に junya を返す
        return User(1, "junya")
