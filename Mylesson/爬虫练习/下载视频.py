from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.iqiyi.com/w_19rwc2of11.html')

ele = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[5]/video')
viedo = ele.read()
with open('quqin.mp4', 'wb') as f:
    f.write(viedo)
