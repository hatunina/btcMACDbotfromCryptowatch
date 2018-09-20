"""
utilモジュール
"""

import os
import sys
import configparser


def relative_to_abs(relative_path):
    # type: (str) -> str
    """
    相対パスを絶対パスに変換する。
    :param relative_path: srcディレクトリからの相対パス
    :return: 絶対パス
    """

    # スクリプトのあるディレクトリの絶対パスを取得
    dir_path = os.path.dirname(os.path.abspath(__file__))

    # 絶対パスと相対パスをくっつける
    tmp_path = os.path.join(dir_path, relative_path)

    # 正規化して絶対パスにする
    abs_path = os.path.normpath(tmp_path)

    return abs_path


def read_config(abs_config_path):
    # type: (str) -> dict
    """
    設定ファイルを読み込み辞書に格納して返す
    :param abs_config_path: 設定ファイルの絶対パス
    :return: 設定内容をキーに持つ辞書
    """
    config = configparser.ConfigParser()

    if is_exits(abs_config_path):
        # 環境によってはencodingを指定しないとエラー
        config.read(abs_config_path, encoding='utf-8')
    else:
        try:
            raise AttributeError("file or dir not found")
        except AttributeError as e:
            print('{}: {}'.format(e, abs_config_path))
            sys.exit(1)

    config_dict = {}

    config_dict['log_dir_relative_path'] = config['Path']['log_dir_relative_path']
    config_dict['periods'] = config['General']['periods']
    config_dict['target_days_range'] = int(config['General']['target_days_range'])
    config_dict['msg_threshold'] = int(config['General']['msg_threshold'])
    config_dict['token'] = config['Slack']['token']
    config_dict['channel'] = config['Slack']['channel']

    return config_dict


def is_exits(check_path):
    # type: (str) -> bool
    """
    引数のパスにファイル/ディレクトリが存在するかチェック
    :param check_path: ファイルもしくはディレクトリのパス
    :return: 存在するかどうかのbool
    """
    return os.path.exists(check_path)
