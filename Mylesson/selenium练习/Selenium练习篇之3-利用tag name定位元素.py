from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.baidu.com/")
try:
    driver.find_element_by_tag_name('form')
    print("test pass,form find")
except Exception as e:
    print("Exception find", format(e))
driver.quit()