


"""
oo2.py  : python class demo wiith attributes
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"



class MyTemplate():
    # Constructor, called whenever an instance of the class is created.
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752 
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2
        
    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")
        
    def my_method2(self, my_name:str):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")
        
        
# Instantiate the class
my_object = MyTemplate("Jerin", False)
# Check the object and type
print(type(my_object))
print(my_object.class_object_attribute1, my_object.class_object_attribute2)
my_object.my_method1()
my_object.my_method2("Slartibartfast")