import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://www.baidu.com')
time.sleep(3)

element = driver.find_element_by_id('kw')
actionChains = ActionChains(driver)  # 鼠标悬停  初始化一个ActionChains对象
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()  # preform--右键
