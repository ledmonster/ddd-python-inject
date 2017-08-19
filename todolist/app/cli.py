# -*- coding: utf-8 -*-
u""" CLI インタフェース """
import click
import inject

from .config import create_config


@click.group()
def main():
    params = {}
    inject.configure(create_config(params))


@main.command()
def list():
    click.echo("list items (TBD)")


@main.command()
def add():
    click.echo("add item (TBD)")


@main.command()
def done():
    click.echo("done item (TBD)")
