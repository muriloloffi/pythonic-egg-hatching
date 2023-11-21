# is vs ==

print(True == 1)  # True
print("" == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True

# The "is" operator checks if two objects are the same object. Meanwhile, the
# "==" operator compares the values of two objects. Python's equal comparator is
# strict except for when comparing 1 to True, and 0 to False. It doesn't matter
# if the value for 1 or 0 is of type float, decimal.Decimal, or long. Zero of
# any numeric type, for example, 0, 0L, 0.0, 0j is always False. (Note that
# anything else cast to a bool is True.)
