# Creating our own objects


# The following lines of code declare a PlayerCharacter class, which is sort of
# a blueprint to create objects with types namesake to the class. Read these
# lines, noting the way they are written. Then, continue to the explanation
# below the code.


class PlayerCharacter:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def run(self) -> None:
        print("run")


# To create our own objects in Python, we first define the type of the object
# with the "class" keyword. Keep in mind that the convention for classes is that
# they should use cammel casing, i.e. the starting letters for every word is
# capital. To setup the attributes that every object our class creates, the
# __init__ magic method must be used, a.k.a. __init__ dunder method. This method
# is also called a constructor, because it's called whenever we create a new
# object of our declared type. The constructor requires a reference for the
# object to be created (self) and the values that it's going to set internally
# to the object. In our case, the values are "name" and "age".

player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)

# Now, we've got two instances of the PlayerCharacter object, each one created
# with the same class, but holding different values for its attributes in
# different locations in the memory of the computer. We can check this out with
# a print statement.


print(player1, player2, sep="\n")

print("\nDid you notice the memory address at the end of the print above?\n")

# Now, let's check the attributes values of one of our objects.
print(player1.name, player1.age, sep=", ")

# Let's call the run() method.
player1.run()
