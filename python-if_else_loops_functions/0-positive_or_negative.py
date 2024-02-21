#!/usr/bin/python3
import random

number = random.randint(-100, 100)

# Complete the code below to print whether the number stored in the variable number is positive or negative
print(number)

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
