#!/usr/bin/env python

"""
実行用スクリプト
"""

from src.mainlogger import Logger
from src.btcmacd import BtcMACD
from src.slack import Slack
import src.util as util


if __name__ == '__main__':
    # 出力先ログファイルのsrcディレからの相対パス
    log_file_relative_path = '../log/log.log'
    # CryptowatchAPIのOHLC取得用パラメータ, 85400は日足
    periods = '86400'
    # 描画する日数
    target_days_range = 90

    token = ''
    channel = 'bot'

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
