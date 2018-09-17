import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://www.creditchina.gov.cn/')
time.sleep(3)

driver.find_element_by_link_text("登录").click()
time.sleep(3)
driver.find_element_by_id('loginBtn').click()

# 方法一，设置断言
# error_mes = driver.find_element_by_class_name("message").text
# print(error_mes)
# try:
#     assert error_mes == '账户不能为空'
#     print('error test pass')
# except Exception as e:
#     print("error test fail", format(e))
# # 判断是否在页面显示

try:
    error_message = driver.find_element_by_class_name('"message" and text()="账户不能为空"').is_displayed()
    print('error test pass,the error message is displayed')
except Exception as e:
    print("error test fail", format(e))
