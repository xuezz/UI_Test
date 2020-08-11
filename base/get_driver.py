"""
@author:xue
@time:2020/8/5 23:01
@desc:
"""
import appium.webdriver
from selenium import webdriver

from config.conf import DRIVER_PATH


class GetDriver:
    _web_driver = None
    _app_driver = None

    @classmethod
    def get_web_driver(cls):
        if cls._web_driver is None:
            cls._driver = webdriver.Chrome(DRIVER_PATH)
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '6.0.1'
            # 必填
            desired_caps['deviceName'] = 'MuMu'
            # APP包名
            desired_caps['appPackage'] = "com.hexin.plat.android"
            # 启动名
            desired_caps['appActivity'] = ".Hexin"
            # 设置driver
            cls._app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            # 返回cls.__app_driver
        return cls._app_driver
