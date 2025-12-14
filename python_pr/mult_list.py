# Babaiar Kenzhebekov
# Date: November 6, 2025
# Problem 3: Multiply all numbers in a list [5, 2, 7, -1]

def multiplyList(numbers):
    """Return product of all numbers in the list"""
    result = 1
    for n in numbers:
        result *= n
    return result

# Example test
my_list = [5, 2, 7, -1]
print("List:", my_list)
print("Product of list:", multiplyList(my_list))
