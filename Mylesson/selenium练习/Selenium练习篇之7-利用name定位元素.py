from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com/")
try:
    driver.find_element_by_name(name="wd")
    print("test pass,element found by name vale")
except Exception as e:
    print("Exception found", format(e))
