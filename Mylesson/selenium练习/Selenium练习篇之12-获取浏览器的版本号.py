import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

time.sleep(5)
print(driver.capabilities)
'''
输出一个字典
{'acceptInsecureCerts': True, 'browserName': 'firefox', 
'browserVersion': '62.0', 'moz:accessibilityChecks': False, 
'moz:headless': False, 'moz:processID': 17384, 
'moz:profile': 'C:\\Users\\Nikll\\AppData\\Local\\Temp\\rust_mozprofile.v7Eh7epCugwi', 
'moz:useNonSpecCompliantPointerOrigin': False, 
'moz:webdriverClick': True, 'pageLoadStrategy': 'normal', 
'platformName': 'windows_nt', 'platformVersion': '10.0', 
'rotatable': False, 
'timeouts': {'implicit': 0, 'pageLoad': 300000, 'script': 30000}}
'''