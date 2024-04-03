# Type conversion exercise

# Problem: Calculate the user age based on the user input to the question "What year
# were you born?"

# The simplest way is to write a code with the current year minus the year the user was
# born. This example is written as comments from line 9 to 14:

# birth_year = input("What year were you born?\n")
# "\n" escaped character breaks line before user input

# current_year = 2023
# age = current_year - int(birth_year)  # Here's a catch: all data from input is string
# print(age)

# Although the code above can give us a satisfactory answer, it has some flaws
# For instance, it will throw an avoidable error if the user inputs letters. Also, it
# won't take into consideration the system's year if the years have passed since the
# code was originally written.

# We can make things better, see it below.

from datetime import date  # This is a module that comes with Python

# The date module allows us to get the current year
# We will see modules in more detail later in the course

birth_year = ""  # this empty string is used to start a loop with the input question

current_year = date.today().year

# The loop keeps printing the question if the user inputs invalid years
while birth_year.isdigit() is False:
    birth_year = input("What year were you born?\n")
    if birth_year.isdigit() and int(birth_year) > current_year or int(birth_year) <= 0:
        birth_year = ""

birth_year = int(birth_year)

age = current_year - birth_year

print("You were born in " + str(birth_year))
print(f"The system clock tells me that the current year is {current_year}.")
print("If this is correct, you are " + str(age - 1) + " or " + str(age) + " years old.")
