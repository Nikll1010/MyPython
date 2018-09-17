class BasePage(object):
    """
    将几个常用的selenium方法封装到BasePage这个类中
    比如：back(),forward(),get(),quit()
    """

    def __init__(self, driver):
        """
        定义一个新的构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :return:
        """
        self.driver.forward()

    def open_url(self, url):
        """
        打开url
        :return:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()


class A:
    def lala():
        print("hahaha")
