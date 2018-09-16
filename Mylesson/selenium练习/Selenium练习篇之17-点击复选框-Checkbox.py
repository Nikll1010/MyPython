import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://weibo.com/")

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/ul/li[3]/a').click()
time.sleep(10)
driver.find_element_by_css_selector('checkbox').click()
# driver.find_element_by_class_name('item auto_login').click()
# driver.find_element_by_id('login_form_savestate').click()
# driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[3]/div[5]/label').click()
time.sleep(10)
# driver.find_element_by_class_name('item auto_login').click()
# driver.find_element_by_id('login_form_savestate').click()
# driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[3]/div[5]/label').click()
time.sleep(10)
driver.quit()
