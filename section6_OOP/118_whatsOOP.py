# What is Object Oriented Programming?

# During the late 60s and early 70s, programmers came up with the concept of
# object oriented programming (OOP) as a way to organize the structure of the
# code into a more readable, reusable and maintainable format. At that time, there
# were a lot of changes happening in the way code is written and OOP stood out
# as one of the most prominent and is the most prevalent paradigm nowadays.

# In OOP, data is structured in so called objects, which are meant to represent
# a more intuitive and natural representation of real world objects. In reality,
# objects of OOP are just a convention for data structuring. The data of an
# object is comprised of variables and functions that have a common purpose. A
# working object in the computer's memory is called an instance. That is brought
# up by a blueprint, called a class. In other words, classes are the piece of
# code that declares what every instance of an object should look like, i.e. what
# variables they should contain, what functions they can perform (called methods
# when these belong to an object) and even who has access to what part of the
# object.

# Let's check a simple use case: a file. To abstract files into objects, we may
# write a class with the following variables: "filename", "contents",
# "date_of_creation", "last_updated", "owner". And the functions we get for such
# class can be: "getContents", "saveFileToDisk", "setFilename". We may have
# functions that can only be used by the object itself, i.e. "setLastUpdated".
# One file class is all that is needed to create any number of files in the
# computer memory. A programmer can leverage the code for files written by a
# previous peer in all his work. If a new variable or function (method) is
# required for the file objects to meet new specifications, there's only one
# piece of code that has to be changed, which is the class that defines the file
# objects.
