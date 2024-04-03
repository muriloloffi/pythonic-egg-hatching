# Clean Code

# Writing clean code translates to writing concise code with well named
# functions, variables, classes and methods, that reduces the cognitive load
# on the programmer when reading that code. For example:


def is_even_or_odd(number):
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False


print(is_even_or_odd(50))

# The function above can be refactored to a simpler more readable one:


def is_even(number: int) -> bool:
    return number % 2 == 0


print(is_even(50))
