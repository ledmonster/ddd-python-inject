# -*- coding: utf-8 -*-
from todolist.domain_model.item import ItemRepository
from todolist.adapter.repo.item import ItemMemoryRepository


def config(binder):
    binder.bind(ItemRepository, ItemMemoryRepository())
