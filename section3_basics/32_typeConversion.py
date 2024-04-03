# Type Conversion

print(str(100), type(str(100)))

print(int(str(100)))
print(type(int(str(100))))
# Same as:

a = str(100)
b = int(a)
c = type(b)
print(c)

# The above are examples of type conversions
# We can convert a strings to integers and vice versa
# But only if the strings are number

d = "3.4"
# print(int(d))  # This will throw an error

invalid_str = "123abc"
# int(invalid_str)  # Raises ValueError: invalid literal for int() with base 10

out_of_range_str = "100000000000000000000000000000000000000000000"
# int(out_of_range_str)  # Raises OverflowError: int too large to convert to long

hex_str = "FF"
hex_int = int(hex_str, base=16)
print(hex_int)  # Output: 255

invalid_base_str = "10101"
# int(invalid_base_str, base=37)  # Raises ValueError: int() base must be >= 2 and <= 36

valid_base = "zzz"
valid_maximum_base = int(valid_base, base=36)
print(valid_maximum_base)
