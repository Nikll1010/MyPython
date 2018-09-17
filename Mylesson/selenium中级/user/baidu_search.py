from selenium import webdriver

import time

from Mylesson.selenium中级.base.basepage import BasePage, A


class BaiduSearch(object):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("http://www.baidu.com")
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        self.basepage.back()
        time.sleep(5)
        self.basepage.forward()
        time.sleep(5)
        self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()
baidu = A
baidu.lala()
