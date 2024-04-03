# Scope Rules

a = 1


def confusion():
    """
    The python interpreter creates the variable 'a' with value 5 in the
    confusion scope, ignoring the global scope
    """
    a = 5
    return a


# Scope rules for the python interpreter:
# 1 - Start with local, check if the variable exists locally (inside function)
print(a)
print(confusion())


# 2 - Is there a parent scope?
def parent():
    a = 10

    def confusion():
        return a

    return confusion()


print("parent1:", parent())
print(a)


# 3 - Global: gets the variable from the global scope
def parent2():
    def confusion():
        return a

    return confusion()


print("parent2:", parent2())


# 4 - Built-in python functions.
def parent3():
    def confusion():
        return sum

    return confusion()


print("parent3:", parent3())
