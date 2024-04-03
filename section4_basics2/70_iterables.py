# In Python, iterating over some data structure is a common vocabulary.
# An iterable is an object that can be iterated over. For example, a list is an
# iterable.
# The for loop is used to iterate over an iterable.
# For example, let's take the object User.

user = {"name": "Golem", "age": 5006, "can_swim": False}

print("\nExample 1:", end="\n\n")
for item in user:
    print(item)  # This will print the keys of the dictionary
# This is because the standard method for iterating over dictionaries is the
# keys() method.
# That is, the above loop is equivalent to:
# for item in user.keys():
#    print(item)

# If we want to iterate over the values, we need to use the values() method.

print("\nExample 2:", end="\n\n")
for item in user.values():
    print(item)  # This will print the values of the dictionary

# If the wanted output is the key and the value, we need to use the items()
# method.

print("\nExample 3:", end="\n\n")

for item in user.items():
    print(item)  # This will print the key and the value of the dictionary as a
# tuple. And if we want to unpack the tuple, we can do:

print("\nExample 4:", end="\n\n")

for item in user.items():
    key, value = item
    print(key, value)  # This will print the key and the value of the dictionary

# Or we can do:

print("\nExample 5:", end="\n\n")

for key, value in user.items():
    print(
        key, ": ", value, sep=""
    )  # This will print the key and the value of the dictionary
# In this case, we can use the sep="" argument to remove the space between the
# key and the value and deliver the output as we want.
