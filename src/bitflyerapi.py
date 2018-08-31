
import requests

class BitflyerAPI(object):

    def __init__(self, logger, product_code):
        self.logger = logger
        self.domain_url = 'https://api.bitflyer.jp'
        self.ticker_url = '/v1/getticker'
        self.product_code = {'product_code': product_code}

    def get_ticker(self):
        # type: () -> str
        """
        bitflyerAPIを叩く
        :return: btcデータ
        """
        request_url = self.domain_url + self.ticker_url
        return requests.get(request_url, params=self.product_code)