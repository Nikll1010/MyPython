import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("lalala")
time .sleep(5)
driver.implicitly_wait(100)
try:
    driver.find_element_by_id("su").click()
    driver.refresh()
    print("test pass,refresh successful")
except Exception as e:
    print("Exception fonud", format(e))
