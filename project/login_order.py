# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)


    def tearDown(self):
        print("单个测试用例结束")
        pass
        #单个测试用例结束
    
    def test_login_order(self):
        u"登录测试用例"
        driver = self.driver
        #登录框
        login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
        ActionChains(driver).click(login_ele).perform()

        sleep(2)
        #查找输入框,输入账号，输入框要提前清理里面的数据
        # driver.find_element_by_id("phone").clear()
        # driver.find_element_by_id("phone").send_keys("13113777338")
        driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
        driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("17671351006")
        #查找密码输入框，输入密码
        # driver.find_element_by_id("pwd").clear()
        # driver.find_element_by_id("pwd").send_keys("123456789")
        driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
        driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("Tiamo2020xd")

        #拿到登录按钮
        login_btn_ele = driver.find_element_by_css_selector(".btn")
        #触发点击事件,登录
        login_btn_ele.click()
        #判断登陆是否成功，逻辑-》鼠标移到上面，判断弹窗字符
        #获取鼠标上移的元素
        user_info_ele = driver.find_element_by_css_selector(".avatar_img")
        sleep(1)
        #hover触发
        ActionChains(driver).move_to_element(user_info_ele).perform()
        sleep(1)
        #获取用户名称元素
        user_name_ele = driver.find_element_by_class_name("username")
        print("===测试结果==")
        print(user_name_ele.text)
        if user_info_ele.text == "wanli":
            driver.get_screenshot_as_file(r".\登录成功图片.png")


        name = user_name_ele.text
        #self.assertEqual(name, u"二当家小D",msg="登录失败")

        video_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
        ActionChains(driver).move_to_element(video_ele).perform()

        driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(2)").send_keys(Keys.ENTER)
        sleep(2)

        driver.find_element_by_class_name("course").click()
        sleep(5)

        # TODO xpath没问题，点击不了
        # buy_btn_ele = driver.find_element_by_xpath("""//div[@class="buy_tolearn"]/a[1]""").send_keys(Keys.ENTER)
        # # ActionChains(driver).click(buy_btn_ele).perform()
        # print(buy_btn_ele.title)
        # sleep(5)
        #
        # driver.find_element_by_css_selector(".r_content > button:nth-child(3)").click()

        print("进入下单页面")
       


if __name__ == '__main__':
       unittest.main()

   
