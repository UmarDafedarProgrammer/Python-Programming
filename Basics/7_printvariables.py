import os

var1 = "hello"
var2 = var1 ## Is it a Both variables pointing to same memory location
print(id(var1),id(var2)) 
var1 = "Cat" # Now, var1 will point to memory containing cat

print(var1,var2)

print(id(var1),id(var2))