#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Complete the code below to print the last digit of the number stored in the variable number
last_digit = abs(number) % 10

print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
