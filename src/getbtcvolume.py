

import ast
from bitflyerapi import BitflyerAPI


class GetBtcVolume(object):

    def __init__(self, logger, product_code):
        self.logger = logger
        self.product_code = product_code

    def pipeline(self):
        self.logger.info('pipline')

        api = BitflyerAPI(self.logger, self.product_code)
        response = api.get_ticker()

        dic = ast.literal_eval(response.text)
        volume = int(dic['volume'])
        timestamp = dic['timestamp']
        total_bid_depth = int(dic['total_bid_depth'])
        total_ask_depth = int(dic['total_ask_depth'])

        self.logger.info('timestamp: {}, volume: {}'.format(timestamp, volume))
        self.logger.info('total_bid_depth: {}, total_ask_depth: {}'.format(total_bid_depth, total_ask_depth))

        return volume, timestamp, total_bid_depth, total_ask_depth

