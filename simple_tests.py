import unittest
import time

class SimpleTests(unittest.TestCase):

    
    def test_should_succeed(self):
        assert 7 == 7
        
    def test_old_print_syntax(self):
        print "This should succd in Python 2.x, but not 3.x try again"

if __name__ == "__main__":
    unittest.main()
