# Global Keyword

# To refer to a global variable from a function scope, without passing arguments
# you can use the 'global' keyword

total = 0

def count():
  global total
  total += 1
  return total

count()
count()
print(count())

# However it's a bad practice to have the code with functions accessing values
# outside their scope, which can cause undesired side effects.

# A better way to do it is using "dependency injection"
total2 = 0
def count2(total):
  total += 1
  return total
print(count2(count2(count2(total2))))
