# List methods 2

# Index
# The index method returns the index of the first occurrence of a value
basket = ["a", "b", "c", "d", "e", "d"]
print(basket.index("d"))  # 3
# It also accepts a start and end parameter, which are the start and end
# indexes to search
print(basket.index("d", 0, 4))  # 3
# print(basket.index("d", 0, 3))  # ValueError: 'd' is not in list

# To avoid method 'not found' errors, we can use Python's in keyword
print("d" in basket)  # True
print("x" in basket)  # False

# Another way to check if an item is in a list is by using the count method
print(basket)
print("d count in the basket: ", basket.count("d"))  # 2
