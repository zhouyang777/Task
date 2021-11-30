'''
1,准备数据
2，执行用例
3.对比结果，分析结果，得出结果
2.1 本身自带测试：unittest
2.2 测试用例类继承 unittest.TestCase
2.3 写测试用例  2.testXXXX

'''

from calc import Calc
import unittest
class TestCalc(unittest.TestCase):
    def testAdd(self):
        a=6
        b=5
        c=11
        calc0=Calc()
        s=calc0.add(a,b)
        self.assertEqual(c,s)
    def testAdd1(self):
        a=-6
        b=-7
        c=-13
        calc1=Calc()
        s=calc1.add(a,b)
        self.assertEqual(c,s)
    def testAdd2(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        result = calc.add(a,b)

        self.assertEqual(result,c)

    def testAdd3(self):
        a = 5
        b = -5
        c = 0

        calc = Calc()
        result = calc.add(a,b)

        self.assertEqual(result,c)


    def testAdd4(self):
        a = -5
        b = -5
        c = -10

        calc = Calc()
        result = calc.add(a,b)

        self.assertEqual(result,c)

    def testAdd4(self):
        a = 50000
        b = 5
        c = 50005

        calc = Calc()
        result = calc.add(a,b)

        self.assertEqual(result,c)




# from calc import Calc
# #1,准备数据
# a=6
# b=5
# c=11
#
# #2.执行用例
# calc0=Calc()
# s=calc0.add(a,b)
#
# #3,对比期望数据和实际数据
# if c==s:
#     print("用例通过！")
# else:
#     print("用例不通过")