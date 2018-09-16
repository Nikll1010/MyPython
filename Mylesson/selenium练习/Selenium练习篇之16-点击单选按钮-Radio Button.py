import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://news.baidu.com")

time.sleep(5)
# n = 10
# while n > 0:
#     for i in driver.find_elements_by_class_name('search-radios'):
#         i.click()
#         time.sleep(15)
#         n -= 1
#         print(i.text)
for i in driver.find_elements_by_class_name('search-radios'):
    i.click()
    time.sleep(5)
    print(i.text)
    print(type(i))
    print(i)
driver.quit()
