# _*_ coding: utf-8 _*_
# 打开网页前需要将 geckodriver.exe 驱动放到浏览器同级目录

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

# 百度
# driver.get("https://www.baidu.com")
# 小D
driver.get("https://xdclass.net")
sleep(3)
print(driver.title)
print(driver.current_url)

# 元素唯一

# 1.name 定位
# driver.find_element_by_name("wd").send_keys("小D课堂")
# driver.find_element_by_id("su").click()

# 2.class_name定位
# driver.find_element_by_class_name("s_ipt").send_keys("小D课堂")
# driver.find_element_by_id("su").click()

# 3.id 定位
# driver.find_element_by_id("kw").send_keys("小D课堂")
# driver.find_element_by_id("su").click()

# 不常用
# 4.标签定位   tag name: find_element_by_tag_name 通过标签名定位，如 find_element_by_tag_name("div)
# 5.超链接内容定位 link_text: find_element_by_link_text("视频学习").click()
# driver.find_element_by_link_text("视频学习").click()
# 6.超链接内容模糊查询定位 partial link text:
# driver.find_element_by_partial_link_text("视频学习").click()

# 7. CSS 定位
# 7.1  driver.find_element_by_css_selector()
# 根据css 属性定位，一般class 是用点（.）标记，id 是用井（#）标记
# css 规则 元素[属性=值] 如：input[id=\'search\']
#
# driver.find_element_by_css_selector(".nav_item > li:nth-child(2)").click()
# print(driver.title)
# sleep(2)
# driver.find_element_by_css_selector(".courselist > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)").click()

# 8.Xpath 定位
# 8.1 xpath 语法  // 全文扫描，/ 相对路径，* 所以元素， . 当前节点
# 8.2 xpath
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/ul/li[2]").click()
print(driver.title)
sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/a[2]/div/img").click()