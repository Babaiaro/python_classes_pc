


# fruits = ["apple", "banana", "cherry"]
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)
#
#
# cars = ["mersedez", "BMW", "Volvo"]
#
# (a, b, c) = cars
# print(a)
# print(b)
# print(c)
from math import frexp

fruits = ["apple", "banana", "cherry","coconut"]
# print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("melon" in fruits)

fruits[0] = "melon"
print(fruits)

fruits.append("watermelon")
print(fruits)

fruits.remove("watermelon")
print(fruits)

fruits.insert(0, "apple")
print(fruits)
fruits.sort()
fruits.reverse()
print(fruits.index("banana"))
print(fruits.count("apple"))

print(fruits)


# sets are here now

fruits = {"apple", "banana", "cherry", "coconut"}

print(fruits)
fruits.remove("banana")
fruits.add("apple2")
fruits.pop() # this is pop the first value in set







print(fruits)