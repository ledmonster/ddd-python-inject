# -*- coding: utf-8 -*-
import logging

from todolist.port.eventbus import EventBus


logger = logging.getLogger(__name__)


class SimpleEventBus(EventBus):
    u""" シンプルなドメインイベントの通知クラス """

    def __init__(self):
        self._listeners = []

    def publish(self, event):
        u""" ドメインイベントを通知する """
        logger.info(event)
        for listener in self._listeners:
            listener(event)

    def register_listener(self, listener):
        u""" ドメインイベントを購読する """
        assert callable(listener)
        self._listeners.append(listener)
