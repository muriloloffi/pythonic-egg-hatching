# Tuple

# A tuple are like lists, but inlike lists, tuples are immutable.
my_tuple = (1, 2, 3, 4, 5)
# In lists, we could change the value of an index.
try:
    my_tuple[0] = 0
except TypeError:
    print(
        """
          If you read this message, it's because you tried to change the value of an
          index in a tuple and instead of stopping the program, the error was handled
          to print this message. TL:DR; tuples are immutable.
    """
    )
# Yet, you can access the values of a tuple by index.
index = 0
print("Value at index {} is {}".format(index, my_tuple[index]))
# We can also check if a value is in a tuple.
value = 1
print("Is {} in the tuple? {}".format(value, value in my_tuple))

# The benefits of using tuples over lists is that in some contexts, tuples are faster,
# safer and more efficient than lists. However, tuples are not as flexible as lists, so
# if you need to change the values of a collection, you should use lists instead.
# In dictionaries, we can't use lists as keys, but because tuples are immutable, we can
# use them as keys.
my_dict2 = {(1, 2): "Hello"}
print("Value of key (1, 2) in my_dict is {}".format(my_dict2[(1, 2)]))
