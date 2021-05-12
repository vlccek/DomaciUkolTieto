import unittest
import unemployment_rate as ur

class TestUnemploymentRateFromJson(unittest.TestCase):

    def testLowest(self):
        df = ur.getSortedDataLow()
        expectedOutput = [2.301867378, 2.498729296, 2.565344859]
        self.assertEqual(df[:3]['value'].tolist(), expectedOutput)
    
    def testBiggest(self):
        df = ur.getSortedDataLow()
        expectedOutput = [26.78073067, 26.89014696, 27.2364419]
        self.assertEqual(df[-3:]['value'].tolist(), expectedOutput)

if __name__ == '__main__':
    unittest.main()