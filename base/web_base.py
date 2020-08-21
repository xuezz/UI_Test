"""
@author:xue
@time:2020/8/5 22:19
@desc:web专属方法
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec

from base.base import Base


class WebBase(Base):

    def open_url(self, url):
        """
        打开网址
        :param url:
        """
        try:
            self._log.info('打开 {} 网址进行测试'.format(url))
            self._driver.get(url)
        except Exception as e:
            self._log.error('打开网址 --> 失败：{}'.format(e))

    def switch_into_frame(self, locator):
        """
        切换frame
        :param locator:
        """
        try:
            # self._driver.switch_to.frame(self._driver.find_element_by_xpath(locator))
            # self._wait.until(ec.frame_to_be_available_and_switch_to_it(locator))
            # self._driver.switch_to.frame(locator)
            iframe = self.wait_visible_element(locator)
            self._driver.switch_to.frame(iframe)

        except TimeoutException as e:
            self._log.error('切换iframe超时{}'.format(e))
            self.save_img("切换frame失败")

    def back_to_windows(self):
        self._log.info('返回主文档')
        self._driver.switch_to.default_content()

    def execute_js(self, js):
        """
        调用js
        :param js:
        :return:
        """
        try:
            self._log.info('调用js: {}'.format(js))
            self._driver.execute_script(js)
        except Exception as e:
            print(e)
            self._log.error('调用js失败：{}'.format(js))
            self.save_img("js执行失败")

    def quit_browser(self):
        self._log.info('浏览器 --> 退出')
        self._driver.quit()

    def back_browser(self):
        self._log.info('浏览器 --> 返回')
        self._driver.back()

    def refresh_browser(self):
        self._log.info('浏览器 --> 刷新')
        self._driver.refresh()
