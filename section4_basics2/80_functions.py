# Python gives us a reasonably good set of default functions. Without those
# we'd have to implement things like printing from scratch every time we wanted
# to print something to the screen.
# To be able to avoid repeating yourself, Python also allows us to create our
# own functions using the keyword "def" followed by the function name and colon.
# "def" comes from "define" and it tells the Python interpreter that the
# following statements after the colon will be stored in memory, if correctly
# indented, as a custom function.

# For instance, let's refactor the tree as a custom function:


def print_picture(picture, fill, end="\n"):
    for row in picture:
        for pixel in row:
            if pixel:
                print(fill["fill"], end="")
            else:
                print(fill["empty"], end="")
        print("\n", end="")
    print(end=end)


picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

fill = {"fill": "*", "empty": " "}

print_picture(picture, fill)
print_picture(picture, fill, end="")

# Functions should always be declared before being called
# Also, function calls required the use of () after the function name
# If we print a function name without parentheses, we get the type details
# and memory address

print(print_picture)
