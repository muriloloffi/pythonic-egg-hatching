# Conditional Logic
# Conditional logic allows our programs to make decisions and carry out actions based on those decisions

# imagine a car that automatically detects if you can drive it
# if you are 16 or older, you can drive

is_old_enough = True
is_licensed = True

if is_old_enough and is_licensed:
    print("You can drive!")
elif not is_licensed:
    print("You don't have a license")
else:
    print("You're too young'!")
