# Return keyword

# Python functions, when invoked, always have a returning value, which can be used
# or assigned to a variable. The value you get when invoking the function 
# depends on what is defined in the function declaration by the "return" 
# statement. If a function lacks a return statement, however, the function 
# automatically returns the value None. The return keyword is an exiting
# statement for a function, that is, in the same function code block, everything
# after the return statement is ignored.

def sum(num1: int, num2: int) -> int:
  return num1 + num2

print(sum(10,5))

# If functions are declared inside one another, the behavior can vary greatly
# depending on how the return keywords are used.

def sum():
  def another_func(n1: int, n2: int) -> int:
    return n1 + n2
  return another_func

# In this case, the returned value will have to be assigned to a variable, that
# can later be used as a function invocation

total = sum()
print(total(10, 5))

# As a final observation, the function-in-function can behave like any other
# function, if the developer decides to do so. For example:

def sum(num1: int, num2: int) -> int:
  def another_func(n1: int, n2: int) -> int:
    return n1 + n2
  return another_func(num1, num2)

print(sum(10, 5))

# Meanwhile, our variable still holds the previous function:
print('final print:', total(10,5))
