import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://news.baidu.com/')
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul/li[1]/strong/a').click()
print(driver.current_window_handle)  # 输出当前窗口的句柄
page_get_title_list = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[2]/ul/li/a').text
print(page_get_title_list)
page1_get_title = driver.find_element_by_xpath(
    '/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul/li[1]/strong/a').text
print(page1_get_title)
handles = driver.window_handles  # 获取当前全部窗口句柄集合
print(handles)

for handle in handles:  # 切换窗口
    if handle != driver.current_window_handle:
        print('switch to second window', handle)
        # driver.close()  # 关闭当前句柄
        driver.switch_to.window(handle)  # 切换到第二个句柄
        print(driver.current_window_handle)
page2_get_title = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[1]/h1').text
print(page2_get_title)

try:
    assert page1_get_title == page2_get_title
    print("test pass")
except Exception as e:
    print("test fail", format(e))
