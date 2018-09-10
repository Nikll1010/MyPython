from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com/")
try:
    driver.find_element_by_link_text("新闻")
    print("test pass,新闻 find")
except Exception as e:
    print("Exception find", format(e))

driver.quit()
