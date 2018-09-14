import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

time.sleep(5)
ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')  # 出发CTRL +T
time.sleep(5)
print("hello")
