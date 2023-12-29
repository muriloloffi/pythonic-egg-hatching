# Parameters and Arguments
# Functions in Python can be defined with one or a set of parameters to be 
# assigned as arguments in the function call. These parameters may have default 
# values, so the arguments become optional. In this case, if the invoked 
# function, that is, the called function doesn't get any arguments, the values 
# defined as default during the function definition are used.

# Parameters:

def say_hello(name, emoji):
  print(f'Hello, {name}! {emoji}')

# Arguments:
say_hello('Olirum', '😊')
say_hello('Dan', '😊')
say_hello('Emily', '😊')

# These parameters are positional. Inverting the order of the arguments inverts
# the assigned values as well. There is, however, another way which is using
# keyword arguments.

say_hello(emoji='😊', name='Bob')

# Using keyword arguments doesn't require arguments to be assigned respecting
# the position of the function definition, but it's highly advised that
# developers keep the order to avoid confusion in the future.

# Finally, there's the examples of the default values, which make it possible
# for the function to work even when only some of the arguments or none of them
# is given.

def say_greetings(name='Darth Vader', emoji='😈'):
  print(f'Greetings, {name}! {emoji}')
  
say_greetings()
