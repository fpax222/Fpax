X = 100


def func(a):
    b = 1

    # global X
    # X = 0

    def inner(x):
        y = 11

        # nonlocal a
        # a = 2222

        print(" --- Local scope (inner) --- ")
        print("Local names:", x, y)
        print("Enclosing names:", a, b, inner)
        print("Global names:", X, func, func2, MyClass)
        print("Built-in names:", range, list, True, len)

    inner(22)
    print("\n --- Local scope (func) --- ")
    print("Local names:", a, b, inner)
    print("Global names:", X, func, func2, MyClass)
    print("Built-in names:", range, list, True, len)


def func2():
    pass
    # print(b)


class MyClass:
    pass


func(2)

if X > 0:
    ceva = "altceva"

print(ceva)

print("\n --- Global scope --- ")
print("Global names:", X, func, func2, MyClass)
print("Built-in names:", range, list, True, len)
