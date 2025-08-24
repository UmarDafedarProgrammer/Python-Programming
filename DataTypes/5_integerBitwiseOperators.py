import os

### Bit wise operators
# OR
# AND
# INVERT
# XOR
# LSHIFT
# RSHIFT

A = 18
B = 10

AorB = A.__or__(B)
AandB = A.__and__(B)
Ainvert = A.__invert__()
AxorB = A.__xor__(B)

print(AorB)
print(AandB)
print(Ainvert) # 2s complement+1 with negative sign
print(AxorB)

Alshift = A.__lshift__(1)
Arshift = A.__rshift__(1)

print(Alshift)
print(Arshift)

Alshift = A.__lshift__(2)
Arshift = A.__rshift__(2)
print(Alshift)
print(Arshift)

def printBitwiseOperators(A, B):
    print(f"A: {A}, B: {B}")
    print(f"A | B: {A | B}")
    print(f"A & B: {A & B}")
    print(f"A ^ B: {A ^ B}")
    print(f"~A: {~A}")
    print(f"A << 1: {A << 1}")
    print(f"A >> 1: {A >> 1}")
    print(f"A << 2: {A << 2}")
    print(f"A >> 2: {A >> 2}")

def addBitwiseOperators(A, B):
    AorB = A | B
    AandB = A & B
    Ainvert = ~A
    AxorB = A ^ B
    Alshift = A << 1
    Arshift = A >> 1

    Alshift2 = A << 2
    Arshift2 = A >> 2
    return AorB, AandB, Ainvert, AxorB, Alshift, Arshift, Alshift2, Arshift2

if __name__ == "__main__":
    printBitwiseOperators(A, B)
    results = addBitwiseOperators(A, B)
    print("Results from addBitwiseOperators:", results)
    print("Current working directory:", os.getcwd())
    print("File path:", __file__)
    print("File name:", os.path.basename(__file__))
    print("Directory name:", os.path.dirname(__file__)) 
    print("Absolute file path:", os.path.abspath(__file__))
    print("File exists:", os.path.exists(__file__))
    print("Is file a directory?", os.path.isdir(__file__))
    print("Is file a file?", os.path.isfile(__file__))
    print("File size:", os.path.getsize(__file__), "bytes")
    print("Last modified time:", os.path.getmtime(__file__))
    print("Creation time:", os.path.getctime(__file__))
    print("File permissions:", oct(os.stat(__file__).st_mode))
    print("File owner:", os.stat(__file__).st_uid)  
    print("File group:", os.stat(__file__).st_gid)
    print("File inode:", os.stat(__file__).st_ino)
    print("File device:", os.stat(__file__).st_dev)
    print("File links:", os.stat(__file__).st_nlink)
    print("File access time:", os.path.getatime(__file__))
    print("File type:", "Directory" if os.path.isdir(__file__) else "File")
    print("File name without extension:", os.path.splitext(os.path.basename(__file__))[0])
    print("File extension:", os.path.splitext(os.path.basename(__file__))[1])
    print("File path components:", os.path.split(__file__))
    print("File path split:", os.path.split(__file__))
    print("File path normalized:", os.path.normpath(__file__))
    print("File path absolute:", os.path.abspath(__file__))
    print("File path relative to current directory:", os.path.relpath(__file__))
    print("File path exists:", os.path.exists(__file__))
    print("File path is absolute:", os.path.isabs(__file__))
    print("File path is relative:", not os.path.isabs(__file__))
    print("File path is a symlink:", os.path.islink(__file__))
    print("File path is a mount point:", os.path.ismount(__file__))
    print("File path is writable:", os.access(__file__, os.W_OK))
    print("File path is readable:", os.access(__file__, os.R_OK))
    print("File path is executable:", os.access(__file__, os.X_OK))
    print("File path is a regular file:", os.path.isfile(__file__))
    print("File path is a directory:", os.path.isdir(__file__))
    print("File path is a symbolic link:", os.path.islink(__file__))
    print("File path is a block device:", os.path.exists(__file__) and os.stat(__file__).st_mode & 0o60000 == 0o60000)
    print("File path is a character device:", os.path.exists(__file__) and os.stat(__file__).st_mode & 0o20000 == 0o20000)
    print("File path is a socket:", os.path.exists(__file__) and os.stat(__file__).st_mode & 0o140000 == 0o140000)
    print("File path is a FIFO:", os.path.exists(__file__) and os.stat(__file__).st_mode & 0o10000 == 0o10000)
    print("File path is a hard link:", os.path.exists(__file__) and os.stat(__file__).st_nlink > 1)
    print("File path is a symbolic link target:", os.path.islink(__file__) and os.path.exists(os.readlink(__file__)))
    print("File path is a symlink to a directory:", os.path.islink(__file__) and os.path.isdir(os.readlink(__file__)))
    print("File path is a symlink to a file:", os.path.islink(__file__) and os.path.isfile(os.readlink(__file__)))
    print("File path is a symlink to a block device:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o60000 == 0o60000)
    print("File path is a symlink to a character device:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o20000 == 0o20000)
    print("File path is a symlink to a socket:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o140000 == 0o140000)
    print("File path is a symlink to a FIFO:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o10000 == 0o10000)
    print("File path is a symlink to a hard link:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_nlink > 1)
    print("File path is a symlink to a regular file:", os.path.islink(__file__) and os.path.isfile(os.readlink(__file__)))
    print("File path is a symlink to a directory:", os.path.islink(__file__) and os.path.isdir(os.readlink(__file__)))
    print("File path is a symlink to a symbolic link:", os.path.islink(__file__) and os.path.islink(os.readlink(__file__)))
    print("File path is a symlink to a block device:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o60000 == 0o60000)
    print("File path is a symlink to a character device:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o20000 == 0o20000)
    print("File path is a symlink to a socket:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o140000 == 0o140000)
    print("File path is a symlink to a FIFO:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o10000 == 0o10000)
    print("File path is a symlink to a hard link:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_nlink > 1)
    print("File path is a symlink to a regular file:", os.path.islink(__file__) and os.path.isfile(os.readlink(__file__)))
    print("File path is a symlink to a directory:", os.path.islink(__file__) and os.path.isdir(os.readlink(__file__)))
    print("File path is a symlink to a symbolic link:", os.path.islink(__file__) and os.path.islink(os.readlink(__file__)))
    print("File path is a symlink to a block device:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o60000 == 0o60000)
    print("File path is a symlink to a character device:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o20000 == 0o20000)
    print("File path is a symlink to a socket:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o140000 == 0o140000)
    print("File path is a symlink to a FIFO:", os.path.islink(__file__) and os.stat(os.readlink(__file__)).st_mode & 0o10000 == 0o10000)
    