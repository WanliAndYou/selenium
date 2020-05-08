# conding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.xdclass.net")
driver.implicitly_wait(10)
print(driver.title)

login = driver.find_element_by_css_selector(".login > span:nth-child(2)")
ActionChains(driver).click(login).perform()
# 捕捉找不到的元素截图
try:
    driver.find_element_by_css_selector(".mobienum > input:nth-child(100)").click()
except:
    driver.get_screenshot_as_file(r"C:\Users\WenFangquan\Desktop\error.png")
finally:
    time.sleep(2)
    driver.close()


