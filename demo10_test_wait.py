# lesson 17
import os.path

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = 'file:///'+os.path.abspath('demo10_test_wait.html')
        self.driver.get(path)


    def test_1(self):
        self.driver.find_element_by_id('btn').click()
        # 显式等待
        # 实例化
        wait = WebDriverWait(self.driver,3)
        wait.until(EC.text_to_be_present_in_element((By.ID,'id2'),'id 2'))
        print(self.driver.find_element_by_id('id2').text)
        print('ok')

if __name__ == '__main__':
    case = TestCase()
    case.test_1()
    case.driver.quit()