"""
my_if.py : if demo
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

a = False
b = False
c = False

if a:
    print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")
    
if (2<3) and (9<5):
    print("Yup!")
else:
    print("Nope!")
