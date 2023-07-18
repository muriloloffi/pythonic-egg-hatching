# Dictionary Methods (Second Part)
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

# Just like in lists, we can use 'in' to check if a key exists in a dictionary
print("basket" in user)  # True
print("size" in user)  # False

# There are not many methods for dictionaries. This one is used to get all the keys:
print(user.keys())  # dict_keys(['basket', 'greet', 'age'])
print("greet" in user.keys())  # True

# To print the keys without the dict_keys, we can use the unpacking operator:
print(*user.keys())  # basket greet age
# This is a very pythonic way of printing the keys

# If I wanna check values, I can use the values() method:
print(user.values())  # dict_values([[1, 2, 3], 'hello', 20])
print(
    user.items()
)  # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
# This last method returns a different synthax. This is because it's actually a tuple.
# We're gonna hold off on tuples for now.

# We can also clear the dictionary:
user.clear()
print(user)  # {}
# Clear doesn't return anything, it alters the dictionary in-place

# We can also copy a dictionary:
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}
user2 = user.copy()
print(user2)  # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
user.clear()  # Clearing user doesn't affect user2.
print(user2)  # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}

user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}
print(user.pop("age"))  # 20 - This returns the value of the key we popped
# But it also removes the key-value pair from the dictionary
print(user)  # {'basket': [1, 2, 3], 'greet': 'hello'}

# popItem() removes the last item from the dictionary
print(user.popitem())  # ('greet', 'hello') - it randomly removes an item from the
# dictionary. This is because dictionaries are unordered. As of Python 3.7, though,
# it will remove the last item added to the dictionary.

# Finally, we can update a dictionary:
user.update({"age": 55})
print(user)  # {'basket': [1, 2, 3], 'age': 55}
# If the key doesn't exist, it will add it to the dictionary
# If the key exists, it will update the value
user.update({"age": 100})
print(user)  # {'basket': [1, 2, 3], 'age': 100}
