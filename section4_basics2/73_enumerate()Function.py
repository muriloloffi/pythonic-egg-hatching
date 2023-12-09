# Enumerate function
# The enumerate function is another useful function used with iterables. When
# enumered receives an iterable, it indexes the iterable with key, value pairs
# in tuples, literally enumerating the values of the iterable starting by zero.

for i, char in enumerate(list(range(100))):
    if char % 7 == 0:
        print(
            f"index {i} has the value {char} which is divisible by 7 with no remainder"
        )
    else:
        print(f"index {i}: {char}")

print(type((0, 1)))

prime_test_number = 673

print(f"\n Is {prime_test_number} a prime number?")
accumulator = 0

for value in range(prime_test_number):
    if 1 < value <= prime_test_number - 1 and prime_test_number % value == 0:
        print(
            f"The tested number {prime_test_number} is divisible by {value} without a remainder, therefore it's not a prime number"
        )

    else:
        accumulator += 1

if accumulator == prime_test_number:
    print("yes")
else:
    print("nope")
