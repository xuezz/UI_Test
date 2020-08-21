'''
@author:xue
@time:2020/8/5 21:41
@desc:app和web的基础类
'''
import datetime
from os import path

import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from common.logger import Logger
from config.conf import BASE_DIR


class Base:
    def __init__(self, driver: webdriver):
        self._driver = driver
        self._log = Logger().get_logger()
        self._wait = WebDriverWait(self._driver, 10, 0.5)

    def open(self, url):
        self._driver.get(url)
        self._driver.implicitly_wait(3)

    def implicitly_wait(self, time):
        self._log.info('隐式等待:{}秒'.format(time))
        self._driver.implicitly_wait(time)

    def is_element_exist(self, locator):
        """
        判断元素是否存在
        :param locator:
        :return:
        """
        try:
            self._wait.until(ec.visibility_of_element_located(locator))
            self._log.info('元素存在:{}'.format(locator))
            return True
        except TimeoutException as e:
            print(e)
            self._log.error('元素不存在:{}'.format(locator))
            return False

    def wait_visible_element(self, locator):
        """
        等待元素可见
        :param locator:
        :return:
        """
        try:
            element = self._wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException as e:
            print(e)
            self._log.error('wait_visible_element 超时{}'.format(locator))

    def wait_clickable_element(self, locator):
        """
        等待元素可以被点击
        :param locator:
        :return:
        """
        try:
            element = self._wait.until(ec.element_to_be_clickable(locator))
            return element
        except TimeoutException as e:
            print(e)
            self._log.error('wait_clickable_element 超时:{}'.format(locator))

    def input_text(self, locator, value):
        """
        输入文本
        :param locator:
        :param value:文本
        """
        e = self.wait_visible_element(locator)
        e.clear()
        self._log.info("输入文本:{}".format(value))
        e.send_keys(value)

    def click(self, locator):
        self._log.info("点击元素:{}".format(locator))
        self.wait_clickable_element(locator).click()

    def get_text(self, locator):
        self._log.info("获取{}文本:{}".format(locator, self.wait_visible_element(locator).text))
        return self.wait_visible_element(locator).text

    def save_img(self, doc=''):
        """
         截图
         :param doc: 截图说明
         :return:
         """
        time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = path.join(BASE_DIR, 'screenshots/{}_{}.png'.format(time, doc))
        try:
            self._driver.get_screenshot_as_file(file_name)
            self._log.info('截图成功，存放路径为：{}'.format(file_name))
            with open(file_name, 'rb') as f:
                file = f.read()
                allure.attach(file, doc, allure.attachment_type.PNG)
        except Exception as e:
            print(e)
            self._log.error('截图失败')
