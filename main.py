#!/usr/bin/env python

"""
実行用スクリプト
"""

from src.mainlogger import Logger
from src.getbtcvolume import GetBtcVolume
from src.slack import Slack
import src.util as util


if __name__ == '__main__':
    # 投稿するチャンネルのurl
    slack_url = ''
    # 出力先ログファイルのsrcディレからの相対パス
    log_file_relative_path = '../log/log.log'
    # bitflyerAPIの取得対象
    product_code = 'FX_BTC_JPY'

    # logファイルの相対パスを絶対パスに変換
    abs_log_file_path = util.relative_to_abs(log_file_relative_path)

    # logger初期化
    logger = Logger(abs_log_file_path).get_main_logger()


    getbtcvolume = GetBtcVolume(logger, product_code)
    volume, timestamp, total_bid_depth, total_ask_depth = getbtcvolume.pipeline()

    messg_1 = 'timestamp: {}, volume: {}'.format(timestamp, volume)
    messg_2 = 'total_bid_depth: {}, total_ask_depth: {}'.format(total_bid_depth, total_ask_depth)

    #slack = Slack(logger, slack_url)
    #slack.notify(messg_1)
    #slack.notify(messg_2)


    logger.info(messg_1)
    logger.info(messg_2)
