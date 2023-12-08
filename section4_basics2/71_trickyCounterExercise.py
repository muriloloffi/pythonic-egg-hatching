# Sum the values of the items of the list below:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for value in my_list:
    print(value)
    counter += value

print(
    "The sum of the values above is:",
    counter,
)
