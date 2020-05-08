# conding: utf-8
# 1.常见验证码解决方案
    # 1.1 破解验证码
        # 1.1.1 ocr识别破解验证码
        # 1.1.2 AI人工智能识别
            # tensorflow 字符验证码识别

    # 2.1 绕过验证码
      # 2.1.1 让开发人员临时关闭验证码 （安全性保密）
      # 2.1.2 提供一个万能完整码（安全性保密）
      # 2.1.3 获取cookie/token/session_id 直接调用接口

# 2.实例
# conding: utf-8
# 弹窗常用方法(需要先切换窗口，alert和comfirm)
    # accept()  接受
    # dismiss() 取消

# 网页单选框
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#app > div > div.selectpay > div > div.pay > div
driver = webdriver.Firefox()
# driver.get("http://www.xdclass.net")
driver.get("https://www.xdclass.net")
driver.implicitly_wait(10)
driver.maximize_window()
driver.add_cookie({"name":"token", "value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTQuanBlZyIsImlkIjo2NzQxMTgsIm5hbWUiOiJ3YW5saSIsImlhdCI6MTU4ODg1MjIwMCwiZXhwIjoxNTg5NDU3MDAwfQ.WFB7xzd7rb-uYw6nrl6xlGyRsVQ4cO3mdeNwFOGF13M"})
try:
    driver.find_element_by_css_selector("#app > div > div.header > div > div.m_navitems.f_l > ul > li:nth-child(2)").click()
    # if driver.find_element_by_css_selector("#app > div > div.allcourse > div > div.content > a:nth-child(1) > div > img").click():
    # elif driver.find_element_by_css_selector("#app > div > div.allcourse > div > div.content > a:nth-child(1) > div > h1").click()
    driver.find_element_by_css_selector("#app > div > div.allcourse > div > div.content > a:nth-child(1) > div").click()

    # buy_tolearn = driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)")
    #     # ActionChains(driver).move_to_element(buy_tolearn).click().perform()
    sleep(3)
    # TODO 这里点击click没成功，后面解决
   # driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)").send_keys(Keys.ENTER)
    tolearn = driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)")
    driver.execute_script(tolearn)
    driver.find_element_by_css_selector("#app > div > div.payconfirm > div.price.w > div.r_content.f_r > button").click()
    driver.find_element_by_css_selector("#app > div > div.selectpay > div > div.pay_way > div.alipay.selected").click()
    driver.find_element_by_css_selector("#app > div > div.selectpay > div > div.pay > div").click()
except:
    pass
finally:
    driver.close()

