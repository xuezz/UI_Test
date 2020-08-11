"""
@author:xue
@time:2020/8/6
@desc:
"""
import configparser
import os
from config.conf import INI_PATH


class ReadConfig:
    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件%s不存在！" % INI_PATH)
        self._config = configparser.RawConfigParser()
        self._config.read(INI_PATH, encoding='utf-8')

    def get(self, section, option):
        return self._config.get(section, option)

    def set(self, section, option, value):
        self._config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self._config.write(f)
