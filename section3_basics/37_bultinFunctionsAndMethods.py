# Built-in Functions and Methods

# Strings have a lot of built-in methods that can be used to modify them.
# One of them being len() which returns the length of the string.

print(
    len("hello world")
)  # Len() counts the length starting from 1, like a human would.

greet = "hellloooo"

print(greet[0 : len(greet)])  # Prints the whole string

# Besides built-in functions, there are also built-in methods.
# A built-in function has the syntax: function_name(argument)
# Methods are similar to functions, but they are owned by objects.
# In Python, strings are objects, and they own a bunch of methods.
# Methods have the syntax: object.method_name(argument), where object is the string.

# Here is a reference on all the string methods: https://www.w3schools.com/python/python_ref_string.asp

quote = "to be or not to be"

print(quote.upper())  # Prints the string in all uppercase
print(quote.capitalize())  # Prints the string with the first letter capitalized
print(quote.rjust(50))
# Prints the string right justified. The argument is the number of spaces to add to
# the left of the string.

print(quote.find("be"))  # Prints the index of the first occurrence of the argument.

print(quote.replace("be", "me"))  # Replaces the first argument with the second.

# If we print quote again, what do you think will happen?

print(quote)  # The original string is not modified.

# Remember: in python, strings are immutable. This means that they cannot be changed.
# If you want to change a string, you have to create a new one.

quote2 = quote.replace(
    "be", "me"
)  # This creates a new string and assigns it to quote2.
