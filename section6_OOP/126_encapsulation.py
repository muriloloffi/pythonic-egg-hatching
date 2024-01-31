# Encapsulation

# Object Oriented Programming (OOP) has a 4-pillar convention: Encapsulation,
# Abstraction, Inheritance and Polymorphism. Encapsulation, states that data and
# behavior of an object should be bundled together. Translating this to code,
# this means writing our classes with all its data as attributes and methods for
# its behavior.

# If coming from a different programming language, keep in mind that Python does
# not use getters and setters. We will see in the next paragraph how Python
# deals with attribute access. This reminder is just for developers who have
# already used another programming language, specially Java and PHP. Now, if
# you're learning Python as your first programming language, just read along
# information in the following lines as a new lesson, just like everything we
# have seen so far.

# Python uses the "Uniform Access Principle"[1]. If a wrap is needed to set a
# variable according to some logic or data treatment, for whatever reason, then
# use @property decorator. This preservers the semantics. That is, foo.x = 0 now
# invokes foo.set_x(0). The main advantage of this approach is that the caller
# gets to do this: foo.x += 1, even though the code might really be doing
# foo.set_x(foo.get_x() + 1)[2].
# [1][https://en.wikipedia.org/wiki/Uniform_access_principle]
# [2][https://stackoverflow.com/questions/4555932/should-i-use-public-attributes-or-public-properties-in-python]

# Abstraction

# The second pillar, abstraction, states that an object should hide its internal
# implementation. So that developers that use the object and its methods don't
# need to know the details of implementation of its methods. When we run a list
# method, for instance, we don't need to know how pop() is implemented, as long
# as we know what to expect as a return and treat the data type accordingly,
# every should go well.
