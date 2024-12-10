""" var.py: variables demo. """
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"






# assigning variables and printing them
# integer
a = 400
print("integer:", a)

# floating point
b = 3.14159
print("float:", b)

# complex number
c = complex(5, 7)  
print("complex number:", c)

# string
d = "python assignment"
print("string:", d)

# boolean
e = True
print("boolean:", e)

# determining type

print(type(a))

print(type(b))

print(type(c))

print(type(d))

print(type(e))

# floating point errors

b = b + b + b

print (b)

print ("b * 3 should be 9.42477")

#none keyword

f = None
print (type(f))

# dynamic typing changing values of variables to different type

a = "jery"

print ("a is now a string ",a)