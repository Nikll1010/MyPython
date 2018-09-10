from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com/")
try:
    driver.find_element_by_partial_link_text("主页").click()
    print("test pass:element found by partial link text")
except Exception as e:
    print("Exception find", format(e))
# driver.quit()
