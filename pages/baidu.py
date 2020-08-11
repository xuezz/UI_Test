"""
@author:xue
@time:2020/8/5 22:49
@desc:
"""
from time import sleep

from selenium.webdriver.common.by import By

from base.web_base import WebBase


class SearchPage(WebBase):
    input_loc = (By.XPATH, '//*[@id="kw"]')
    search_btn = (By.XPATH, '//*[@id="su"]')

    def search(self):
        self.input_text(self.input_loc, "52")
        sleep(2)
        self.click(self.search_btn)
