# Escape Sequence

weather = "It's sunny"  # Single quotes inside double quotes are printed as it is

print(weather)

weather = (
    'It\'s "kind of" sunny'
    # Escape sequence is used to print single quotes inside single quotes
)

print(weather)

weather = (
    # fmt: off
    "It\'s \"kind of\" sunny"
    # fmt: on
    # Escape sequence is used to print every quote inside double quotes
)
# P.S. The comments "fmt:" above are used to disable the formatting of the code so that
# it doesn't try to fix the quotes and ruin the example

print(weather)

# Some letters after backslash are used to print special characters,
# e.g. \n for new line

weather = 'It\'s "kind of" sunny \nHope you have a good day'
print(weather)
