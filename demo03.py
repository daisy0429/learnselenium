# webdriver常用属性和方法
from time import sleep

from selenium import webdriver

class TestCase():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    # driver常用属性
    def test_property(self):
        print(self.driver.name) ##浏览器名称
        print(self.driver.current_url)
        print(self.driver.title)##判断是否登陆成功
        print(self.driver.window_handles)##tab及其操作
        print(self.driver.page_source)##source code of page
        self.driver.quit()
    # driver常用方法
    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        self.driver.forward()
        sleep(1)
        self.driver.close()#
        self.driver.quit()#close of browser

        #窗口切换
    def test_window(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)



if __name__ == '__main__':
    case = TestCase()
    # case.test_property()
    #case.test_method()
    case.test_window()