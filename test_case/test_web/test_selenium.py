"""
@author:xue
@time:2020/8/5 23:16
@desc:
"""
from selenium import webdriver

from common.logger import Logger
from config.conf import DRIVER_PATH


driver = webdriver.Chrome(DRIVER_PATH)
Logger().get_logger().info("kk")
driver.get("http://www.baidu.com")
