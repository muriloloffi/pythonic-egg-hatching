# Sets
# Sets are unordered collection of unique objects

my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set, ", ", type(my_set), ", sets only have unique values")
# Sets only have unique values, that is, no duplicates

my_set.add(100)
print(my_set, "We tried to add 2, but it was already in the set.")
# Sets are unordered, so we can't index them. So it's all over the place in-memory

# Given the array [1,2,3,4,5,5], how do we convert it to a set?
# How'd you do it? I did it like this:
my_list = [1, 2, 3, 4, 5, 5]
my_set = set(my_list)
print(list(my_set))

# print(my_set[0]) doesn't work, because sets doesn't support indexing
# to Work around this, we can use the in keyword
print(1 in my_set)
print(100 in my_set)
