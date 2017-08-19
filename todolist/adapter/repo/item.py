# -*- coding: utf-8 -*-
from todolist.domain_model.item import Item, ItemRepository


class ItemMemoryRepository(ItemRepository):
    u""" ItemRepository のメモリ実装 """

    def __init__(self):
        self._last_id = 0
        self._items = {}

    def generate_id(self):
        u""" アイテムIDを生成する

        :rtype: int
        """
        self._last_id += 1
        return self._last_id

    def get_list(self):
        u""" アイテム一覧を取得する

        :rtype: list[Item]
        """
        return self._items.values()

    def get(self, item_id):
        u""" アイテム一覧を取得する

        :type item_id: int
        :rtype: Item
        """
        if not isinstance(item_id, int):
            raise TypeError("item_id should be int")
        return self._items.get(item_id)

    def save(self, item):
        u""" アイテムを保存する

        :type item: Item
        """
        if not isinstance(item, Item):
            raise TypeError("item should be Item")
        self._items[Item.item_id] = Item


class ItemRedisRepository(ItemRepository):
    u""" ItemRepository のRedis実装 """
