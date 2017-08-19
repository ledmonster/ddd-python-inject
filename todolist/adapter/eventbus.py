# -*- coding: utf-8 -*-
import logging

from todolist.port.eventbus import EventBus


logger = logging.getLogger(__name__)


class SimpleEventBus(EventBus):
    u""" シンプルなドメインイベントの通知クラス """

    def publish(self, event):
        u""" ドメインイベントを通知する """
        logger.info(event)
