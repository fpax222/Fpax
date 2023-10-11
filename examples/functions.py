from decimal import Decimal


def greet(name, greeting="hi"):
    print(f"{greeting.capitalize()}, {name}!")


greet("Anna")
greet("Jane", "hello")
greet(greeting="bună dimineața", name="Miruna")

# name_and_greeting = ["Jane", "hello"]
# greet(*name_and_greeting)

# print("----")
# print(greet("Mike"))
# print("----")


def get_price_with_vat(product, price):
    if product in ("bread", "water"):
        return price * Decimal("1.05")  # early-return pattern
    return price * Decimal("1.19")


bread_price = get_price_with_vat("bread", 5)
water_price = get_price_with_vat("water", 7)

print("Total:", bread_price + water_price)
print(get_price_with_vat("phone", 1500))


def varargs(*values, sep=" ", **kwargs):
    print(values, type(values), len(values), sep=sep)
    print(kwargs, type(kwargs), end="\n\n")


varargs()
varargs(1)
varargs(1, 2, 3, sep=" | ")
varargs(1, 2, 3, 4, 5, 6, 7)
varargs(name="Ana", balance=50.324534, lalala="ceva")

chars = ['a', 'b', 'c', 'd']
varargs(chars)
varargs(*chars)
varargs(*range(3))


person = {
    'times': 130,
    'name': 'George',
    'hobbies': ['fishing'],
    'friends': ['Alina', 'Andrei', 'Mihai'],
}
varargs(**person)
varargs(times=130, name="George")


# Type hints & recursive function
def factorial(n: int) -> int:
    # if not isinstance(n, int):
    #     return
    if n <= 0:
        return 1
    return n * factorial(n - 1)


print(factorial(3))
print(factorial(4))
print(factorial(4.5))
