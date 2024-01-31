# Developer Fundamentals V

# The advice for the Developer Fundamentals no. 5 is: Test your assumptions!
# Whenever a new concept is introduced, don't just rely on accepting it works.
# Don't take it as a "black box logic". Test it. Experiment with code to try to
# explore the inner workings of the concept. For example, when learning what
# the keyword self is in the scope of class, try returning self from a method.
# Run that method in a stantiated object and see what it returns.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self


player1 = PlayerCharacter("Murilo", 99)

print(player1.run())
