# conding: utf-8
# 脚本名不能用unittest.py
import unittest
from selenium import webdriver
import HTMLTestRunner

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # firefox_driver = webdriver.Firefox()
        # firefox_driver.maximize_window()
        # firefox_driver.get("https://www.baidu.com")
        print("--setUp--")

    def tearDown(self):
        print("--tearDown--")
        print("→"*50)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("1")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("2")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print("3")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite控制TestCase执行顺序
    suite.addTest(TestStringMethods("test_upper"))
    suite.addTest(TestStringMethods("test_isupper"))
    suite.addTest(TestStringMethods("test_split"))

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
    # unittest.main()