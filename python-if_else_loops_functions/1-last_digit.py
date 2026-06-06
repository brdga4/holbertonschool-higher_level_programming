#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end = " ")
if number < 0:
    number = -number
last = number % 10
print(f"{last} and is", end = " ")
if last > 5:
    print("is greater than 5")
elif last == 0:
    print("0")
elif (last < 6) and not(last == 0):
    print("less than 6 and not 0")
