import os # allows a program to interact with an opeating system
import sys # allows a program to interact with an intepreter


l = len(sys.argv)

if l > 1:
    for i in sys.argv:
        print(i)
    
    for j in range(l):
        print(sys.argv[j])

print(sys.argv)


print(sys.path) # would tell me the path from where it is reading the imports

sys.stdout.write("Validatintg the console output") # print() is just a wrapper to sys.stdout.write("text\n") 
sys.stdout.write("Validatintg the console output2\n")
sys.stdout.write("Validatintg the console output3\n")

sys.stderr.write("Error Message \n")
sys.exit(0) # exit the program with program code of 0