# Formatted Strings

name = "Johnny"
age = 55

# In python, beginning with version 3+, we can use formatted strings,
# which allows for more readable code.

# In formatted strings (f-strings), we can use curly braces to insert variables.
# Start by adding an f before the string.

print(f"f-strings: Hi, {name}. You are {age} years old.")
# Hi, Johnny. You are 55 years old.

# Before python3, we had to use the format method to insert variables into strings.
# Example below:

print("format(): Hi, {}. You are {} years old.".format(name, age))
# Hi, Johnny. You are 55 years old.

# We can also use indexes to specify the order of the variables.
print("format(): Hi, {1}. You are {0} years old.".format(name, age))
# Hi, 55. You are Johnny years old. (Note the order of the variables)

# Finally, we can also use keywords to specify the order of the variables.
print("format(): Hi, {n}. You are {a} years old.".format(n=name, a=age))


# Bonus: we can also use the format method to specify the number of decimal places.
print("format(): Hi, {n}. You are {a:.2f} years old.".format(n=name, a=age))

# Let's agree that formatted strings with f in front are the way to go,
# for short we usually call them f-strings.
