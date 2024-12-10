"""
fun_ex1.py : functions exercise 1
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

def divisible(numerator: int, denominator: int)->bool:

# checking if the numerator is divisible by the denominator by using the modulus operator and evaluating the remainder is zero or not.


    return numerator % denominator == 0
# The modulus operator % calculates the remainder and if it is 0, returns true

print(divisible(30,4))

# any numerator which is perfectly divisible by denominator will return true

