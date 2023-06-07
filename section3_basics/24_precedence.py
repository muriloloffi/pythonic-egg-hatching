# Operator precedence

print(
    20 - 3 * 4,
    "because in '20 - 3 * 4' the precedence of multiplication is over subtraction",
)

# First parentheses are evaluated
# Then exponentiation
print((20 - 3) + 2**2)

# divisions always output a float
print((5 + 4) * 10 / 2)

# multiplication and division have the same precedence and are
# evaluated from left to right
print(5 + 4 * 10 / 2)
print(5 * 2 / 3)

# Precedence:
# ()
# **
# * /
# + -
