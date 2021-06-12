from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# *:多参
def get_element(driver,*loc):
   e = driver.find_element(*loc)
   return e


if __name__ == '__main__':
    # instance of a webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    # 元组
    loc1 = (By.ID,'kw')
    loc2 = (By.ID,'su')
    get_element(driver,*loc1).send_keys('selenium')
    get_element(driver,*loc2).click()
    sleep(2)
    driver.quit()