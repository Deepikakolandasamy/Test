
# coding: utf-8

# In[14]:

import unittest
class TestStringMethods(unittest.TestCase):

    def test_unit1(self):
        hour=3
        minute=0
        if (((hour >= 0) & (hour <= 12)) & ((minute >= 0) & (minute <= 60))):
            angle=abs((hour * 30 + minute * 0.5)-(minute * 6))
            self.assertEqual(angle, 90)
    def test_unit2(self):
        hour=3.3
        minute=0
        angle='Enter some interger value'
        self.assertEqual(angle,'Enter some interger value')
    def test_unit3(self):
        hour=''
        minute=''
        angle='Enter some interger value'
        self.assertEqual(angle,'Enter some interger value')
    def test_unit4(self):
        hour=23
        minute=61
        angle='Enter correct time'
        self.assertEqual(angle,'Enter correct time')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

