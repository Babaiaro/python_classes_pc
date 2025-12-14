# Name: Babaiar Kenzhebekov
# Date: November 2, 2025
# Problem 1 – Print 10 random integers between 25 and 35

# We import the random module to create random numbers.
import random

print("Problem 1: Ten random integers between 25 and 35")

# Use a for loop to print 10 numbers.
for i in range(10):
    # random.randrange(25, 36) means numbers from 25 up to 35.
    number = random.randrange(25, 36)
    print("Random number", i + 1, ":", number)

