import unittest
import Assignment.primesInRange as primesInRange

class PrimeInRangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# Sample happy path test
    def test100_100_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 2
        highBound = 10
        expectedResult = [2, 3, 5, 7]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
# Happy path tests

    def test010_ShouldDeterminePrimesInLowerRange(self):
        lowBound = 2
        highBound = 32
        expectedResult = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)

    def test020_ShouldDeterminePrimesInMidRange(self):
        lowBound = 500
        highBound = 530
        expectedResult = [503, 509, 521, 523]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test030_ShouldDeterminePrimesInUpperRange(self):
        lowBound = 970
        highBound = 1000
        expectedResult = [971, 977, 983, 991, 997]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test040_ShouldReturnNoPrimes(self):
        lowBound = 444
        highBound = 448
        expectedResult = []
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test050_ShouldReturnConsecutivePrimes(self):
        lowBound = 2
        highBound = 3
        expectedResult = [2, 3]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    
    def test060_ShouldTestEqualLowBoundHighBound(self):
        lowBound = 701
        highBound = 701
        expectedResult = [701]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        

# Sad path tests

    def test910_ShouldTestNonIntegerLowBound(self):
        lowBound = 0.4
        highBound = 10
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        
    def test920_ShouldTestNonIntegerHighBound(self):
        lowBound = 2
        highBound = 11.6
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        
    def test930_ShouldTestLowBoundOutOfRange(self):
        lowBound = 1
        highBound = 10
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)

    def test940_ShouldTestHighBoundOutOfRange(self):
        lowBound = 990
        highBound = 1001
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        
    def test950_ShouldTestLowBoundGreaterThanHighBound(self):
        lowBound = 500
        highBound = 490
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        

        