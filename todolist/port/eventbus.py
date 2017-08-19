# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class EventBus(object):
    u""" ドメインイベントの通知インタフェース """

    __metaclass__ = ABCMeta

    @abstractmethod
    def publish(self, event):
        u""" ドメインイベントを通知する """
