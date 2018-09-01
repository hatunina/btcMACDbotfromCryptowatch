"""
slackに関するモジュール
"""

import slackweb


class Slack(object):
    """
    Slack関連クラス
    """

    def __init__(self, logger, url):
        # type: (logger, str) -> None
        """
        slackwebモジュール, loggerの設定
        :param logger: logger
        :param url: 投稿先チャンネルurl
        """
        self.logger = logger
        self.slack = slackweb.Slack(url=url)

    def notify(self, message):
        # type: (str) -> None
        """
        設定されたチャンネルへ投稿する
        :param message: 投稿内容
        """
        self.logger.info(message)
        self.slack.notify(text=message)
