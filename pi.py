# Name: Babaiar Kenzhebekov
# Date: November 2, 2025
# Problem 4 – Approximation of Pi using a simple formula and compare to math.pi

import math

print("Problem 4: Approximation of Pi")

# Leibniz formula: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
# More terms = more accurate.
terms = 100000
approx_pi = 0

for k in range(terms):
    approx_pi += ((-1) ** k) / (2 * k + 1)

approx_pi *= 4  # Multiply by 4 to get π.

print("Approximated Pi:", approx_pi)
print("math.pi:", math.pi)
print("Difference:", abs(approx_pi - math.pi))

