# from selenium.webdriver.firefox import webdriver
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com/")

try:
    driver.find_element_by_id('kw')
    print("tess pass,Find ID")
except Exception as e:
    print("Exception found", format(e))

driver.quit()
