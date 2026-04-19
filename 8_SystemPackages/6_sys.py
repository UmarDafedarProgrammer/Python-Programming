import sys

print(sys.path)

import CustomPackage as CP # Custom package

a = CP.calculator.addition(4,5)
print(a)

sys.path.append("C:/Users/umard/OneDrive/Desktop/GenerativeAIStudy/Repo/genai_venv/Python-Programming/CustomPackage")

import SubPackage

print(SubPackage.calculatorSub.addition(6,7))

from SubPackage import *

print(addition(6,9))
