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

    # logファイルの相対パスを絶対パスに変換
    abs_log_file_path = util.relative_to_abs(config_dict['log_file_relative_path'])

    # logger初期化
    logger = Logger(abs_log_file_path).get_main_logger()

    btcmacd = BtcMACD(logger, config_dict['periods'], config_dict['target_days_range'], config_dict['msg_threshold'])
    message, abs_figure_path = btcmacd.pipeline()

    slack = Slack(logger, config_dict['token'], config_dict['channel'])
    slack.notify_with_figure(message, abs_figure_path)

    logger.info('DONE')
