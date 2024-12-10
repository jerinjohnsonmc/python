"""
list.py : list demo
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"





a = [1, 2, 3]
b = [4, 5, 6]

# concatenate lists
c = a + b
print("cat list:", c)

# length
print("length:", len(a))

# slicing
d = c[1:4] 
print("slice :", d)

# nested lists
e = [a, b]
print("nested :", e)

# mutability
a[0] = 99
print("new list:", a)

# append
a.append(70)
print("after append:", a)

# splitting
f = "jerin,johns,nirej"
split_list = f.split(",")
print("split list:", split_list)
