# The Constructor (__init__)

# The __init__ magic method (or dunder, from Double UNDERline) is called
# everytime a new object is created. Additional control is possible to be
# built-in to the constructor. For instance, it can have conditional
# verification and default values for its parameters. See the following example:


class PlayerCharacter:
    def __init__(self, name: str = "Anonymous", age: int = 0) -> None:
        if age >= 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"MY NAME IS {self.name}")


player1 = PlayerCharacter(name="Tom", age=18)

print(player1.name)
