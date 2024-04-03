# Scope

# Global Scope: variables declared outside functions automatically enter the
# global scope of the environment where that file is executed. That means such
# variables share the same environment as the whole program executed by the
# source code that the variable was declared in.

# Function Scope: When a variable is declared in the code block of a function,
# then the variable is not accessible from outside that function.

# Examples:

# Global scope:

some_global_variable = 10

if True:
    another_global_variable = 5
    # even with indentation, because it's not inside a function

print(some_global_variable, another_global_variable)

# Function Scope:


def some_func() -> None:
    total = 100
    print(total)


some_func()

# Throws an error because total isn't accessible outside some_func
# print(total)

# Finally, the variable "total" can be accessed by another function if that
# function was declared inside some_func(). Global variables can be accessed
# inside any function too.


def some_other_func() -> None:
    some_total = 101
    print(some_global_variable)

    def nested_func():
        by_the_prophets_beard = some_total + another_global_variable
        print(by_the_prophets_beard)

    nested_func()


some_other_func()
print(list(globals().keys())[-4:])
