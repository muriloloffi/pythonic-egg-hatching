# Immutability

# What does immutability mean?

# Strings in Python are immutable. This means that once a string is created, the
# elements within it can not be changed or replaced.

# I.e.: Once a value is assigned to the string 'selfish', it can not be changed.

selfish = "01234567"  # 01234567

# Erase the comment character '#' from the line below to see the error:
# selfish[0] = "8"  # TypeError: 'str' object does not support item assignment

# The only way to change the value of a string is to reassign it:

new_selfish = "12345678"  # 12345678

new_selfish = "8"  # variable reassigned

print(new_selfish)  # 8

# This is because strings are immutable, and the only way to change them is to reassign
# them.

selfish = selfish + "8"  # 012345678

# This is not the same as changing the value of the string, but rather creating a new
# one and reassigning it. In memory, the old string gets replaced by the new one.
