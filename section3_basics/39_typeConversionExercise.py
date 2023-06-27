# Type conversion exercise

from datetime import date  # This is a module that comes with Python

# This module allows us to get the current date
# We will see modules in more detail later in the course

birth_year = int(input("What year were you born?\n"))

current_year = date.today().year

age = current_year - birth_year

print("You were born in " + str(birth_year))
print(f"The system clock tells me that the current year is {current_year}.")
print("If this is correct, you are " + str(age - 1) + " or " + str(age) + " years old.")
