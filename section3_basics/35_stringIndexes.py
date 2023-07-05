# String indexes

# For the string below
selfish = "me me me"
# each character has an index: 0; 1; 2; 3; 4; 5; 6; 7;

# If we access the index 0, we get the first character
print(selfish[0])

# Python has a feature that allows to grab different parts of a string
# This is called slicing, the operator is a colon:
# [start:stop:stepover]
# The stop is not inclusive, so the character at the stop index is not included

print(selfish[0:2])  # This will print characters 0 and 1

numbers = "01234567"

# Slicing allows for stepover, which is the number of characters to skip
print(numbers[0:8:2])  # This will print every third character

print(numbers[1:])  # This will print from the second character to the end

print(numbers[:5])  # This will print from the beginning to the fifth character

print(numbers[::1])  # This will print the whole string

print(numbers[-1])  # This will print the last character
# In python, negative indexes start from the end of the string

# A neat common operation is to reverse a string, this can be achieved with:
print(numbers[::-1])
