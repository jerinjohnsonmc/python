"""
fun_ex3.py : functions exercise 2
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"


def contains_even(number_list: list) -> bool:
   
    for number in number_list:
        if number % 2 == 0: 
        # checks if remainder is zero
            return True
    return False 


volume_cylinder = lambda radius, height: 3.14159 * radius**2 * height 
#pirsqured multiplied by height



result = contains_even([1, 3, 5, 7, 9])  
print(result)  

result = contains_even([1, 2, 3, 5, 4])  
print(result)  

vol= volume_cylinder(7,9)

print (vol)
