import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

time.sleep(5)
driver.find_element_by_link_text("新闻").click()
print(driver.title)  # 获取当前页面title
