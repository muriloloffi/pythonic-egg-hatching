# Methods vs Functions

# Python has many built-in functions which can be called anywhere, like list(),
# print(), max(), min(), input(). On the other hand, methods are required to
# belong to an object. Invocations of methods are only possible through the
# parent object.

def some_random_stuff() -> None:
  pass

some_string = 'abcdefu'

# Function call
some_random_stuff()

print(
  # Method call below
  some_string.capitalize() 
)

print(
  # Method call below
  'helllooo'.swapcase()
)
