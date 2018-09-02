"""
slackに関するモジュール
"""

import requests

class Slack(object):
    """
    Slack関連クラス
    """

    def __init__(self, logger, token, channel):
        # type: (logger, str) -> None
        """
        slackwebモジュール, loggerの設定
        :param logger: logger
        :param url: 投稿先チャンネルurl
        """
        self.logger = logger
        self.token = token
        self.channel = channel

    def notify_with_figure(self, massage, save_path):
        self.logger.info('notify_with_figure')

        files = {'file': open(save_path, 'rb')}
        param = {
            'token': self.token,
            'channels': self.channel,
            'filename': "filename",
            'initial_comment': massage,
            'title': "todays btc MACD"
        }

        requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
