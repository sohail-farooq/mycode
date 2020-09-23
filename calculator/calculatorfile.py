#!/usr/bin/env python3


num1 = float(input("Enter number: "))
oper = input("Enter operation: ")
num2 = float(input("Enter second number: "))


if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "*":
    print(num1 * num2)
else:
    print("Invalid operation")

