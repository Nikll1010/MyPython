import time

from selenium import webdriver


class Search:
    driver = webdriver.Firefox()
    driver.set_window_size(1024, 768)
    driver.set_window_position(500, 100)
    driver.implicitly_wait(10)
    time.sleep(3)

    def open_baidu(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(3)

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("seleinum")
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium' in self.driver.title
            print("test pass")
        except Exception as e:
            print("test fail", format(e))


if __name__ == '__main__':
    baidu = Search()
    baidu.open_baidu()
    baidu.test_search()
