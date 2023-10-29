# Sets 2
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(f"Original sets\nmy_set: {my_set}\nyour_set: {your_set}")

# Sets are useful for finding differences between sets of elements and information
print(my_set.difference(your_set), "difference")
print(
    f"We didn't change the original set because we used the method .difference():\n{my_set}"
)

my_set.discard(5)
print(my_set, "We removed 5 from the set")

my_set.difference_update(your_set)  # Removes all elements of another set from this set
print(my_set)

my_set = {1, 2, 3, 4, 5}  # Resetting the set
print(
    my_set.intersection(your_set),
    "This returned set has the intersection of the two sets",
)

print(
    f"""Are the sets disjoint?\n{my_set.isdisjoint(your_set)}""",
    "\nThe method .isdisjoint() returns a boolean",
    "\nIt'd be True if they had no intersection",
)
# Returns True if two sets have a null intersection

print(my_set.union(your_set), "\nThis is the union of the two sets")
print(
    "We didn't change the original set because we used the method .union():\n",
    my_set,
    "so it is returning a new set, not changing the original in-place",
    "\nAlso, the union of the sets only has unique values, no duplicates too",
    "\nThis is the same as using the pipe operator |",
)
print(
    f"my_set | your_set: \n{my_set | your_set} \n| operator is a shortcut for .union()"
)
print(f"While & is a shortcut for .intersection():\n{my_set & your_set}")

my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(
    f"resetting the sets\nmy_set: {my_set}\nyour_set: {your_set}\n",
    "Is 'my_set' a subset of 'your_set'?\n",
    f"my_set.issubset(your_set): {my_set.issubset(your_set)} \n'my_set' is a subset of 'your_set'.",
)

print(f"Is 'your_set' a superset of 'my_set'?\n{your_set.issuperset(my_set)}")

# Subsets are a slice of a set, while supersets are the whole, or broader spectrum, of a set
