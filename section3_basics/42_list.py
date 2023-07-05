# List data type

# Lists are an ordered sequence of objects that can be of any type.
# They are mutable, which means that you can change their content without changing
# their identity. You can recognize lists by their square brackets [ and ] that hold
# elements, separated by a comma ,. Lists are built into Python: you do not need to
# invoke them separately.

# For instance, you can create a list of integers as follows:

li = [1, 2, 3, 4, 5]

# Or a list of strings:

li2 = ["a", "b", "c"]

# Also possible are lists of mixed items:

li3 = [1, "a", "string", True]

# And list of lists:
li4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# If coming from a different programming language, you can think of lists as arrays.

# This is the first data structure we will look at. We will see that lists are very
# versatile and can be used in many different ways.

# Taking another example, if we had a shopping cart, we could store the items in a list:

amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]

print(len(amazon_cart))  # This will print the first item in the list

print(
    """personal note here: I am not sure whether len() is the most genius or non-sense
    way a programming language implements item counting from different data types."""
)
