# Exercise: check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# for each item of the list, check how many time it appears, if it's greater than 1, print it

duplicate_list = []
for item in some_list:
    if some_list.count(item) > 1:
        duplicate_list.append(item) if item not in duplicate_list else None

print(duplicate_list)
