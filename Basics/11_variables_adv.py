import os

#Python encounters the first statement, it creates an object for the value 5 and makes x reference it. 
# The second statement creates y and references the same object as x, not x itself. 
# This is called a Shared Reference, where multiple variables reference the same object.

x = 10
y = x

print("Values in the variables")
print(x,y)

print("address variables are referencing to")
print(id(x),id(y))

# Multiple variable assignments
# Python allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
a = b = c = 45.67
print(a,b,c)
print(id(a),id(b),id(c))


# Multiple variables assigned with different value
# We can assign different values to multiple variables simultaneously, making the code concise and easier to read.
a1, b1, c1 = 34, 45.345, "String"
print(a1,b1,c1)
print(id(a1),id(b1),id(c1))

# Type of a variable can be identified using type()
print(type(a1), type(b1), type(c1))

# Type casting
a2 = int(b1)
# b2 = float(c1) ### ValueError: could not convert string to float: 'String'
b2 = float(a1)
c2 = str(a1)
# After type casting the value of a2, b2, c2
print(type(a1), type(b1), type(c1))
print(a2,b2,c2)

# delete the variable from the namespace
# this is manual freeing up the memory
# We can remove a variable from the namespace using the del keyword. This effectively deletes the variable and frees up the memory it was using.
del a2
# print(a2) NameError: name 'a2' is not defined. Did you mean: 'a'
# Since, a2 is deleted, it wont be accessed and we will get NameError

# Count Number of Characters in a string
print(f"length of the string: {len(c1)}")