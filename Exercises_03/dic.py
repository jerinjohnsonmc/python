"""
dic.py : dictionary demo
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"



a = {"football": "messi","tennis": "federer","cricket": "kohli","basketball": "leBron"}

print(a)

# add item 
a["swimming"] = "phelps"
print(a)

# edit item
a["tennis"] = "nadal"
print(a)


#keys
print("keys:", a.keys())

# values
print("values:", a.values())

# items
print("items:", a.items())



