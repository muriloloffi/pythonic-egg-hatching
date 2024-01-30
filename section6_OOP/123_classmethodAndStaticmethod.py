# Class methods and static methods

# Besides the class object attribute, python classes can have these two kinds of
# static methods. The class and static methods, declared using the @classmethod
# and @static decorator, are types of methods that don't need an object instance
# to be invoked. However, class methods are able to receive the "cls" parameter,

# The "cls" parameter allows the class methods to access the class constructor.
# This allows the class method to perform data manipulation for a specific case
# before creating an object of the class.

# Example


class Date(object):
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split("-"))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string) -> bool:
        day, month, year = map(int, date_as_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

    def show(self) -> str:
        return f"{self.day}-{self.month}-{self.year}"


is_date = Date.is_date_valid("11-09-2012")
if is_date:
    date2 = Date.from_string("11-09-2012")

print(date2.show())
