import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://www.baidu.com')
time.sleep(3)

element = driver.find_element_by_tag_name('html')
element.send_keys(Keys.CONTROL+'t')
element.send_keys(Keys.CONTROL+'a')
