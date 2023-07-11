# Common List Patterns
# We have already seen some common list methods.
# Let's talk about some more list patterns and useful tricks you'll see a lot.
# Some of these methods can be performed with slicing. I.e.:
basket = ["a", "x", "b", "c", "d", "e", "d"]
basket.sort()
basket.reverse()
print(basket[::-1])  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
# What happened: we sorted the list, then reversed it, and then reversed it again with
# slicing.
# If we print basket again, we'll see that it's still sorted and reversed:
print(basket)  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']

# If I want to quickly create a list of items from 0 to 100, I can do:
range_list = list(range(1, 101))
print(range_list)

# If i give one single argument to range(), it will start from 0:
range_list2 = list(range(101))
print(range_list2)

# Range is something we will talk a lot more when we see loops.
# Finally, the last common list pattern we will see a lot is the join() method.
# Join() is a string method, but it's very useful to join lists.
sentence = " "
sentence2 = sentence.join(["Hi", "my", "name", "is", "Joao"])
print(sentence)
print(sentence2)
# Join() joins the elements of the list with the string we pass to it.

# The short way to do this is to not even create the sentence variable:
sentence3 = " ".join(["Hi", "my", "name", "is", "Joao"])
print(sentence3)

# This way we are combining the list elements with a space in between into a string.
