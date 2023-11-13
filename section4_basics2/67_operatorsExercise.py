# Exercise: Logical and Comparison Operators

is_magician = False
is_expert = False

# Check if magician AND expert: "You are a master magician"
if is_expert and is_magician:
    print("You are a master magician")

# Check if magician but not expert: "At least you're getting there"
elif not is_expert and is_magician:
    print("At least you're getting there")

# If you're not a magician: "You need magic powers"
else:
    print("You need magic power")
