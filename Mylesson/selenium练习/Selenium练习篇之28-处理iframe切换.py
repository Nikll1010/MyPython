import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('https://www.126.com')
time.sleep(3)

driver.switch_to.frame("x-URS-iframe")  # 切换到iframe，若无此行代码，则找不到帐号输入框
driver.find_element_by_xpath("//*[@class='j-inputtext dlemail']").send_keys("selenium switch test")  # 在帐号输入框内输入
