"""This is a docstring for module script"""

x = 5
# x + 7
# x = str(x)
print("value = " + str(x))
print(type(x))

# Explicit line joining (\)
command = "/Users/iulia/PycharmProjects/python-training-oct2023/venv/bin/" \
          "python /Users/iulia/PycharmProjects/python-training-oct2023/" \
          "examples/script.py"
print(command)

# Implicit line joining
command = ("/Users/iulia/PycharmProjects/python-training-oct2023/venv/bin/"
           "python /Users/iulia/PycharmProjects/python-training-oct2023/"
           "examples/script.py")
print(command)

if x > 0:
    print("under if")
else:
    print("under else")
