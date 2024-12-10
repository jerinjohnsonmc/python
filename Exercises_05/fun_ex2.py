"""
fun_ex2.py : functions exercise 2
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

def find_num(number_list: list, number: int) -> bool:
    # function loops through a list of numbers and return true if given number is found in list if not it returns None
  
    for iterate_number in number_list:
        if iterate_number == number:  
            return True
        else:
            pass  
			
			
def find_number(number_list: list, number: int) -> bool:
    # function loops through a list of numbers and return true if given number is found in list if not it returns None
  
    for iterate_number in number_list:
        if iterate_number == number:  
            return True
        else:
            return False  
result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)  
result = find_number([1, 2, 3, 4, 5, 6, 7, 8], 9)

print(result) 
