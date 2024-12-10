""" ops.py: operators demo. """
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"




# aithmetic operators

a = 15
b = 4


addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print(addition)         
print(subtraction)      
print(multiplication) 
print(division)            
print(floor_division) 
print(modulus)               
print(exponentiation) 

#comparison


print(a == b)  
print(a != b) 
print(a > b)   
print(a < b)   
print(a >= b) 
print(a <= b) 

#boolean

x = a == b
y = a > b
z = 'J' in "Jery"

print(x and y)  
print(x or y)   
print(not x)    
print (z)