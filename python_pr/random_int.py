# Name: Babaiar Kenzhebekov
# Date: November 2, 2025
# Problem 2 – Print one random odd integer between 0 and 100

import random

print("Problem 2: One random odd integer between 0 and 100")

# The third number (2) means “step by 2” so we only get odd numbers.
odd_number = random.randrange(1, 100, 2)

print("Random odd integer:", odd_number)
