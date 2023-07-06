# Matrix

# A matrix is a bidimensional list, that is, an list of lists.

# fmt: off
# Comment above prevents automatic formatting of the lines below
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
# fmt: on

# This type of matrixes come up a lot in topics like machine
# learning or image processing. For instance, a computer can
# understand an image as a matrix of pixels, where each pixel
# is a list of three numbers, representing the red, green and
# blue values of that pixel.

# The matrix variable could represent an X.

# To access indexes in a matrix, we can use the same syntax
# as with lists, but with two indexes instead of one.

print("matrix[0]:", matrix[0])  # This will print [1, 0, 1]
print("matrix[0][0]:", matrix[0][0])  # This will print 1
