"""
class_template.py  : python class demo wiith attributes
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

import telnetlib
# In any complex application, create a base class which will never be instantiated.
class Device():
    
    # Define a class object attribute, the same for any instance of the class
    ip_type = IPV4

    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for base class")
        # Create attributes and set initial values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def connect(self, host:str)->int: 
        print("connecting to ")
        tn = telnetlib.Telnet(host)
        
        return tn
        
# Create child class which can access the methods and properties of the base class
class Firewall(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""
    
    def configure_firewall(self):
        print("Configuring Firewall")

    def connect(self, host:str)->int: 
        print("connecting to ",host)
        tn = telnetlib.Telnet(host)
        
        return tn
        
class Switch(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""
    
    def configure_switch(self):
        print("Configuring Switch")

    def connect(self, host:str)->int: 
        print("connecting to ",host)
        tn = telnetlib.Telnet(host)
        
        return tn