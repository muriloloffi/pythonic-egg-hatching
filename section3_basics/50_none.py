# None


# What does none mean? It's a special data type in Python that means "nothing".
# It's a placeholder for something that doesn't exist.
# For example, if we have a function that doesn't return anything, it will return None.
# Let's see an example:
def some_func():
    print("Hi")


# If we call this function, we'll see that it prints "Hi", but it doesn't return
# anything.
# So if we try to print the result of calling this function, we'll get None:
print(
    "some function return: ", some_func()
)  # "Hi", then newline and "None" (without quotes)

# None might be useful when we want to initialize a variable, but we don't know
# what value it should have yet. For example:
some_var = None
