import os

"""
Scope of a Variable
In Python, the scope of a variable defines where it can be accessed in the program. There are two main types of scope: local and global.

Local Variables:
Defined within a function or block, accessible only inside that scope.
Destroyed once the function/block ends.
Temporary, used for short-term data.
Global Variables:
Defined outside functions, accessible throughout the program.
To modify within a function, use the global keyword.
Persist in memory for the program’s duration, useful for shared data.
"""

"""
Python Variables - Python
What is the scope of a variable in Python?
The scope of a variable determines where it can be accessed. Local variables are scoped to the function in which they are defined,
    while global variables can be accessed throughout the program.

Can we change the type of a variable after assigning it?
Yes, Python allows dynamic typing. A variable can hold a value of one type initially and be reassigned a value of a different type later.

What happens if we use an undefined variable?
Using an undefined variable raises a NameError. Always initialize variables before use.
"""

x = 5 # Global Variable

def function_localx():
    x = 10 # Creates a local variable
    print(f"Value of x inside function_localx: {x}")

def function_globalx():
    global x # Indicate function to use the global x variable
    print(f"Value of x inside function_globalx: {x}")
    x = 91
    print(f"Value of x inside function_globalx after modification: {x}")

print(f"Value of global x outside: {x}")
function_localx()
print(f"Value of global x after function_localx: {x}")
function_globalx()
print(f"Value of global x after function_globalx: {x}")