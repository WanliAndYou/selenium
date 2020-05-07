# conding: utf-8
# 1.为什么需要等待时间：页面需要加载对应的资源文件，页面渲染，窗口处理等等
# 2，自动化测试常用的等待时间
    # 2.1 强制等待：time.sleep()
    # 2.2 隐性等待：
        # driver.implicitly_wait(10) # 隐性等待，最长等10秒
        # 设置了一个最长等待时间，如果在规定的时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
        # 弊端：程序一直等待整个页面加载完成，到浏览器标签不在转圈,根据网络情况

        # 注意：对driver起作用，所有只要设置一次即可，没有必要到处设置

    # 2.3 显性等待
        # WebDriverWait 需要配合
        # until和until_not,程序没隔N秒检查一次，如果成功，则执行下一步，否则继续等待，直到超过设置的最长时间
        from selenium.webdriver.support.wait import WebDriverWait

        # 语法：
        # WebDriverWait(driver=FifFoxdriver, timeout=10, poll_frequency=0.5, ignored_exceptions=None) # ignored_exceptions这里忽略异常
# 3.隐性，显性可以同时时间