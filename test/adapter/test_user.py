# -*- coding: utf-8 -*-
from todolist.adapter.user import SimpleUserService
from todolist.domain_model.user import User


def test_simple_user_service():
    service = SimpleUserService()
    user = service.get_current_user()
    assert isinstance(user, User)
