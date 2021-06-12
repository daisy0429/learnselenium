from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form07_dropdownlist.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element_by_id('provise')
        # 实例化一个对象
        select = Select(se)

        # 单选
        # select.select_by_value('bj')
        # sleep(2)
        # select.select_by_visible_text('TianJin')
        # sleep(2)
        # select.select_by_index('2')
        # sleep(2)
        # self.driver.quit()

        # 多选 选中三个
        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(3)

        #反选
        # select.deselect_all()
        # select.deselect_by_index()
        # sleep(3)

        # 一个list列表
        # select.options
        # select.all_selected_options
        # select.first_selected_option

        for option in select.options:
            print(option.text)



if __name__ == '__main__':
    case =TestCase()
    case.test_select()
    case.driver.quit()
