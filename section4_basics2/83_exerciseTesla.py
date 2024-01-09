# You just got employed by Tesla, and you need to solve a problem for their self
# driving car:
# age = input("What is your age?: ")

# if int(age) < 18:
# 	print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
# 	print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
# 	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?


def checkDriverAge():
  age = ageInput()

  if age < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif age >= 18:
    print("Powering On. Enjoy the ride!")
    

def ageInput() -> int:
  age = ""

  #Check user input for any wrongly entered characters
  #It's good practice to avoid using try...except blocks in input validation:
  #https://stackoverflow.com/questions/729379/why-not-use-exceptions-as-regular-flow-of-control
  while age.isdigit() is False:
    age = input("What is your age?").strip() or "0"

    if age.isdigit() is False:
      print("Wrongly entered: ")

  return int(age)



checkDriverAge()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age: int = 0) -> None:  
  if age < 18:
    print("Sorry, you're too young to drive this car. Powering off.")
  elif age >= 18:
    print("Powering On. Enjoy the ride!")


checkDriverAge()
