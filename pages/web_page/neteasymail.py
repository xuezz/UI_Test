"""
@author:xue
@time:2020/8/10
@desc:
"""
from time import sleep

from selenium.webdriver.common.by import By

from base.web_base import WebBase


class NetEasyMail(WebBase):
    frame = "//iframe[starts-with(@id, 'x-URS-iframe')]"
    account_loc = By.NAME, 'email'
    password_loc = By.NAME, 'password'
    login_btn = By.ID, 'dologin'
    email_loc = By.XPATH, '//*[@id="_mail_component_145_145"]/span[2]'
    url = 'https://mail.163.com/'

    def open_url(self):
        self.open(self.url)
        sleep(3)
        self.switch_into_frame(self.frame)

    def input_id(self, account):
        self.input_text(self.account_loc, account)

    def input_password(self, password):
        self.input_text(self.password_loc, password)

    def click_login(self):
        self.click(self.login_btn)

    def login(self, account, pwd):
        self.input_id(account)
        self.input_password(pwd)
        self.click_login()

    def is_login(self):
        sleep(3)
        return self.is_element_exist(self.email_loc)

    def send_mail(self):
        pass
