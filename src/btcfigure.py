"""
BTCの描画関連モジュール
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
matplotlib.use('Agg')


class BtcFigure(object):
    """
    画像生成、保存等のクラス
    """

    def __init__(self, logger):
        # type: (logger) -> None
        """
        コンストラクタ
        :param logger: logger
        """
        self.logger = logger

    def generate_figure(self, macd):
        # type: (df) -> matplotlib.pyplot
        """
        macdを格納したdataframeから図を作成する
        :param macd: dataframe
        :return: plt
        """

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

    def save_figure(self, plt, abs_figure_path):
        # type: (matplotlib.pyplot, str) -> None
        """
        渡されたpltをabs_figure_pathに保存する
        :param plt: 図が格納されたplt
        :param abs_figure_path: 保存先の絶対パス
        """
        self.logger.info('save_figure')
        self.logger.info('abs_figure_path: {}'.format(abs_figure_path))
        plt.savefig(abs_figure_path)