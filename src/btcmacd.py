

import ast
import datetime

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
matplotlib.use('Agg')

from src.cryptowatchapi import CryptowatchAPI
import src.util as util


class BtcMACD(object):

    def __init__(self, logger, periods, target_days_range):
        self.logger = logger
        self.periods = periods
        self.target_days_range = target_days_range
        self.cryptowatch_api = CryptowatchAPI(self.logger)
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
        plt = self.generate_figure(macd)

        # 図を保存する
        save_path = util.relative_to_abs('../figure/' + self.today.strftime("%Y-%m-%d") + '.jpg')
        self.save_figure(plt, save_path)

        message = self.generate_message(macd)

        return message, save_path


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


    def generate_figure(self, macd):
        self.logger.info('generate_figure')
        # x軸を作成
        date_range = pd.date_range(macd.iloc[0, 0], periods=len(macd), freq='d')

        fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]})

        # 価格チャート, macd, signalのチャート, macdとsignalの差を棒グラフで描画
        ax1.plot(date_range, macd['close'])
        ax2.plot(date_range, macd['macd'])
        ax2.plot(date_range, macd['signal'])
        ax2.bar(date_range, macd['macd-signal'])

        # グリッドを描画
        ax1.grid()
        ax2.grid()

        # x軸のラベルを縦にする
        ax1.set_xticklabels(date_range, rotation=90, size="small")
        ax2.set_xticklabels(date_range, rotation=90, size="small")

        # x軸のラベルの日付のフォーマットを調整
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

        # ラベルが被らないように調整
        fig.tight_layout()

        return plt

    def save_figure(self, plt, save_path):
        self.logger.info('save_figure')
        self.logger.info('save_path: {}'.format(save_path))
        plt.savefig(save_path)




