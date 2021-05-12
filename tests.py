import unittest
import unemployment_rate as ur

class TestUnemploymentRateFromJson(unittest.TestCase):

    def testLowest(self):
        df = ur.getSortedDataLow()
        expectedOutput = [2.301867378, 2.498729296, 2.565344859]
        self.assertEqual(df[:3]['value'].tolist(), expectedOutput)
    
    def testLowest(self):
        df = ur.getSortedDataLow()
        expectedOutput = [26.78073067, 26.89014696, 27.2364419]
        self.assertEqual(df[-3:]['value'].tolist(), expectedOutput)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()