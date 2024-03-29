# Dictionary Methods

# Recap: dictionaries are mutable, unordered, and have to have unique keys.
# Let's see some methods that we can use with dictionaries.

user = {"basket": [1, 2, 3], "greet": "hello"}

# Do the user have an age key?
# print(user("age"))  # KeyError: 'age' # type: ignore
# Errors are not good, it's gonna stop our program.

# To access a key in a dictionary, we can use the get method without throwing an error
# if the key doesn't exist.
print(user.get("age"))  # None

# One less common way to create a dictionary is using the dict() object or its
# fromkeys method.
user2 = dict(name="JohnJohn", age=0)
print(user2)  # {'name': 'JohnJohn', 'age': 0}

user3 = dict.fromkeys(["name", "age", "height"])  # There's an optional second argument,
# which defaults to None, that sets the value used for the keys. Note that the same
# object passed as argument is used for all keys. That can cause reference problems with
# mutable objects.
print(user3)  # Values are None by default

# To overcome the problem of having mutable objects as default values, we can use a dict
# comprehension, as shown below.
user4 = {
    value: None
    for value in ["name", "age", "height", "basket", "greet", "inventory", "status"]
}
print(user4)  # No more reference problems
