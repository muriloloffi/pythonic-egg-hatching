# Up until now we've only seen statement looping using the "for" keyword.
# But there's another way to loop through statements: the "while" keyword.
# For loops are dubbed definite loops, that is, they are used when we know in
# advance the size of the data stracture we are working on. For instance, a
# string has a well defined integer number of elements. But sometimes the data
# structure we're working on doesn't have an well difined size. That's when we
# should use the While looping. This looping structures keep looping indefinite-
# ly as long as the condition given is true. Take the examples below.

x = 0
while x <= 50:
    print(x)
    x += 1
else:
    print("Loop finished")

# this else after the while keyword is not mandatory
# and it's not common practice to use it, unless there's an statement that
# was meant to be executed only when at the end of the loop && the loop
# did not enter a break condition.

x = 0
while x <= 50:
    print(x)
    x += 1
    if x >= 40:
        break
else:
    print(
        """Example when the else condition has a statement that should be
        skiped for the break condition"""
    )

# beware that in the case above, the identation could make the else be interpre-
# ted as part of the "if x >= 40:\" condition
