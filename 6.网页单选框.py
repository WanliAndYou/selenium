# conding: utf-8

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
# 休眠几秒在选下一个单选框和多选框
driver.find_element_by_id("femail").click()