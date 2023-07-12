# Dictionaries

# Another data type in Python is the dictionary, which is also a data structure.
# It's similar to a list, but instead of using indexes to access the data, we use keys.
# On other languages, dictionaries can be found as "hash tables" or "associative
# arrays", in Python they are called dictionaries, or "dict" for short. The "dict"
# keyword is used to create a dictionary.
# Let's see an example:
my_dict = {
    "key1": "value1",
    "key2": "value2",
}  # Here, we're using curly brackets to create a dictionary with two keys: "key1" and
# "key2". The values of these keys are "value1" and "value2" respectively.
# We can access the values of the dictionary by using the keys:
print(my_dict["key1"])  # If key "key1" exists, print "value1". Value1 will be printed.
print(my_dict["key2"])  # ... again, "value2" will be printed.

# print(my_dict["key3"])  This would throw an error if it was uncommented, because
# "key3" doesn't exist in the dictionary. That being said, we must understand that a
# dictionary is unordered, so the order of the keys doesn't matter. This means that the
# key value pairs are not next to each other in memory. In these small examples, it may
# seem that the order is preserved, but that's not the case. In big dictionaries, the
# values might be retrieved in a different order than they were inserted. As long as we
# use the correct key, we'll get the correct value.

# The cool thing about data structures like dictionaries is they function as containers
# for other data types. For example, we can have a dictionary with a list as a value:
my_dict2 = {
    "key1": ["value1", "value2", "value3"],
    "b": "hello",
    "c": 3,
}  # This is a dictionary with 3 keys: "key1", "b" and "c". The value of "key1" is a
# list with 3 elements.

print(my_dict2["key1"])  # This will print the list ['value1', 'value2', 'value3']
print(my_dict2["key1"][1])  # This will print 'value2'

# This is the same with lists, we can have a list with a dictionary as a value:
my_list = [
    1,
    2,
    3,
    {"key1": "value1", "key2": "value2"},
    {"a": [1, 2, 3], "b": "hello", "c": True},
]  # This is a list with 4 elements, the last one being a dictionary
print(my_list[3])  # This will print the dictionary {'key1': 'value1', 'key2': 'value2'}
print(my_list[3]["key1"])  # This will print 'value1'
print(my_list[4]["a"][2])  # This will print 3
