# Variables

# Assigning a value to a variable can be done in two ways in Python:
# using the assignment operator = and using the augmented assignment operator +=.
# Assigning is called binding, because we bind a value to a variable.
user_iq = 190

print(user_iq)


# Best practice is to write variables using:
# - snake_case: all lowercase letters with underscores between words
# - start with lowercase letters or underscores*
# - anything with letters, numbers, underscores
# - variables are case sensitive
# - shouldn't start with numbers
# - shouldn't be a keyword

# *Starting with underscore in python is a convention that means the variable is private

# Some good rules of thumb are:
# to be descriptive with your variable names.
# to use all lowercase letters for variables and all uppercase letters for constants.

# Variables can also be reassigned
user_age = user_iq / 4
a = user_age

print(a)

# Two smalls gotchas with variables:
# - Constants: variables that shouldn't change. usually written in all uppercase
PI = 3.14

# - Dunder variables: variables that start and end with double underscores
# These are usually reserved for Python's internal use and should be left alone

# Finally, multiple variables can be assigned at once
a, b, c = 1, 2, 3

print(a)
print(b)
print(c)
