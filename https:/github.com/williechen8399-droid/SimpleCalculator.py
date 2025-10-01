#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created 101 by Willie

# Get two numbers from user
number1 = float(input("First number = "))
operation = input("What is the operation (+-*/) ")

number2 = float(input('Second number = '))

# Add numbers and print answer 
if operation == "+":
    print(f"{number1} + {number2} =", number1 + number2)
if operation =='-':
    
    print(f"{number1} - {number2} =", number1 - number2)
if operation =="*":
    print(f"{number1} * {number2} =", number1 * number2)
if operation =="/":
    print(f"{number1} / {number2} =", number1 / number2)
if operation =="/":
    print(f"{number1} ** {number2} =", number1 ** number2)
if operation =="/":
    print(f"{number1} // {number2} =", number1 // number2)
if operation =="/":
    print(f"{number1} % {number2} =", number1 % number2)
if operation =="/":
    print(f"{number1} / {number2} =", number1 / number2)

