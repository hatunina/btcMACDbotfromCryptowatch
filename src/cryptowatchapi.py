"""
CryptowatchのAPI用モジュール
"""

import requests

class CryptowatchAPI(object):
    """
    CryptowatchAPIの設定やリクエスト用クラス
    """

    def __init__(self, logger):
        # type: (logger) -> None
        """
        設定
        :param logger: logger
        """
        self.logger = logger
        self.ohlc_url = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc'

    def get_ohlc(self, dict_periods):
        # type: (dict) -> response
        """
        CryptowatchAPIを使ってOHLCを取得する
        :return: response
        """
        self.logger.info('get_ohlc')
        self.logger.info('periods: {}'.format(dict_periods['periods']))
        return requests.get(self.ohlc_url, params=dict_periods)
