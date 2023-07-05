# List slicing

# Just like in strings, we can use slicing to access only part of a list.

# Recap: string slicing
string = "0123456789"
string[0:5]  # This will return "01234"

# We can do the same with lists:
cart = ["notebooks", "sunglasses", "toys", "grapes"]
print("sliced cart:", cart[0::2])  # This will return ['notebooks', 'toys']

# As we have seen in the previous lesson, strings are immutable but lists are mutable.
# For instance:
cart[0] = "laptop"  # This will change the first item in the list to "laptop"
print(
    "complete cart:", cart
)  # This will print ['laptop', 'sunglasses', 'toys', 'grapes']

# Every sliced list is a new list. For instance:
new_cart = cart[0:2]
print("new cart from slice:", new_cart)  # This will print ['laptop', 'sunglasses']
# If we change the first item in the original list, the new list will not be affected.
new_cart[0] = "phone"
print(
    "new cart after being edited:", new_cart
)  # This will print ['phone', 'sunglasses']

# But if we assign the original list to a new variable, and then change the first item
# in the original list, the new list will be affected. This is because both variables
# point to the same list in memory.
original_cart = cart
original_cart[0] = "phone"
print(
    "original cart:", original_cart
)  # This will print ['phone', 'sunglasses', 'toys', 'grapes']
print("cart:", cart)  # This will too print ['phone', 'sunglasses', 'toys', 'grapes']

# To create a new list that is a copy of the original list, we can use the [:] syntax.
full_copy_of_cart = cart[:]
print(
    "full copy of cart:", full_copy_of_cart
)  # This will print ['phone', 'sunglasses', 'toys', 'grapes']
full_copy_of_cart[0] = "laptop"
print(
    "edited full copy of cart:", full_copy_of_cart
)  # This will print ['laptop', 'sunglasses', 'toys', 'grapes']
print("cart:", cart)  # This will print ['phone', 'sunglasses', 'toys', 'grapes']

# Later in the course we will see more ways to copy lists. Like shallow copies and
# deep copies.
