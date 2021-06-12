from selenium import webdriver
import os
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms02.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        sleep(3)
        checkbox_swimming = self.driver.find_element_by_name('swimming')
        if not checkbox_swimming.is_selected():
            checkbox_swimming.click()

        checkbox_reading = self.driver.find_element_by_name("reading")
        if not checkbox_reading.is_selected():
            checkbox_reading.click()

        sleep(3)

        # 反选 un-selected
        checkbox_swimming.click()


    def test_radio(self):
        sleep(2)
        list = self.driver.find_elements_by_name('gender')
        list[0].click()


if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()