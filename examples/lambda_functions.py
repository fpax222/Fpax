def compute(operation, a, b):
    # print(operation)
    return operation(a, b)


print(compute(pow, 12, 2))
print(compute(divmod, 10, 3))
print(compute(lambda x, y: x + y, 10, 14))
print(compute(lambda x, y: x * y, 10, 14))
print(compute(lambda x, y: x.index(y), "say something", "some"))
