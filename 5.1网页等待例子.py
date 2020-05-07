# conding: utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
# driver.get("http://www.xdclass.net")
driver.get("https://www.baidu.com")
driver.maximize_window()
# 强制等待
# sleep(5)

# 隐性等待
# driver.implicitly_wait(5) # 设置一次即可
# print(driver.title)

# 显性等待
try:
    # presence_of_element_located 检查网络元素出现
    ele = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
    if ele:
        print("元素加载成功")
    print(driver.title)
except:
    print("资源加载失败")
finally:
    driver.close()

