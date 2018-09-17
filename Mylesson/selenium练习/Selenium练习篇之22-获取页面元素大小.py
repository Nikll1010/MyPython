import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://www.baidu.com')
time.sleep(3)

search_btn = driver.find_element_by_id('su')

print(search_btn.size)
