"""
@author:xue
@time:2020/8/5 22:47
@desc:
"""
import os

import pytest

from base.get_driver import GetDriver
from common.logger import Logger

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate report/ -o report/html --clean')
    # Logger().get_logger().info("ll")
    # GetDriver.get_app_driver()
