# Logical Operators

# Logical operators are used to combine conditional statements.
# and, or, not - are the logical operators in Python.
# Logical operators are complemented by comparison operators, which also behave similarly on short-circuiting.
# i.e. Logical operators can be used to evaluate more than one condition at the same time.
print(1 < 2 < 3 < 4)  # True

# But as soon as one of the condition is false, the whole expression becomes false and the Python interpreter
# stops evaluating the remaining conditions.
print(1 < 2 > 3 < 4)  # False

# The comparison operators are:
# ==, !=, >, <, >=, <=
# equal to, not equal to, greater than, less than, greater than or equal to, less than or equal to
# The logical operators are:
# and, or, not
print(
    not (True)
)  # Although not looks like a function here, it is in fact just operator. In this case, the parentheses are
# just surrounding the operand. It's the same as "not True". Because "not" only accepts one operand, it's
# called an unary operator.
