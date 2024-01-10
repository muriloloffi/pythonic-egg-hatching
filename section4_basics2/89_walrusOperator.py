# Walrus Operator

# As we build more complex logical expressions, one might find to be repeating 
# ourselves too often. For example, a calculation used in a condition might be
# useful later on in the same code block. With that in mind, the walrus operator
# (:=) was created. This operator lets us assign a valvue to a variable at the
# same time it is evaluated by a bigger logical expression. Let's take a look:

a = 'helloooooooooooo'

if (n := len(a)) > 10:
  print(f"too long, {n = }; should be 10 or less")

while (n := len(a)) > 10:
  a = a[:-1]
  print(a, n-1)
  
print('success')

