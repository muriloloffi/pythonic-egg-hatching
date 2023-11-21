# for Loops

# for loops are used to iterate through a sequence (list, tuple, string) or
# other iterable objects.

for item in "Zero to Mastery":
    print(item)

# item is a variable that represents each item in the string 'Zero to Mastery'.
# Strings are iterable objects, so we can iterate through each character in it.
# The variable name can be anything you want. The following code will produce
# the same result:

for i in "Zero to Mastery":
    print(i)

# It is also possible to iterate through a list:

for item in [1, 2, 3, 4, 5]:
    print(item)

# Finally, it is possible to nest iteration inside iteration:

for item in [1, 2, 3, 4, 5]:
    for x in ["a", "b", "c"]:
        print(item, x)
