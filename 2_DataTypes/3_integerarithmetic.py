import os
import sys

a = 786
b = -678
# List all the methods
for method in dir(int):
    if not method.startswith("__"):
        print(method)

# List all the attributes and methods
print(dir(int))

print("Original Values")
print(a,b)


## Dunder methods/ attributes :(double underscores)
# __abs__()
print()
print("absolute value")
print(a.__abs__()) # equivalent to abs() Returns an absolute value
print(b.__abs__()) # -678 -> 678


# __add__()
print()
print("addition")
print(a.__add__(-b)) # a+b
print(a.__add__(b)) # a+(-b)



# __sub__()
print()
print("subtraction")
print(a.__sub__(-b)) # a-b
print(a.__sub__(b)) # a-(-b)


# __mul__()
print()
print("Multiplication")
print(a.__mul__(-b)) # a*b
print(a.__mul__(b)) # a*(-b)


# Even though both are integers, the result is always a float.
# __truediv__()
print()
print("Division and quotient")
print(a.__truediv__(-b)) # a/b
print(a.__truediv__(b)) # a/(-b)


# Floor division means "division that rounds down to the floors the result to get whole number".
# __floordiv__()
print()
print("Floor Division")
print(a.__floordiv__(-b)) # a//b
print(a.__floordiv__(b)) # a//(-b)


# The __mod__() method defines the behavior of the modulus operator %, which returns the remainder after division.
# __mod__(self, other)
# a % b = a - (a // b) * b
print()
print("modulus/remainder Division")
print(a.__mod__(-b)) # a%b
print(a.__mod__(b)) # a%(-b)


# __divmod__(self, other)
# Returns the tuple of (quotient,remainder) => (a//b,a%b)
print()
print("Floor Division, Modulus")
print(a.__divmod__(-b)) # (a//b,a%b)
print(a.__divmod__(b)) # (a//-b,a%(-b))

