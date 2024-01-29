# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
aelin = Cat("Aelin", 2)
kaz = Cat("Kaz", 4)
yen = Cat("Yennefer", 5)


# 2 Create a function that finds the oldest cat
def getOldestCat(*args) -> Cat:
    return max(args, key=lambda cat: cat.age)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldestCat = getOldestCat(aelin, kaz, yen)
print(f"{oldestCat.name}, the oldest cat, is {oldestCat.age} years old.")
