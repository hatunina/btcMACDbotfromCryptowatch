

from mainlogger import Logger
from getbtcvolume import GetBtcVolume

import slackweb


if __name__ == '__main__':
    # logの出力先
    log_file_path = './log/log.log'
    # logger初期化
    logger = Logger(log_file_path).get_main_logger()

    logger.info('TEST')

    product_code = 'FX_BTC_JPY'

    getbtcvolume = GetBtcVolume(logger, product_code)
    volume, timestamp, total_bid_depth, total_ask_depth = getbtcvolume.pipeline()

    messg_1 = 'timestamp: {}, volume: {}'.format(timestamp, volume)
    messg_2 = 'total_bid_depth: {}, total_ask_depth: {}'.format(total_bid_depth, total_ask_depth)

    slack = slackweb.Slack(url="")

    slack.notify(text=messg_1)
    slack.notify(text=messg_2)
