"""
expo.py : example package
"""


expo_text = "exponent time"

def expo(x):
    return x**x

# Uncomment to test
print(expo(2))


if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")