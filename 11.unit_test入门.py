# conding: utf-8
import unittest
class UserTestCase(unittest.TestCase):

    def setUp(self):
        #初始化
        print("--setUp--")

    def tearDown(self):
        print("--tearDown--")

    def test_name(self):
        # 每次运行都会调用setUp,tearDown
        print("-"*66)
        print("--调用test_name--")

    def test_isuper(self):
        # 每次运行都会调用setUp,tearDown
        print("--调用test_isupper--")

# 入口
if __name__ == '__main__':
    unittest.main()