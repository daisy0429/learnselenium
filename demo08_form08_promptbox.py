from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form08_promptbox.html'
        self.driver.get(file_path)

    def test_alert(self):
        # 触发alert
        self.driver.find_element_by_id('alert').click()
        # 切换到alert弹出框
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        # confirm.accept()
        # 取消
        confirm.dismiss()

    def test_prompt(self):
        # 触发alert
        self.driver.find_element_by_id('prompt').click()
        sleep(2)
        # 切换到弹出框
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.accept()

if __name__ == '__main__':
    case =TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()

    case.driver.quit()