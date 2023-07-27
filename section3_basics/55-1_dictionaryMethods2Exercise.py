# 1 Create a user profile for your new game. This user profile will be stored in a
# dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user_profile = {
    "age": 25,
    "username": "nacho",
    "weapons": ["sword", "gun"],
    "is_active": True,
    "clan": "Pythonistas",
}

# 2 iterate and print all the keys in the above user.

# Answer:
print(*user_profile.keys(), "\nor: ")  # also prints "or:" in new line
# or:
for keys in user_profile:
    print(keys)

# 3 Add a new weapon to your user

user_profile["weapons"].append("club")
print("Current weapons:", user_profile["weapons"][-1])

# 4 Add a new key to include 'is_banned'. Set it to false

user_profile.update({"is_banned": False})
print(user_profile["is_banned"])

# 5 Ban the user by setting the previous key to True

user_profile.update({"is_banned": True})
print("Is banned:", user_profile["is_banned"])

# 6 create a new user2 by copying the previous user and update the age value and
# username value.

user2_profile = user_profile.copy()
user2_profile.update({"age": 20, "username": "John"})
print(user_profile, user2_profile, sep="\n\n")
