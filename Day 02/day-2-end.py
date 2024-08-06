
# ? Type Error, Type Checking and Type Conversion

# Type Error
# len(1234) # TypeError: object of type 'int' has no len()

# Type Checking
print(type(1234)) # <class 'int'>
print(type(1234.0)) # <class 'float'>
print(type("1234")) # <class 'str'>

# Type Conversion
num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters.")
print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100