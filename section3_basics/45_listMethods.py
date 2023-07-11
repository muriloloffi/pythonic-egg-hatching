# List Methods

basket = [1, 2, 3, 4, 5]
print(len(basket))

# A Method is an action that belongs to an object
# The way we use methods is by using the dot notation

# Adding
new_list = basket.append(100)
# Everything in python is an object
print(new_list)  # None
print(basket)  # [1, 2, 3, 4, 5, 100]
# Methods don't return anything, they just modify the object itself
# if we wanted to get the appended value to new_list, we should have to have it appended
# before assigning to new_list

# Inserting
# Insert modifies the list in place
basket.insert(4, 100)
print(basket)  # [1, 2, 3, 4, 100, 5, 100]
# insert(index, value) - inserts the value at the index

# Extend
# Instead of receiving an item, it receives an iterable
basket2 = [1, 2, 3, 4, 5]
new_list2 = basket2.extend([100, 101])
print(new_list2)  # None
print(basket2)  # [1, 2, 3, 4, 5, 100, 101]

# Removing
# There's a few ways to remove items from a list
# First, we can use the pop method
basket.pop()
print(basket)  # [1, 2, 3, 4, 100, 5]
basket.pop(0)  # Removes the item at the index
print(basket)  # [2, 3, 4, 100, 5]
basket.remove(4)  # Removes the item with the specified value

# However, pop returns the item that was removed
popped_item = basket.pop()  # pop returns the item from the index it was removed
print("popped_item: ", popped_item)  # 5
print(basket)
# Different methods do different things
# pop() - removes the last item and returns it
# pop(index) - removes the item at the index and returns it
# The last way we will see to remove items from a list is by using the clear method
clear_method_return = basket.clear()
print(basket)  # []
print(clear_method_return)  # None

# It's advised that the developer is always aware of what the method returns
