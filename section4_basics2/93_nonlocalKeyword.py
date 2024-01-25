# nonlocal Keyword

# This keyword allows us to ask the interpreter to use a variable outside of the
# scope of a function, but avoid using the global scope.

x = "local"


def outer():
    x = "local"

    def inner():
        nonlocal x  # if line 8 is commented, the interpreter returns an error
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
