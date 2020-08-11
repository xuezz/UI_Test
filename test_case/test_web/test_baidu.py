"""
@author:xue
@time:2020/8/5 22:49
@desc:
"""
from time import sleep

# import allure
import allure
import pytest

from pages.baidu import SearchPage


@pytest.mark.usefixtures("browser_setup")
class TestSearch:

    @allure.step(title="测试步骤001")
    def test_search(self, browser_setup):
        sp = SearchPage(browser_setup)
        allure.attach("描述", "搜索页面~~")
        sp.search()
        sleep(2)
        sp.save_img("百度")
