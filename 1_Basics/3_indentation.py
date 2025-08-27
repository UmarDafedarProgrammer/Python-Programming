import os

# Python does not use semicolon or braces to group the statements
# Instead, it uses indentation of the statements to group together as a block
# Ideally, 4 spaces or tab can be used for indentation
# Statmenets with same indentation level are grouped together



print("First Statement")

    # print("Second Statement")
r"""
 $ python3 indentation.py 
  File "C:\Users\umard\OneDrive\Desktop\Repo\Python-Programming\Basics\indentation.py", line 10
    print("Second Statement")
IndentationError: unexpected indent
"""
# \ is used for unicode escape seuqence characters like \U so python exeuction would fail
r"""
$ python3 indentation.py 
  File "C:\Users\umard\OneDrive\Desktop\Repo\Python-Programming\Basics\indentation.py", line 13
    \"""
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 38-39: truncated \UXXXXXXXX escape
"""

# first print statement has no indentation, so it is correctly executed.
# second print statement has tab indentation, but it doesn't belong to a new block of code. Python expects the indentation level to be consistent within the same block. This inconsistency causes an IndentationError.