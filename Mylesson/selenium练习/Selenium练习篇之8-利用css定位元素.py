from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    driver.find_element_by_css_selector("#kw").send_keys("hahaha")
    driver.find_element_by_css_selector("#su").click()
    print("test pass,element found by css selector")
except Exception as e:
    print("Exception found", format(e))
