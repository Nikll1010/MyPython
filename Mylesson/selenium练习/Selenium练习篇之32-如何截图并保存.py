import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://news.baidu.com')
time.sleep(3)
nowTime = time.strftime("%Y%m%d.%H.%M.%S")  # 加个时间戳
driver.get_screenshot_as_file(r"D:\%s.png" % nowTime)  # 共有三种截图方法
