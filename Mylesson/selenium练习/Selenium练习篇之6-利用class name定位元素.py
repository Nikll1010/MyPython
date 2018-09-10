from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com/")

try:
    driver.find_element_by_class_name('s_ipt')
    print("test pass: element find class name")
except Exception as e:
    print("Exception find", format(e))
driver.quit()
