# Tuple

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
new_tuple = my_tuple[1:2]

print(new_tuple)
print("A tuple with a single value is printed with a comma at the end.")

# Similar to lists, it's possible to assign tuple values to multiple variables.

x, y, z, *other = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print("x: ", x, "\ny: ", y, "\nz: ", z, "\nother: ", other)

my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
