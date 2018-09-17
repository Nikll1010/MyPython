import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('https://tieba.baidu.com/index.html')
time.sleep(3)

# driver.execute_script('window.alert("这是一个alter弹匡");')  # 执行js
# time.sleep(5)

# 滚动滚动条
# target_elem = driver.find_element_by_link_text("人文自然")
# driver.execute_script('return arguments[0].scrollIntoView();', target_elem)

driver.execute_script('scroll(0,3400)')  # 大致的滚动滚动条
