# One of the tools available for Python programmers to make iterations easiear
# is the range() function.
# With the range function, you can easily create large sequences of integers to
# iterate. Let's take the example below:

print("\nExample 1:", end="\n\n")

for number in range(0, 14):
    print(number)  # This will print the numbers from 0 to 13

# Range is a generator, so it doesn't store the numbers in memory. It generates
# them on demand. This is useful when you want to iterate over a large sequence
# of numbers. For example, if you want to iterate over a million numbers. And it
# also accepts a variable as an argument. For example:

print("\nExample 2:", end="\n\n")

stop_number = 14
for number in range(0, stop_number):
    print(number)  # This will print the numbers from 0 to 13

# The range function accepts a step parameters, meaning you can jump over some
# numbers (example 3). It's very flexible, meaning you can use it backwards
# (example 4).

print("\nExample 3:", end="\n\n")

for number in range(0, 14, 2):
    print(number)  # This will print the numbers from 0 to 13, jumping 2 numbers

print("\nExample 4:", end="\n\n")

for number in range(14, 0, -2):
    print(number)  # This will print the numbers from 14 to 1, jumping 2 numbers
