"""
utilモジュール
"""

import os


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