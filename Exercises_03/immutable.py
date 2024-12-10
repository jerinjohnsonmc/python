"""
immutable.py : verify tuple immutability
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

#tuple
a = (1, 2, 3, 4, 5, 6, 1)



# count
c = a.count(1)  
print("count is ", c)

# index
d = a.index(3)  
print("index of 3 is ", d)



try:
    # change a value in the tuple
    a[1] = 4
except TypeError as e:
   
    print("Error:", e)

# print tuple again
print(a)
