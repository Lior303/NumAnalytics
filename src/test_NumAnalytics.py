'''
Created on Oct 30, 2018

@author: Pavel Shavarchov
'''
import unittest
from NumAnalytics import *
from numpy.ma.testutils import assert_equal, assert_not_equal

class Test(unittest.TestCase):


    def testParsingPoly(self):
        assert(Polynom("x^2")==Polynom([1,0,0]))
        assert(Polynom("x^2")==Polynom('2x^2 -x^2'))
        assert(Polynom("1.1x^3-2")==Polynom([1.1,0,0,-2]))

    
    def testMatrixDecompose(self):
        matrix = Matrix("[1,2;3,4]")
        assert(matrix.decompose()==None)
        assert_not_equal(matrix.decompose('D'),matrix.decompose('U'))
        assert_equal(matrix.decompose('D'),Matrix('[1,0;0,4]'))
        assert_equal(matrix.decompose('U'),Matrix('[0,2;0,0]'))
        assert_equal(matrix.decompose('L'),Matrix('[0,0;3,0]'))
        assert_equal(matrix.decompose('LU'),Matrix('[0,2;3,0]'))
        assert_equal(matrix.decompose('DL'),Matrix('[1,0;3,4]'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()