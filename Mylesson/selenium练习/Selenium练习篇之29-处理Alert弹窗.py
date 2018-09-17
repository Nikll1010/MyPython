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

driver.execute_script('window.alert("这是一个测试alter弹窗")')
time.sleep(3)

# assert isinstance(driver.switch_to_alert().accept, object)
# noinspection PyDeprecation
driver.switch_to.alert.accept()  # 点击alter弹出框的确定按钮
