# -*- coding: utf-8 -*-
u""" Dependency Injection 用の設定関数を提供するモジュール """
import inject


def create_config(params):
    u""" inject 用の config を生成する

    :param dict params: パラメータの辞書
    :return function: inject 用の config 関数
    """
    def config(binder):
        pass
    return config
