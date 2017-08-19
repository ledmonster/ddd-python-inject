# -*- coding: utf-8 -*-
from todolist.domain_model.item import Item, ItemStatus


def test_create():
    item = Item.create(u'PyConJP の資料を作る')
    assert isinstance(item, Item)
    assert item.name == u'PyConJP の資料を作る'
    assert item.status == ItemStatus.todo


def test_done():
    item = Item.create(u'PyConJP の資料を作る')
    item.done()
