'''
@author:xue
@time:2020/8/5 21:47
@desc:日志
'''
import datetime
import logging.handlers
import os.path
from config.conf import BASE_DIR, LOG_PATH


class Logger:

    def __init__(self):
        self._logger = None
        # self._logger = logging.getLogger()
        # self._logger.setLevel(logging.DEBUG)
        # pass

    def _set_logger(self):
        date = datetime.datetime.now().strftime("%Y_%m_%d")
        main_log = os.path.join(LOG_PATH, date + '_log.log')
        err_log = os.path.join(LOG_PATH, date + '_err.log')
        if self._logger is None:
            # 创建handle
            main_handle = logging.FileHandler(main_log, encoding='utf-8')
            main_handle.setLevel(logging.INFO)

            err_handle = logging.FileHandler(err_log, encoding='utf-8')
            err_handle.setLevel(logging.ERROR)

            console_handle = logging.StreamHandler()
            console_handle.setLevel(logging.DEBUG)

            # 创建日志格式
            formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d: %(message)s")
            main_handle.setFormatter(formatter)
            err_handle.setFormatter(formatter)
            console_handle.setFormatter(formatter)

            self._logger.addHandler(main_handle)
            self._logger.addHandler(err_handle)
            self._logger.addHandler(console_handle)

    # def get_logger(self):
    #     """
    #     主函数，供调用生成日志
    #     :return: Logger对象
    #     """
    #     print("_set_logger")
    #     self._set_logger()
    #     return self._logger

    def get_logger(self):
        # 判断日志器为空：
        if self._logger is None:
            # 获取日志器
            self._logger = logging.getLogger()
            # 修改默认级别
            self._logger.setLevel(logging.INFO)
            date = datetime.datetime.now().strftime("%Y_%m_%d")
            log_path = os.path.join(LOG_PATH, date + '_log.log')
            # 获取处理器
            th = logging.FileHandler(filename=log_path, encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            self._logger.addHandler(th)
        # 返回日志器
        return self._logger


if __name__ == '__main__':
    Logger().get_logger().info("kk")
