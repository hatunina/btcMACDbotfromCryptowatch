
import requests


class CryptowatchAPI(object):

    def __init__(self, logger):
        self.logger = logger
        self.ohlc_url = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc'

    def get_ohlc(self, dict_periods):
        # type: (dict) -> response
        """
        CryptowatchAPIを使ってOHLCを取得する
        :return: response
        """
        self.logger.info('dict_periods: {}'.format(dict_periods))
        return requests.get(self.ohlc_url, params=dict_periods)
