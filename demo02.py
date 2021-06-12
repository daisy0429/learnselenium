# 找元素方法


from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

url = 'http://www.baidu.com'
# # from .chrome.webdriver import WebDriver as Chrome  # noqa````````````
# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()
# sleep(1)

# element = driver.find_element_by_id('kw')
# element.send_keys('selenium')
# print(type(element))
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.quit()

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(1)

    def test_find_element_by_id(self):
        # id is unique
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        print(type(element))
        self.driver.find_element_by_id('su').click()
        sleep(3)
        # self.driver.quit()

    def test_find_element_by_name(self):
        # 1. find_element_by_name will locate to the 1st element which has the same name,
        # in case more than one elements having the same name
        # 2. find_elements_by_name will return a collection/list
        element = self.driver.find_element_by_name('wd')
        element.send_keys('selenium')
        print(type(element))
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_find_element_by_link_text(self):
        self.test_find_element_by_id()
        self.driver.find_element_by_link_text('百度首页').click()
        sleep(3)

    def test_find_element_by_partial_link_text(self):
        self.test_find_element_by_id()
        self.driver.find_element_by_partial_link_text('首页').click()
        sleep(3)

    def test_find_element_by_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_find_element_by_tag_name(self):
        input = self.driver.find_element_by_tag_name('input')[0]
        print(input)
        # input.send_keys('selenium')
        # self.driver.find_element_by_id('su').click()
        # sleep(3)

    def test_find_element_by_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_find_elements_by_class_name(self):
        element = self.driver.find_elements_by_class_name('s_ipt')
        print(type(element))
        element[0].send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_find_element(self):
        # default: by id
        self.driver.find_element(By.ID,value='kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()



if __name__ == '__main__':
    # instance of class TestCase
    case = TestCase()
    # case.test_find_element_by_id()
    # case.test_find_element_by_name()
    # case.test_find_element_by_link_text()
    # case.test_find_element_by_partial_link_text()
    # case.test_find_element_by_xpath()
    # case.test_find_element_by_tag_name()
    # case.test_find_element_by_css_selector()
    # case.test_find_elements_by_class_name()
    case.test_find_element()