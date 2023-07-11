# List methods 3
# The next one is sort() method. It sorts the list in ascending order.

basket = ["a", "x", "b", "c", "d", "e", "d"]
print(basket.sort())  # None - it alter the object in-place, so
# it's not returning anything
# and returning None
print(basket)  # ['a', 'b', 'c', 'd', 'd', 'e']

# If we got to built-in functions, we have sorted() function.
# It returns a new list, so it doesn't alter the original list.
print(sorted(basket))
print(basket)  # ['a', 'b', 'c', 'd', 'd', 'e']
# Sorted doesn't modify the object in-place, the basket still remains the same.
# Instead, it returns a new list, which is sorted.
# It's as if we did:
new_basket = basket[:]
new_basket.sort()
# By the way, we also have the in-place method copy() for lists, which returns a new
# list.
# It's the same as [:]
# So, we can do:
new_basket2 = basket.copy()
basket.extend(["a", "b", "c", "d", "e", "d"])
print(sorted(basket))

basket.sort()  # Previous sorted() didn't sort the basket in-place, it just returned
# a new list. Now, it's properly sorted in-place.
basket.reverse()
print(basket)
