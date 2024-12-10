"""
my_for.py : for loop demo
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

a = [1,2,3,4,5,6]

for item in a:
    # For each item, execute this code block
    print(item)



# print all even numbers



for item in a:
    if item %2 == 0:
        print(item)
        
total = 0

for item in a:
    total = total + item

print(total)


# Define a string to iterate over
for this_letter in "Jerin Johns":
    # Specify which letter to test for
    if this_letter == "j":
        # Found the test letter
        print(f"Woo hoo, found a {this_letter}!")
        # Exit the current loop
        break
    else:
        # Didn't find the test letter
        print(f"Aww man, I didn't want a {this_letter}!")
        
        
        
my_list = [1,2,3,0]

for my_number in my_list:
    if my_number == 1:
        pass
    if my_number == 2:
        continue
    if my_number == 3:
        print(f"Found the number {my_number}")
    if my_number == 0:
        break




list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
    print(item)  
    
# Tuple unpacking
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
    print(a)  
    print(b)


for index in range(1, 100, 7):
    print(index)