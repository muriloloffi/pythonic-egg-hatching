# Dictionary Keys

# Up until now we have only seen strings as dictionary keys. Can we use other data
# types? Let's see!

# The following dictionary works:
dictionary = {
    123: [1, 2, 3],
    True: "hello",
    "bye": False,
}
print(dictionary[123])  # [1,2,3]
print(dictionary[True])  # hello

# But this one doesn't:
# dictionary = {
#     [1, 2, 3]: 123,
# }
# That's because dictionary keys always must be immutable. Lists are not.
# Numbers, strings, tuples (we will see later), etc. are immutable, but lists are not.
# Most of the time, the key will be descriptive, so we will use strings.
# What if we use two keys with the same name? Let's see!
dictionary2 = {
    "123": [1, 2, 3],
    "123": "hello",  # The linter may already warn us here. To disable: # noqa: F601
}  # The second key will overwrite the first one
print(dictionary2["123"])  # hello
# A key in a dictionary has to be unique.
# Any key that is repeated will be overwritten.
