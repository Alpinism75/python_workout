#! /usr/bin/env python

# Unit Test for chpt1_numbers.py  - Not used yet.

import unittest

class Block(unittest.TestCase):
    
    def test_name(self):
        s = 'Name1'
        self.assertIn(s)

    def test_script(self):
        self.assertEqual(50)
        self.assertIsInstance(square(3), int)


    def test_values(self):
        self.assertRaises(ValueError, "blah")
    

if __name__ == '__main__':
    unittest.main()