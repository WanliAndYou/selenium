# coding: utf-8
# 模拟事件处理
# 1.自动化测试使用selenium里面的ActionChains模拟用户的行为
#   需求：需要模拟鼠标操作才能进行的情况，比如单击，双击，点击，拖拽，点击右键
#   解决：selenium里面提供了一个类来处理这类事件
#       from selenium.webdriver.common.action_chains import ActionChains
#   执行原理：调用ActionChains的方法时不会立即执行，会将所有，会将所以的操作放在一个队列里，当调用perprom()方法时，队列会链试，会依次执行
#   执行链试写法或者分布写法
#   ActionChains(driver).click(ele).perform()


# 2.鼠标和键盘方法列表
#     perform() 执行链中的所有动作
#     click(on_element=None) 单击鼠标左键
#     context_click(on_element=None) 单击鼠标右键
#     double_click(on_element=None)  双击鼠标左键
#     move_to_element(to_element)  鼠标移动到某个位置
#     ele_send_keys(keys_to_send)  发送某个词到当前焦点的元素
#     ======不常用=======
#     click_and_hold(on_element=None) 点击鼠标左键，不松开
#     release(on_element=None)  在某个元素位置松开鼠标左键
#     key_up(value, element=None)  按下某个键盘上的键
#     key_up(value, element=None) 松开某个键
#     drag_and_drop(source, target)  拖拽到某个元素然后松开
#     drag_and_drop_by_offset(source, xoffset, yoffset) 拖拽到某个坐标后松开
#     move_to_offset(xoffset, yoffset) 鼠标从当前位置移动到某个坐标
#
#     move_to_element_with_offset(to_element, xoffset, yoffset) 移动到距某个元素（左上角坐标）多少距离的位置

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver