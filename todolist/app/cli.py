# -*- coding: utf-8 -*-
u""" CLI インタフェース """
import click
import inject

from .config import create_config


@click.group()
def main():
    params = {
        "redis_host": "localhost",
        "redis_port": "6379",
        "redis_db": "2",
    }
    inject.configure(create_config(params))


@main.command()
def list():
    click.echo("list tasks (TBD)")


@main.command()
def add():
    click.echo("add task (TBD)")


@main.command()
def done():
    click.echo("done task (TBD)")
