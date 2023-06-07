# Operator precedence

print(
    20 - 3 * 4,
    "because 20 - 3 * 4 has the precedence of multiplication over subtraction",
)
print((20 - 3) + 2**2)
print((5 + 4) * 10 / 2)  # divisions always output a float

# Precedence:

# ()
# **

print((5 + 4) * 10 / 2)  # divisions always output a float
print(
    5 + 4 * 10 / 2
)  # multiplication and division have the same precedence and are evaluated from left to right

# Precedence:
# ()
# **
# * /
# + -
