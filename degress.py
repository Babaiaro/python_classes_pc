# Name: Babaiar Kenzhebekov
# Date: November 2, 2025
# Problem 5 – Convert radians to degrees

import math

print("Problem 5: Convert radians to degrees")

# Ask the user for a value in radians.
radians_value = float(input("Enter a value in radians: "))

# Manual conversion formula: degrees = radians * (180 / π)
manual_degrees = radians_value * (180 / math.pi)

# Built-in function from the math module.
library_degrees = math.degrees(radians_value)

print("Manual conversion:", manual_degrees)
print("Using math.degrees():", library_degrees)

