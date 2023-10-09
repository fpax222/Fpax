sentence1 = 'Ana says "hello"'
sentence2 = 'Matei says "what\'s up"'
print(sentence1)
print(sentence2)

multiline_str = """x + y (addition)
x - y (substraction)
x * y (multiplication)
x / y (division)"""

print(multiline_str)

print("say" in sentence2)

greeting = "hello"
name = "ana"
age = 20
text = f"{name.capitalize()} says '{greeting.title()}!'"
print(text)

text = f"{name.capitalize()} is {age + 2} years old."
print(text)
