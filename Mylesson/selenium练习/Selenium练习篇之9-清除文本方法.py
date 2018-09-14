from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("lalala")
driver.implicitly_wait(100)
try:
    driver.implicitly_wait(100)
    driver.find_element_by_id("kw").clear()
    driver.implicitly_wait(100)
    driver.find_element_by_id("su").click()
    print("test pass,clean successful")
except Exception as e:
    print("Exception fonud", format(e))
