print("\tSimple Calculator")

num1 = int(input("Enter first number: "))
operation = input("Enter the choice(+, -, *, /): ")
num2 = int(input("Enter second number: "))


if operation == "+":
    res = num1 + num2
elif operation == "-":
    res = num1 - num2
elif operation == "/":
    res = num1 / num2
elif operation == "*":
    res = num1 * num2

print("Result:",res)