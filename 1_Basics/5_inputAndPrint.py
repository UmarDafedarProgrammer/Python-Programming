
"""
Python's input() function is used to take user input. By default, it returns the user input in form of a string. 
"""
print("Let us try to read the input from the user")

inputvalue = input("Please, enter the input value: ")
print(inputvalue)

# inputint = input("Pleas, enter the integer value: ")
# inputint = inputint + 5
# print(inputint)

r"""
Traceback (most recent call last):
  File "C:\Users\umard\OneDrive\Desktop\Repo\Python-Programming\Basics\5_inpoutANDprint.py", line 11, in <module>
    inputint = inputint + 5
               ~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
"""


# As we already know the input is read as a string value. We need to do the explicit casting if we are expecting other values
# Typecast is required to convert the data before use if required
inputint = int(input("Pleas, enter the integer value: "))
inputint = inputint + 5
print(inputint)

# Lets read multiple values from the input
r"""
Please, enter the quantity and price: 45 68 97
Traceback (most recent call last):
  File "C:\Users\umard\OneDrive\Desktop\Repo\Python-Programming\Basics\5_inpoutANDprint.py", line 30, in <module>
    int_var, float_var = input("Please, enter the quantity and price: ")
    ^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 2)
"""
# int_var, float_var = input("Please, enter the quantity and price: ")
int_var, float_var = input("Please, enter the quantity and price: ").split() 
print(int_var, float_var)


r"""
Please, enter the quantity and price: 67
Traceback (most recent call last):
  File "C:\Users\umard\OneDrive\Desktop\Repo\Python-Programming\Basics\5_inpoutANDprint.py", line 39, in <module>
    int_var, float_var = input("Please, enter the quantity and price: ").split()
    ^^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 1)
"""

int_var, float_var = input("Please, enter the quantity and price: ").split('/')  # Returns a list
print(int_var, float_var)


var = list(input("Please, enter the quantity and price: "))
print(type(var))
print(var)