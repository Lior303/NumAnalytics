'''
Created on Oct 30, 2018

@author: Pavel Shavarchov
'''
import unittest
from PolynomHalf import *

class Test(unittest.TestCase):


    def testParsingPoly(self):
        assert(Polynom("x^2")==Polynom([1,0,0]))
        assert(Polynom("x^2")==Polynom('2x^2 -x^2'))
        assert(Polynom("1.1x^3-2")==Polynom([1.1,0,0,-2]))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()