from selenium import webdriver
from time import sleep

# 实例化chromedriver。 环境变量已配置 executable_path='所需driver所在的具体路径'
# driver = webdriver.Chrome(executable_path='chromedriver')

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
sleep(1)
driver.find_element_by_name('wd').send_keys('selenium')
sleep(2)
driver.find_element_by_id('su').click()
sleep(1)
driver.quit()

