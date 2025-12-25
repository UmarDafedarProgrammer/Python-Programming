# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive (myVar and myvar are different).
# Avoid using Python keywords (e.g., if, else, for) as variable names.

# Dynamic Typing
# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.

var1 = 10
var2 = "value"
var3 = 4.5

print(var1, var2, var3)

var3 = 99

print(var3)

# for = 99
# invalid syntax error: as for is keyword and can not be used as a variable name

_startswithUnderscore = 34

print(_startswithUnderscore)

# Dynamic typed example
# Same variable can hold different type of data during execution
var = 10
print("Here are some examples of Dynamic typing of variable var")
print(var, type(var))

var = 33.33
print(var, type(var))

var = "string"
print(var, type(var)) # Type inferencing type() - > will retrieve the type of object/variable

var = True
print(var, type(var))

# Multiple assignment example
v1, v2, v3 = 10, 33.33, "Test"
v4 = v5 = v6 = 55

print(v1, v2, v3, v4, v5, v6)
