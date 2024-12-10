"""
library1.py : std library demo
"""



__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"


import math
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse to 2 places is: {hypo:1.2f}".format(hypo=c))