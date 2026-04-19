import sys

original = sys.stdout

sys.stdout = open("file.txt","w")
print("Saving the text to file.txt")

sys.stdout = original

print("Writing back to console")

sze = sys.getsizeof(10) # Size of integer objects
print(sze)