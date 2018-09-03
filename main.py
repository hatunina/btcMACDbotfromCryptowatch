#!/usr/bin/env python

"""
実行用スクリプト
"""

from src.mainlogger import Logger
from src.btcmacd import BtcMACD
from src.slack import Slack
import src.util as util


if __name__ == '__main__':
    config_relative_path = '../config/config.ini'
    abs_config_path = util.relative_to_abs(config_relative_path)

    # 設定ファイルを読み込む
    config_dict = util.read_config(abs_config_path)

    # 出力先ログファイルのsrcディレからの相対パス
    log_file_relative_path = config_dict['log_file_relative_path']

    # CryptowatchAPIのOHLC取得用パラメータ, 85400は日足
    periods = config_dict['periods']

    # 描画する日数
    target_days_range = config_dict['target_days_range']

    # Slackのtoken
    token = config_dict['token']

    # 投稿するチャンネル名
    channel = config_dict['channel']

    # logファイルの相対パスを絶対パスに変換
    abs_log_file_path = util.relative_to_abs(log_file_relative_path)

    # logger初期化
    logger = Logger(abs_log_file_path).get_main_logger()

    btcmacd = BtcMACD(logger, periods, target_days_range)
    message, save_path = btcmacd.pipeline()

    slack = Slack(logger, token, channel)
    slack.notify_with_figure(message, save_path)


    logger.info(save_path)
    logger.info(message)
