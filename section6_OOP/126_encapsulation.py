# Encapsulation

# Object Oriented Programming (OOP) has a 4-pillar convention: Encapsulation,
# Abstraction, Inheritance and Polymorphism. Encapsulation, states that data and
# behavior of an object should be bundled together. Translating this to code,
# this means writing our classes with all its data as attributes and methods for
# its behavior.

# Ff coming from a different programming language, keep in mind that Python does
# not use getters and setters. This paragraph is just for developers who have
# already used another programming language, specially Java and PHP. Python uses
# the "Uniform Access Principle"[1]. If a wrap is needed to set a variable, for
# whatever reason, then use @property decorator. This preservers the semantics.
# That is, foo.x = 0 now invokes foo.set_x(0). The main advantage of this
# approach is that the caller gets to do this: foo.x += 1, even though the code
# might really be doing foo.set_x(foo.get_x() + 1)[2].
# [1][https://en.wikipedia.org/wiki/Uniform_access_principle]
# [2][https://stackoverflow.com/questions/4555932/should-i-use-public-attributes-or-public-properties-in-python]

