# coding: utf-8
# 鼠标事件实战 hover

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.xdclass.net")
sleep(3)

# 定位鼠标移动到元素上面
menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(3)")
ActionChains(driver).move_to_element(menu_ele).perform()

# 选中子菜单
driver.find_element_by_css_selector(".deep > div:nth-child(3) > a:nth-child(1)").click()