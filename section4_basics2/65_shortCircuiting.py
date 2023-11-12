# Short circuiting

# When evaluating logical expressions, the Python interpreter may take the following shortcuts:
#   - For an OR expression, if the first operand is True, then the entire expression must be True,
# so the second operand is not evaluated.
#  - For an AND expression, if the first operand is False, then the entire expression must be False,
# so the second operand is not evaluated.
# This is called short circuiting.

# Short circuiting can be used to avoid errors in expressions that would otherwise cause errors.
# For example, if we want to check if a list is not empty and then access the first element, we can
# use the following expression:
# if len(my_list) > 0 and my_list[0] == 1:
#    print("my_list is not empty and the first element is 1")
# If my_list is empty, then the expression my_list[0] would cause an error.
# Because of short circuiting, the second operand of the AND expression is not evaluated if the first
# operand is False, so the error is avoided.
