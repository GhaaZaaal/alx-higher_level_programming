#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
if mod == 0:
    print(f"Last digit of {number} is {mod} and is {mod}")
elif mod > 5:
    print(f"Last digit of {number} is {mod} and is greater than 5")
else:
    print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
