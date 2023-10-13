from datetime import date


class Person:
    """Class describing a person
    Person(name, date_of_birth) --> Person object"""
    MIN_YEAR = 1900  # class attribute
    count = 0

    def __init__(self, pname, dob):
        self.name = pname  # instance attribute
        self.date_of_birth = dob
        self._increment_count()

    @property
    def date_of_birth(self):  # getter
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):  # setter
        if value.year < self.MIN_YEAR:
            raise Exception(f"minimum year is {self.MIN_YEAR}")
        self._date_of_birth = value

    @date_of_birth.deleter
    def date_of_birth(self):  # deleter
        del self._date_of_birth

    @property
    def age(self):
        return self.compute_age(self.date_of_birth)

    # def __setattr__(self, key, value):
    #     if key == 'date_of_birth':
    #         if value.year < self.MIN_YEAR:
    #             raise Exception(f"minimum year is {self.MIN_YEAR}")
    #     super().__setattr__(key, value)

    def greet(self, greeting="hi"):  # instance methods
        print(f"{greeting.capitalize()}! I am {self.name}.")

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def __str__(self):
        return f"Person object (name={self.name})"

    @classmethod
    def _increment_count(cls):
        cls.count += 1

    @staticmethod
    def compute_age(date_obj):
        diff = date.today() - date_obj
        return int(diff.days / 365.25)


if __name__ == "__main__":
    print(Person.__doc__)
    p1 = Person("Ana", date(2000, 4, 5))
    p2 = Person("Matei", date(1985, 12, 25))
    print(p1, str(p1), repr(p1))

    # Attributes can be modified from outside the class
    p2.name = 'Andrei'
    print(p2.name, p2.date_of_birth)

    print(p1.MIN_YEAR is Person.MIN_YEAR)
    print("Person count:", Person.count)

    p1.greet("hello")
    p2.greet()

    # Can also be called as:
    Person.greet(p1, "hello")

    print('p1 is younger than p2:', p1 < p2)

    print(Person.compute_age(date(1800, 4, 8)))

    # Private/protected methods shouldn't be called from outside the class
    # Person._increment_count()
    # print("Person count:", Person.count)

    # Magic methods can be called from outside the class
    print(p1.__str__())
    # But we should rather call use the built-in function or operator that calls
    # them under the hood
    print(str(p1))

    invalid_date = date(1898, 4, 2)
    try:
        p3 = Person("Ion", invalid_date)
    except Exception:
        pass

    try:
        p1.date_of_birth = invalid_date
    except Exception:
        pass
    print(p1.date_of_birth)

    # del p1.date_of_birth
    # print(p1.date_of_birth)

    print(f"{p1.name} is {p1.age} years old.")
