from selenium import webdriver
import os
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

        # 当前文件所在路径
        # / usr / local / bin / python3.8 / Users / dengping / project / PycharmProjects / pythonProject / demo05_forms.py
        # / Users / dengping / project / PycharmProjects / pythonProject / demo05_forms.py
        # / Users / dengping / project / PycharmProjects / pythonProject / demo05_forms.py
        # path = os.path.abspath(__file__)
        # print(path)

        # 嵌套一下，取得当前文件所载的路径
        # /Users/dengping/project/PycharmProjects/pythonProject
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)

        # 取得指定本地文件的路径  file协议加载本地表单
        file_path = 'file:///' + path + '/forms.html'
        print(file_path)

        # 打开本地文件
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('admin')

        pwd = self.driver.find_element_by_id('pwd')
        pwd.send_keys('123')

        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))

        sleep(2)
        self.driver.find_element_by_id('submit').click()

        self.driver.switch_to.alert.accept()

        username.clear()
        pwd.clear()

        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
