

'''
Docstring example 
slicing.py: slicing strings demo.

by : JJ
purpose demostrate string manipulation in python



'''

"""
another way of commenting
"""

# file header dunder variables
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

#slicing
a = "Jerin Johns"
b = a[0:11:6]
c = a[-1:-12:-1]
d = a [0:11:2]
e = a[6]
print ("initials", b)

print ("funny" , d)

print ("reverse",c)

print (e)

amalagam = a + b + c + d + e


#interpolation  this is a comment in single line
print ("Good morning {}". format (a))

f = "good morning"

print ("message: {first}{second}".format (first=a,second=f))

print (f"message {a} {f}")
#escape sequence
print (b, a, end = " ") 
print (c)

print (f"{b} {a} \n {c}") 
#functions

print ("length",len(a))

print (a.upper())

print (c.lower())

print (a.replace(" ",""))