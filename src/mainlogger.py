"""
ロガー設定、生成モジュール
"""

from logging import getLogger, StreamHandler, FileHandler, Formatter, INFO


class Logger(object):
    """
    コンストラクタでロガーの出力先やフォーマット、レベルを設定しgetterでロガーを取得する。
    """

    def __init__(self, log_file_path):
        # type: (str) -> None
        """
        ロガーの設定を行う。
        :param log_file_path: 出力先ファイルパス
        """
        self.logger = getLogger("Logger")
        self.logger.setLevel(INFO)

        handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        stream_handler = StreamHandler()
        stream_handler.setLevel(INFO)
        stream_handler.setFormatter(handler_format)

        file_handler = FileHandler(log_file_path, 'a')
        file_handler.setLevel(INFO)
        file_handler.setFormatter(handler_format)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def get_main_logger(self):
        # type: (None) -> Logger
        """
        getter
        :return: コンストラクタで設定したロガー
        """
        return self.logger
