
"""
oo1.py  : python class demo
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

# Create a class 
class JJClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JJClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)
		
		
class test_even():
    def __init__(self, my_num):
        print("Running constructor for test_even")
        # Create attributes and set initial values
        self.num = my_num

    def even_method(self):
        if self.num %2 == 0:
            return True
        return False
		

my_class1 = JJClass("Good Morning!")
my_class1.my_method()
print(type(my_class1))

my_class2 = test_even(5)
a=my_class2.even_method()
print (a)
print(type(my_class2))