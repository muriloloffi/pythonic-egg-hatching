# List unpacking

# With list unpacking it's possible to assign each item in a list to a variable.
a, b, c, d = [1, 2, 3, 4]
print(a)
print(b)
print(c)

# It's not the same as assigning multiple variables at once, because in unpacking we're
# iterating over the list.
a, b, c = 1, 2, 3  # multiple assignment
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # other is a list
print(other)
