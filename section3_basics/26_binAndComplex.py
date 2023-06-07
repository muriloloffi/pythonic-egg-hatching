# bin() and complex type

# complex is a third type of number in python. (The other two are int and float)
# e.g.: x = 1j

x = 1j
print(type(x))

# bin() is a function that converts an integer to a binary string prefixed with “0b”.

print(bin(5))

# int() is a function that converts a number or string to an integer.
# we can convert a binary string to an integer by passing 2 as the second
# argument to int().

print(int("0b101", 2))
