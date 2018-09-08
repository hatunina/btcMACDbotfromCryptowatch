"""
MACD関連モジュール
"""

import ast
import datetime

import pandas as pd

from src.cryptowatchapi import CryptowatchAPI
from src.btcfigure import BtcFigure
import src.util as util

class BtcMACD(object):
    """
    MACD関連クラス
    """

    def __init__(self, logger, periods, target_days_range):
        self.logger = logger
        self.periods = periods
        self.target_days_range = target_days_range
        self.cryptowatch_api = CryptowatchAPI(self.logger)
        self.btc_figure = BtcFigure(self.logger)
        self.today = datetime.datetime.now()

    def pipeline(self):
        self.logger.info('BtcMACD.pipeline')
        self.logger.info('today: {}'.format(self.today))
        self.logger.info('target_days_range: {}'.format(self.target_days_range))

        # apiを叩く
        dict_periods = {'periods': self.periods}
        response = self.cryptowatch_api.get_ohlc(dict_periods)

        # responseをデータフレームへ整える
        df_adjusted_response = self.response_to_dataframe(response)

        # 指定した期間だけ抜き出す
        df_adjusted_response = self.extract_dataframe(df_adjusted_response)

        # MACDを計算する
        macd = self.caluc_macd(df_adjusted_response)

        # 価格, MACD, signal, 差を描画する
        plt = self.btc_figure.generate_figure(macd)

        # 図を保存する
        abs_figure_path = util.relative_to_abs('../figure/' + self.today.strftime("%Y-%m-%d") + '.jpg')
        self.btc_figure.save_figure(plt, abs_figure_path)

        message = self.generate_message(macd)

        return message, abs_figure_path

    def generate_message(self, macd):
        self.logger.info('generate_message')

        today_macd_diff_signal = int(macd[macd['date'] == self.today.strftime("%Y-%m-%d")]['macd-signal'])

        if 3000 >= today_macd_diff_signal >= -3000:
            message = 'MACDとsignalの差は{}！トレンド転換？'.format(today_macd_diff_signal)
        else:
            message = 'MACDとsignalの差は{}！トレンド継続！'.format(today_macd_diff_signal)

        return message

    def extract_dataframe(self, df_adjusted_response):
        self.logger.info('extract_dataframe')

        target_days = (self.today - datetime.timedelta(days=self.target_days_range)).strftime("%Y-%m-%d")
        df_adjusted_response = df_adjusted_response[df_adjusted_response['CloseTime'] >= target_days]

        return df_adjusted_response

    def response_to_dataframe(self, response):
        self.logger.info('response_to_dataframe')

        dict_response = ast.literal_eval(response.text)
        dct_result = dict_response['result'][self.periods]

        df_adjusted_response = pd.DataFrame(dct_result, columns=['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', '?'])
        df_adjusted_response['CloseTime'] = pd.to_datetime(df_adjusted_response['CloseTime'], unit='s')

        return df_adjusted_response

    def caluc_macd(self, df_adjusted_response):
        self.logger.info('caluc_macd')

        macd = pd.DataFrame()
        macd['date'] = df_adjusted_response['CloseTime']
        macd['close'] = df_adjusted_response['ClosePrice']
        macd['ema_10'] = df_adjusted_response['ClosePrice'].ewm(span=10).mean()
        macd['ema_26'] = df_adjusted_response['ClosePrice'].ewm(span=26).mean()
        macd['macd'] = macd['ema_10'] - macd['ema_26']
        macd['signal'] = macd['macd'].ewm(span=9).mean()
        macd['macd-signal'] = macd['macd'] - macd['signal']

        return macd