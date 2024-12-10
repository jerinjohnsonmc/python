"""
list_comp.py : list comprehension exercise
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"



conversion_c = 273.15
temp_in_kelvin = [313, 303,301, 300, 298, 295, 294, 293, 283, 273]
temp_in_celsius = [value - conversion_c for value in temp_in_kelvin]
temp_in_farenheit = [value * 9/5 + 32 for value in temp_in_celsius]



print("Temperatures in Kelvin:", temp_in_kelvin)
print("Temperatures in Celsius:", temp_in_celsius)
print("Temperatures in Fahrenheit:", temp_in_farenheit)
