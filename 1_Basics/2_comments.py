import os

# Single line comment [Ignored]

print("Commenting") #Another comment

# Multiple line comments
"""
Comment 1
Comment 2
"""

# Print function taking input text to be printed in multiple lines
print("""
Multiple 
    line inputs to print function
""")

# Print statement, to print to a single line but the input is spread across multiple input lines
print("Checking \
Another way \
of multiple line \
text to be printed on one line")

'This is also a comment ?: yes, as this string literal is not assigned to any variable' 

"Is this also a comment ?: Yes, as this is also not assigned to any variable"

'''
By default, anything included in triple quotes will follow line contination
For an example
'''

"""
By default, anything included in triple quotes will follow line contination
For an example
"""

somevariable='''
Checking for the line continuation
first line
second line
'''

print(somevariable)

print(__doc__)