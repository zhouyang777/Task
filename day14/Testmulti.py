from calc import Calc
from unittest import TestCase
class TestCalc(TestCase):
    def testmulti1(self):
        a=-6
        b=-6
        c=36
        calc1=Calc()
        s=calc1.multi(a,b)
        self.assertEqual(s,c)
    def testmulti2(self):
        a=6
        b=6
        c=36
        calc2=Calc()
        s=calc2.multi(a,b)
        self.assertEqual(s,c)

    def testmulti3(self):
        a = -6
        b = 6
        c = -36
        calc3 = Calc()
        s = calc3.multi(a, b)
        self.assertEqual(s, c)
    def testmulti4(self):
        a = 0
        b = 6
        c = 0
        calc4 = Calc()
        s = calc4.multi(a, b)
        self.assertEqual(s, c)