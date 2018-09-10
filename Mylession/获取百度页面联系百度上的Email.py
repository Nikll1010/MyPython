import re

import selenium.webdriver
import urllib.request

# from selenium.webdriver.firefox import webdriver

driver = selenium.webdriver.Firefox()
# driver.maximize_window()

driver.get("http://home.baidu.com/home/index/contact_us")
'''
content = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div[7]/div/div[1]/div[1]").text
print(content)
if content == "合作联系":
    print("匹配成功")
'''

doc = driver.page_source  # 获取当前页面源代码，可以以‘列表形式’也可以以‘字典形式’
# print(doc)
# emaillist = re.findall(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$ ', doc)
emaillist = re.findall(r'[\w]+@[\w\.-]+', doc)
for eachemail in emaillist:
    print(eachemail)
