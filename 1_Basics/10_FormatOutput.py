
# Using % Operator
# We can use '%' operator. % values are replaced with zero or more value of elements. 
# The formatting using % is similar to that of ‘printf’ in the C programming language.

# %d –integer
# %f – float
# %s – string
# %x –hexadecimal
# %o – octal

i1 = 10
f2 = 3.456
f3 = 345.56777
s3 = "string"
b4 = True

print("value of i %d" %i1)
print("value of f %f" %f2)
print("value of .2f %.2f" %f2)
print("value of .3f %.3f %f %.10f" %(f3, f3, f3))
print("value of s %s" %s3)
print("value of hexadecimal i %x" %i1)
print("value of octal i %o" %i1)