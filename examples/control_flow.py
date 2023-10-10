hour = 10
minute = 25

if hour < 10:
    print("Good morning!")
    if minute > 30:
        print("It's getting late!")
    print("under if")
elif hour < 14:
    print("Good day!")
elif hour < 16:
    print("Good afternoon!")
else:
    print("Good evening!")

print("outside if")


status = 200
message = ""

match status:
    case 200:
        message = "OK"
    case 401 | 403 | 404:
        message = "Client Error"
    case 500 | 502:
        message = "Server Error"
    case _:
        message = "Unknown"

print(message)

sum_of_digits = 0
x = 456128
while x:
    sum_of_digits += x % 10
    x //= 10
    ceva = 100

print(f"Sum of digits:", sum_of_digits)

greeting = "Hello"
for char in greeting:
    print(char)

print("range(5):")
for i in range(5):
    print(i)
print()

print("range(3, 7):")
for i in range(3, 7):
    print(i)
print()

print("range(3, 10, 2):")
for i in range(3, 10, 2):
    print(i)
print()

print("range(5) break for i == 3:")
for i in range(5):
    if i == 3:
        break
    print(i)
print()

print("range(5) continue for i == 3:")
for i in range(5):
    if i == 3:
        continue
    print(i)
print()
