"""
test_formatter.py  : unit testing
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

import unittest


import formatter

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "JERIN JOHNS"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "jerin johns")

    def test_upper(self):
        test_text = "Jerin Johns"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "JERIN JOHNS")

if __name__ =="__main__":
    unittest.main()
