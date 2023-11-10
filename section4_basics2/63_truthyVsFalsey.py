# Truthy and falsey values

# Python converts values to boolean according to a convention.
# Those boolean values are usually called truthy and falsey.

# All values are considered "truthy" except for the following, which are "falsey":
# None
# False
# Zero of any numeric type: 0, 0.0, 0j
# A fraction that equates to 0
# Any empty sequence, for example, '', (), []
# Any empty mapping, for example, {}
# Instances of user-defined classes, if the class defines a __bool__() or __len__()
# method, when that method returns the integer zero or bool value False.

# Here is a Python code snippet that demonstrates this:

from fractions import Fraction


falsey_values = [None, False, 0, 0.0, 0j, "", (), [], {}, Fraction(0, 1)]

for value in falsey_values:
    print(f"{repr(value)} is Falsey: {bool(value) is False}")
