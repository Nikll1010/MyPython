import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(1024, 768)
driver.set_window_position(500, 100)
driver.get('http://www.baidu.com')
time.sleep(3)
#
# # 方法1
try:
    assert '百度一下1' in driver.title
    print("Assertion test pass")
except Exception as e:
    print('Assertion test fail', format(e))
    print(e)

# 方法二

# if '百度一下，你就知道' == driver.title:
#     print('Assertion test pass')
# else:
#     print('Assertion test fail')

print(driver.title)
