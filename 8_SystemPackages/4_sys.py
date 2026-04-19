import os
import sys

f = open("log.txt","w")
sys.stdout=f

print("Is it writing to the log.txt file?") # writing to the log.txt file

sys.stdout.write("Is it also pointing to the same file ?") # writing to the log.txt file

sys.stderr.write("What about error message") # is not writing to the log.txt file

ferr = open("errorlog.txt","w")
sys.stderr = ferr
sys.stderr.write("What about second error message") # is writing to the errorlog.txt file

sys.exit()