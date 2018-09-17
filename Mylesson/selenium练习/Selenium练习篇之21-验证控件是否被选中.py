import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://news.baidu.com')
time.sleep(3)

try:
    driver.find_element_by_id("news").is_selected()
    print("test pass,")
except Exception as e:
    print("test fail", format(e))
try:
    driver.find_element_by_id("newstitle").is_selected()
    print("test pass,")
except Exception as e:
    print("test fail", format(e))
