# Doc Strings

# Doc Strings are strings declared within a function or method that details
# its purpose. Amongst the goals of doc strings are: to provide details for IDEs
# and text editors hover tooltips on functions or methods; provide details for
# the help(function) built-in function; provide the content for the __doc__
# magic method.


def test(a):
    """
    Info: a purposeless function that takes a single argument and prints it,
    with the goal to show how Doc Strings work.
    """
    print(a)


print(help(test))
print(test.__doc__)
