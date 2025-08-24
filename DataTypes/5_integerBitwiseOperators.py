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