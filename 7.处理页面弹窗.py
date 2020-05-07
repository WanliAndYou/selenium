# conding: utf-8
# 弹窗常用方法(需要先切换窗口，alert和comfirm)
    # accept()  接受
    # dismiss() 取消

# 网页单选框
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
# driver.get("http://www.xdclass.net")
driver.get("https://www.baidu.com")
# driver.maximize_window()
# 点击按钮
driver.find_element_by_id("alert").click()
# 切换到弹窗
alert = driver.switch_to_alert()
sleep(2)
alert.accept() # 接受

# 点击按钮
driver.find_element_by_id("confirm").click()
# 切换到弹窗
confirm = driver.switch_to_alert()
sleep(2)
# confirm.accept()
confirm.dismiss() # 取消