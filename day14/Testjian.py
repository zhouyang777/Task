from calc import Calc
import unittest
class TestCalc(unittest.TestCase):
    def testjian0(self):
        a=6
        b=1
        c=5
        calc0=Calc()
        s=calc0.jianfa(a,b)
        self.assertEqual(c,s)

    def testjian1(self):
        a=-6
        b=-1
        c=-5
        calc1=Calc()
        s=calc1.jianfa(a,b)
        self.assertEqual(c,s)


    def testjian2(self):
        a=5
        b=-1
        c=6
        calc2=Calc()
        s=calc2.jianfa(a,b)
        self.assertEqual(c,s)