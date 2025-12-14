
# Name: Babaiar Kenzhebekov
# Date: November 2, 2025
# Problem 6 – Calculate factorial manually and using math.factorial()

import math

print("Problem 6: Factorial Calculation")

# Ask the user for a number.
n = int(input("Enter a positive integer: "))

# Manual factorial using a loop.
manual_fact = 1
for i in range(1, n + 1):
    manual_fact *= i

# Built-in factorial function.
library_fact = math.factorial(n)

print("Manual factorial:", manual_fact)
print("Using math.factorial():", library_fact)
