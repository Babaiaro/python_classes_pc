def greet(name):
    print(f"Hello, {name}")

greet("Bob")

def multiplying (num1, num2):
    return num1 * num2
print(multiplying(5,8))

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print(fahrenheit_to_celsius(25))
print(fahrenheit_to_celsius(45))
print(fahrenheit_to_celsius(6))


def get_name():
    return "Hello world"

al_name = get_name()
print(al_name)



def parts_for_sale(*parts):
    print("Parts", type(parts))
    print("For Volvo", parts[0])
    print("For Freightliner", parts[1])
    print("For Kenworth", parts[2])

parts_for_sale("Oil separator", "Oil Filter", "Fuel filter")

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
            return max_num
print(my_function(9, 2, 3,6,8,5))

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))