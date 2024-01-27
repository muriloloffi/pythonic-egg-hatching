# Attributes and Methods

# Objects can have another type of attribute, called "Class Object Attribute".
# These are static, which means their values don't change from one object to the
# other. Class object attribute can be referenced inside the object with and
# without the self keyword, because it independent from the object that is
# calling it.


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        # Here, we access the Class Object Attribute "membership", without using
        # the keyword self. But it can also be refered to with self.membership
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def shout(self):
        # To get access to each objects attribute when calling a method, the
        # self keyword is required to be set as the method's parameter
        print(f"MY NAME IS {self.name}")

    def run(self, greeting):
        print(f"{greeting}, let's run!")


player1 = PlayerCharacter("Golias", 20)

player1.run("Hello")

# Bonus: We can get an entire description of the class and it's methods using
# the help() function on a variable. help() will display details about the class
# that describes the type stored in that variable.

help(player1)
