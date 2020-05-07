# conding: utf-8
# 查找登录框 =》 输入用户名和密码 =》触发登录 =》 判断登录是否成功 =》打印结果

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.xdclass.net")
driver.maximize_window()
print(driver.title)
# 休眠
# sleep(2)
driver.implicitly_wait(3)

# 登录
login_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.login > span:nth-child(2)")
# 触发点击事件
ActionChains(driver).click(login_ele).perform()

# 查找输入框，账号密码，框需要提前清理
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("17671351006")

driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("Tiamo2020xd")

login_btn = driver.find_element_by_css_selector(".login_btn > span:nth-child(1) > input:nth-child(1)")
ActionChains(driver).click(login_btn).perform()

# 查找登录按钮
driver.find_element_by_class_name("btn").click()

# 判断登录成功
avatar_img = driver.find_element_by_css_selector(".avatar_img")
# try:
#     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(avatar_img))
# except:
#     print("等待时间不足")
#     driver.close()


ActionChains(driver).move_to_element(avatar_img).perform()

# 获取用户名元素
username = driver.find_element_by_class_name("username")
print(username.text)

if username.text == u"wanli":
    print("login OK!")
    sleep(2)
    driver.close()
else:
    print("login Failed!")
    sleep(2)
    driver.close()
