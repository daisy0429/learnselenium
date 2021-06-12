from selenium import webdriver

from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    # 仅用于调试代码
    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # 线程阻塞blocking  wait机制
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_implicityly(self):
        # 如果元素没找到，最多等待10s。
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(3)

    # 最常用
    def test_wait(self):
        # 实例化
        wait = WebDriverWait(self.driver,2,0.5)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicityly()
    case.test_wait()
    case.driver.quit()