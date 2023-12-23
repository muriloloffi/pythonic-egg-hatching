# Given a list with a limited number of elements, let's say
little_list = [1, 2, 3]
# We can iterate over that list either with
# 1 - a for:
for item in little_list:
  print(item)

# 2 - a while:
i = 0
while i < len(little_list):
  print(little_list[i])
  i += 1

# Let's recaptulate what we saw in the previous page.
# We can use the while loop whenever the size of the data structure we'll itera-
# te is indefinite. For instance, if we have a queue stored in any kind of data
# structure, usually a list, it can have its size updated while we iterate over
# it. In that case, we use a while loop which condition is true whenever the
# list is not empty.

# But truly, the most common use case for a while loop we will see is this:

while True:
  response = input("say something: ")
  if response == "bye":
    break
  else:
    print(response)
    
# While true with a condition break allows us to loop indefinetely until a
# goal is reached.
