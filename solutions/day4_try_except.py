# Write a program to read two numbers: x and y from standard input and print
# the result of x / y. If the user inputs invalid data, display an error message
# and exit gracefully.

while True:
    try:
        nr1 = int(input("Type first number: "))
        nr2 = int(input("Type second number: "))
        result = nr1 / nr2
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print('Cannot divide by 0')
    else:
        print(f'Result = {result}. Good job!')
        break
