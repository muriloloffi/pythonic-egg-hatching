# Python's *args (arguments) and **kwargs (keyword arguments)

# With *args, a wild card parameter, Python allows us to pass multiple
# arguments with an undetermined limit.

# So let's say we have the function


def super_func(*args):
    return sum(args)


# We can give as many numbers we want:

print(super_func(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

# The other wild card, **kwargs, works similarly, but the arguments must be
# named and these are used as an dictionary inside the function.


def super_kwfunc(**kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return total


print(super_kwfunc(num1=0, num2=1, num3=2, num4=3, num5=4, num6=5))

# Keep in mind these will work as long as the wild card * or ** precedes the
# parameters names. So, any custom named parameters will work the same as *args
# and **kwargs if intended, but the community's convention is to name *args and
# **kwargs. Finally, if a function is going to receive all kinds of arguments at
# once, the convention is the following:
# params, *args, default parameters, **kwargs
