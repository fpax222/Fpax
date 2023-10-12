from datetime import date


class Person:
    """Class describing a person
    Person(name, date_of_birth) --> Person object"""
    MIN_YEAR = 1900  # class attribute
    count = 0

    def __init__(self, pname, dob):
        self.name = pname  # instance attribute
        if dob.year < self.MIN_YEAR:
            raise Exception(f"minimum year is {self.MIN_YEAR}")
        self.date_of_birth = dob
        Person.count += 1

    def greet(self, greeting="hi"):  # instance methods
        print(f"{greeting.capitalize()}! I am {self.name}.")


if __name__ == "__main__":
    print(Person.__doc__)
    p1 = Person("Ana", date(2000, 4, 5))
    p2 = Person("Matei", date(1985, 12, 25))
    print(p1.name, p1.date_of_birth)
    print(p2.name, p2.date_of_birth)

    print(p1.MIN_YEAR is Person.MIN_YEAR)
    print(Person.count, p1.count, p2.count)

    p1.greet("hello")
    p2.greet()

    # Can also be called as:
    Person.greet(p1, "hello")
