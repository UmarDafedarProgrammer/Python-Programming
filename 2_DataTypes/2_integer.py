import os
import sys

i = 5
print(type(i))
print(sys.getsizeof(i)) ## int class object size 


# j = int('3.5') ## Value Error as 3.5 is string
j = int(3.5)
print(j)

# Value provided should be whole number. Otherwise it will give ValueError (if other than whole number is provided)
k = int(input("Enter the value of int k ")) 
print(k)


# Size of int object
a = 0
b = 100
c = 10**10
d = 10**100

print(f"Size of a (0): {sys.getsizeof(a)} bytes")
print(f"Size of b (100): {sys.getsizeof(b)} bytes")
print(f"Size of c (10**10): {sys.getsizeof(c)} bytes")
print(f"Size of d (10**100): {sys.getsizeof(d)} bytes")

"""
Method	    Purpose
dir(int)->List of all attributes & methods
help(int)->Documentation and usage
int.__dict__->Class-level namespace dictionary
inspect.getmembers(int)->All members with detail
"""

for method in dir(int):
    if not method.startswith("__"):
        print(method)
