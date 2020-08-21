"""
@author:xue
@time:2020/8/11
@desc:
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.web_base import WebBase


class SendPage(WebBase):
    write_btn = By.XPATH, '//*[@id="_mail_component_137_137"]'
    address_input = By.XPATH, '//*[starts-with(@id,"_mail_emailinput")]/input'
    subject_input = By.XPATH, "//*[contains(@aria-label,'邮件主题输入框，请输入邮件主题')]/input"
    iframe_id = By.CLASS_NAME, 'APP-editor-iframe'
    content_input = By.XPATH, '/html/body'
    send_btn = By.XPATH, '//*[@class="jp0"]/div[1]'
    send_ret = By.XPATH, "//h1[text()='发送成功']"

    def send_email(self, address, subject, content):
        self.click(self.write_btn)
        self.input_text(self.address_input, address)
        self.input_text(self.subject_input, subject)
        self.switch_into_frame(self.iframe_id)
        self.input_text(self.content_input, Keys.TAB)
        self.input_text(self.content_input, content)
        self.back_to_windows()
        self.click(self.send_btn)

    def is_send_success(self):
        return self.is_element_exist(self.send_ret)
