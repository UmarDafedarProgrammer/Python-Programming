r"""
end:
by default the end character is next line \n. 
However, developer can assign any character or string as the end line
end must be None, or a string and not int/number

sep:
seperator, this separates the inputs provided to print with separator
"""
print(1,2,3,end="*") # -> 1 2 3*
print('.com')  # -> 1 2 3*.com

print(1,3,4,sep='/',end='@') #-> 1/3/4@