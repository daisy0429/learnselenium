#webElement：nput,button  等等对象
# 这些对象：常用属性和方法
# : i

from selenium import webdriver
from time import sleep

#http://sahitest.com/demo/
from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webElement_property(self):
        e = self.driver.find_element_by_id('t1')
        print(type(e))
        e1 = WebElement
        print(e.id)
        print(e.size)
        print(e.rect)
        print(e.text)

    def test_webelement_method(self):
        e = self.driver.find_element_by_name('t1')
        e.send_keys('hello world')

        print(e.get_attribute('type'))#type = text
        print(e.get_attribute('name'))#name = null
        print(e.get_attribute('value'))#value = hello world

        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))

        sleep(2)
        e.clear()

    def test_webelement_method_findElementBy(self):
        form_element = self.driver.find_element_by_xpath('/html/body/form[1]')
        form_element.find_element_by_id('t1').send_keys('bala')


if __name__ == '__main__':
    case = TestCase()
    # case.test_webElement_property()
    # case.test_webelement_method()
    case.test_webelement_method_findElementBy()
