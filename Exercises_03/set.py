"""
set.py : sets demo
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"



a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print (a,b)

# add 
a.add(6)
print(a)

# remove
a.remove(2)
print( a)

# union
c = a.union(b)
print( c)

# interection
d = a.intersection(b)
print(d)

# diff
e = a.difference(b)
print( e)


# clear
a.clear()
print( a)
