from decimal import Decimal


def greet(name, greeting="hi"):
    print(f"{greeting.capitalize()}, {name}!")


greet("Anna")
greet("Jane", "hello")


def get_price_with_vat(product, price):
    if product in ("bread", "water"):
        return price * Decimal("1.05")  # early-return pattern
    return price * Decimal("1.19")


bread_price = get_price_with_vat("bread", 5)
water_price = get_price_with_vat("water", 7)

print("Total:", bread_price + water_price)
print(get_price_with_vat("phone", 1500))

