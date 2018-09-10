from selenium import webdriver
import time
import selenium.common

'''
1） 启动后浏览器

2） 打开百度首页，https://www.baidu.com

3） 定位搜索输入框，记录下输入框元素的xpath表达式：//*[@id='kw']

4） 定位搜索提交按钮（百度一下这个按钮），获取xpath表达式：//*[@id='su']

5） 在搜索输入框输入“Selenium”，点击百度一下这个按钮。

6） 在搜索结果列表去判断是否存在Selenium官网这个链接。

7） 退出浏览器，结束测试。
'''
# driver = webdriver.firefox
# driver = webdriver.FirefoxOptions
driver = webdriver.Firefox()
# print(type(driver))
# driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(8)
driver.get(url='https://www.jd.com/')
driver.find_element_by_xpath('//*[@id="key"]').send_keys('手机')  # 搜索框输入selenium
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/button').click()  # 点击百度按钮

time.sleep(2)  # 等待两秒
# driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/strong").is_displayed()
content = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/strong").text
print(content)
if content == "品牌：":
    print("输入结果匹配")
else:
    print("输入不匹配")
# driver.quit()
