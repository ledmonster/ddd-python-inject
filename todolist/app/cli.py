# -*- coding: utf-8 -*-
u""" CLI インタフェース """
import logging

import click
import inject

from .config import create_config
from .read_model.updater import register_readmodel_updater
from todolist.domain_model.task import Task, TaskStatus, TaskRepository


logging.basicConfig(level=logging.INFO)


@click.group()
def main():
    params = {
        "redis_host": "localhost",
        "redis_port": "6379",
        "redis_db": "2",
    }
    inject.configure(create_config(params))
    register_readmodel_updater()


@main.command()
def list():
    repo = inject.instance(TaskRepository)
    tasks = repo.get_list()
    for task in tasks:
        if task.status is TaskStatus.todo:
            click.echo(u"[ ] #{}: {}".format(task.task_id, task.name))
        else:
            click.echo(u"[x] #{}: {}".format(task.task_id, task.name))


@main.command()
@click.option("--name", type=unicode, help="task name", prompt="task name")
def add(name):
    repo = inject.instance(TaskRepository)
    task = Task.create(name)
    repo.save(task)
    click.echo(u"#{}: {}".format(task.task_id, task.name))


@main.command()
@click.argument("task_id", type=int)
def done(task_id):
    repo = inject.instance(TaskRepository)
    task = repo.get(task_id)
    if task is None:
        click.echo("task not found: #{}".format(task_id))
    elif task.status is TaskStatus.todo:
        task.done()
        repo.save(task)
    click.echo(u"[x] #{}: {}".format(task.task_id, task.name))
