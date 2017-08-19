# -*- coding: utf-8 -*-
import inject

from todolist import testing


def pytest_runtest_setup(item):
    # dependency injection
    inject.clear_and_configure(testing.config)
