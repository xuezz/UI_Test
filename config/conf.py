'''
@author:xue
@time:2020/8/5 21:45
@desc:
'''
import os

# driver目录
DRIVER_PATH = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

# 项目目录
BASE_DIR = os.path.dirname((os.path.dirname(__file__)))

# 配置目录
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini').replace('\\', '/')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log').replace('\\', '/')

# 数据目录
DATA_PATH = os.path.join(BASE_DIR, 'data').replace('\\', '/')

# 截图目录
IMG_PATH = os.path.join(BASE_DIR, 'screenshot').replace('\\', '/')