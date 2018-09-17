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

for image in driver.find_elements_by_tag_name("img"):
    print(image.text)
    print(image.size)
    print(image.tag_name)


print(driver.find_elements_by_tag_name('img'))

