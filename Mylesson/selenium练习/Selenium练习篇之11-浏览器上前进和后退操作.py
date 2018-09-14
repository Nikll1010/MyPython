import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

time.sleep(5)
elem_news = driver.find_element_by_link_text("新闻")
elem_news.click()  # 进入新的页面
time.sleep(5)
driver.back()  # 返回百度主页
time.sleep(5)
driver.forward()  # 前进前一页
