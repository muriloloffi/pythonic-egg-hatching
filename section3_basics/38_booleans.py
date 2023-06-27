# Booleans

# classic boolean behavior

name = "Murilo"  # string
is_cool = False  # boolean

is_cool = True

# Booleans can be used to control the flow of a program.
# It's a cornerstone of programming.

if is_cool:  # if is_cool is True
    print("Murilo is cool")
else:
    print("Murilo is not cool")

# A bool conversion function converts values to booleans according to the following rules:
# 1. False, None, 0, "", (), [], {} are all False
# 2. Everything else is True

print(bool(0))  # False
print(bool(1))  # True
print(bool("False"))  # True, because it's a non-empty string
