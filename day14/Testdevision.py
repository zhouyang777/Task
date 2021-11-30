from unittest import TestCase
from calc import Calc
class TestCalc(TestCase):
    def testdev1(self):
        a=5
        b=1
        c=5
        calc1=Calc()
        s=calc1.devision(a,b)
        self.assertEqual(c,s)
    def testdev1(self):
        a=-80
        b=0
        c=0
        calc1=Calc()
        s=calc1.devision(a,b)
        self.assertEqual(c,s)

    def testdev1(self):
        a=-80
        b=8
        c=-10
        calc1=Calc()
        s=calc1.devision(a,b)
        self.assertEqual(c,s)

    def testdev1(self):
        a=-10
        b=-10
        c=1
        calc1=Calc()
        s=calc1.devision(a,b)
        self.assertEqual(c,s)
