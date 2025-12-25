"""
Python input() : practical walkthrough
--------------------------------------
This file is meant to be RUN, not just read.

It walks through common input() scenarios one by one.
Each section pauses so you can see the output clearly.

How to use:
1. Run the file
2. Follow the prompts in the terminal
3. Read the comments to understand what is happening

"""

print("\n--- Python input() complete walkthrough ---\n")

# ------------------------------------------------------------
# 1. Basic input
# ------------------------------------------------------------
name = input("1) Enter your name: ")
print("Hello", name)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 2. input() always returns a string
# ------------------------------------------------------------
value = input("2) Enter any value: ")
print("You entered:", value)
print("Type of value:", type(value))

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 3. Integer input (with conversion)
# ------------------------------------------------------------
age = int(input("3) Enter your age: "))
print("Next year you will be", age + 1)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 4. Float input
# ------------------------------------------------------------
price = float(input("4) Enter price: "))
print("Price with tax:", price * 1.18)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 5. Multiple inputs (space separated)
# ------------------------------------------------------------
a, b = map(int, input("5) Enter two numbers (space separated): ").split())
print("Sum:", a + b)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 6. List input
# ------------------------------------------------------------
numbers = list(map(int, input("6) Enter numbers for a list: ").split()))
print("List:", numbers)
print("Sum:", sum(numbers))

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 7. Boolean input
# ------------------------------------------------------------
flag_input = input("7) Enter True or False: ").strip().lower()
flag = flag_input == "true"
print("Boolean value:", flag)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 8. Empty input handling
# ------------------------------------------------------------
text = input("8) Enter something (or just press Enter): ")
if text == "":
    print("No input provided")
else:
    print("You entered:", text)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 9. Input with validation using loop
# ------------------------------------------------------------
while True:
    try:
        num = int(input("9) Enter a valid integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("That was not a valid integer. Try again.")

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 10. Dictionary input
# ------------------------------------------------------------
data = {}
count = int(input("10) How many key-value pairs? "))

for i in range(count):
    key = input(f"  Enter key {i + 1}: ")
    value = input(f"  Enter value {i + 1}: ")
    data[key] = value

print("Dictionary:", data)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 11. Input until exit word
# ------------------------------------------------------------
print("11) Type messages (type 'exit' to stop)")
while True:
    msg = input("> ")
    if msg.lower() == "exit":
        break
    print("You typed:", msg)

input("Press Enter to continue...\n")

# ------------------------------------------------------------
# 12. Secure password input
# ------------------------------------------------------------
import getpass
password = getpass.getpass("12) Enter password (hidden): ")
print("Password received (not displayed for security)")

print("\n--- End of walkthrough ---")
print("You have executed all major input() scenarios successfully.")
