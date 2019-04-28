import re
from time import sleep

import selenium.webdriver
import urllib.request

# from selenium.webdriver.firefox import webdriver

driver = selenium.webdriver.Firefox()
# driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com/")
'''
content = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div[7]/div/div[1]/div[1]").text
print(content)
if content == "合作联系":
    print("匹配成功")
'''
for cook in driver.get_cookies():
    print("%s-->%s" % (cook["name"], cook["value"]))

sleep(2)
driver.quit()
