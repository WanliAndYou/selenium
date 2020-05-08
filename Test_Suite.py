# # conding: utf-8
# 测试套件TestSuite介绍
# 简介：讲解测试套件TestSuite的基本介绍和使用场景
#
# 需求：1.利用unittest执行流程测试而非单元测试
#       2.控制unittest的执行顺序
#
# 1.unittest.TestSuite()类来表示一个测试用例集
#     1.用来确定测试用例的顺序，哪个先执行哪个后执行
#     2.如果一个class中有四个test开头的方法，则加载suite中是则有四个测试用例
#     3.有TestLoder加载TestCase到TestSuite
#     4.verbosity参数可以控制执行结果的输出，0.简单报告，1.一般报告，2.详细报告，默认1 会在灭个成功的用例前面加个“.”，每个失败的用例前面加个"F"
#
# 2.TextTestRunner() 文本测试用例运行器