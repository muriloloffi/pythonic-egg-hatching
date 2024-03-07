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
# you're learning Python as your first programming language, just read along the
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


class Foo:
    def __init__(self) -> None:
        self._bar = 0

    @property
    def bar(self) -> int:
        return self._bar

    @bar.setter
    def bar(self, bar_value: int) -> None:
        self._bar = bar_value


x = Foo()
x.bar = 5
print(x.bar)


# Abstraction

# The second pillar, abstraction, states that an object should hide its internal
# implementation, so that developers that use the object and its methods don't
# need to know the details of this implementation. When we run a list method,
# for instance, we don't need to know how pop() is implemented, as long as we
# know what to expect as a return and treat the data type accordingly,
# everything should go well.


# Inheritance

# In OOP, inheritance is the practice of creating a relationship between classes
# with a common behavior through a parent class, or super class, which holds the
# behavior in it and inherits this behavior to its children, thus keeping the
# logic and implementation in a single place.

# For example: Let's say a videogame has multiple character classes and all of
# then hold a common method, which is sign_in. We can keep yourselves from
# repeating by creating a class parent to the characters, which we'll call User,
# that defines this method.


class User:
    def sign_in(self):
        print("log-in logic")


class Wizard(User):
    def __init__(self, name, power=1):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name}: attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows_number=0):
        self.name = name
        self.arrows_number = arrows_number

    def attack(self):
        self.arrows_number -= 1
        print(f"{self.name}: {self.arrows_number} arrows left")


archer1 = Archer("Legolas", 100)
wizard1 = Wizard("Gandalf", 99)

archer1.sign_in()
wizard1.sign_in()

archer1.attack()

wizard1.attack()

archer1.attack()
archer1.attack()

print(isinstance(archer1, User))

# Polymorphism

# Last but not least, polymorphism is the characteristic defined by the ability
# of an object's methods behaving differently depending on the context it was
# called. For example, consider our character classes above, Archer and Wizard.
# Both of them implement the attack method, but the way these method behave is
# different in each character. Another situation which is related, although not
# required, is when the class they extend from implements the method. In this
# case, the children classes can override a method from the parent class to
# change its behavior. Having these implemented, the objects can be used as
# arguments for another method or function and have its method called, returning
# different behaviors, no matter what object was passed. For example:


def player_attack(character):
    character.attack()


print("Using polymorphic method call:")
player_attack(archer1)
player_attack(wizard1)
