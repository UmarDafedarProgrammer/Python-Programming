# Escape Characters
# Provide the special meaning to the characters within the double and single quotes
# \n - LineFeed (Go to the next line)
# \f - form feed (Page seperator)
# \r - Carriage Return (Return to the beginning of the line without advancing downward)
# \t - tab seperator (4 or 8 space depends up on the operating system)
# \\ - backslash
# \' - Single Quote
# \" - Double quote
# \ooo - Octal Number
# \xhh - hexa decimal number

print('\\n -Next line\nnext line')
print('\\t -Write data\twith tab space sepetated.')

print('\"Double Quotes\"')
print("\"Double Quotes\"")
print('"Double Quotes"')
print("'Single Quote'")
print('\'Single Quote\'')
print("\'Single Quote\'")
print('\\b - \bbackspace')
print('\\r - carriage\r return\rOverwriting the previous ones') #overwrites the first printed line with next one
# its better to use \n instead of \r
print('backslash followed by three integers will result in a octal value: \100\101\102')
txt = "\x48\x65\x6c\x6c\x6f"
print("A backslash followed by an 'x' and a hex number represents a hex value:",txt) 
print("What is form feed \fchecking")