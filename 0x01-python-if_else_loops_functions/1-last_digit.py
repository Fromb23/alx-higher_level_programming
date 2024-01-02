#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
original_sign = -1 if number < 0 else 1 
print("Last digit of", number, "is", original_sign * last_digit, end=" ")

if original_sign * last_digit > 5:
    print("and is greater than 5")
elif original_sign * last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
