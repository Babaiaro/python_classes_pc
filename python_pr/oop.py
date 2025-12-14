class MyClass:
    variable = "blah"

    def function(self):
        print("this the message insite the class.")

myobjectx = MyClass()
print(myobjectx.variable)
print(myobjectx.function())

# class MyClass:
#     color = "red"
#
#     def function(self):
#         print("this the message insite the class.")
#
#     myobjectx = MyClass()
#     myobjecty = MyClass()
#
#     myobjectx.color = "blue"
#
#     print(myobjectx.color)
#     print(myobjecty.color)

class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number
var = NumberHolder(10)
var2 = NumberHolder(20)
print(var.returnNumber())
print(var2.returnNumber())

class MyClass:
    def __init__(self, color):
        self.color = color

    def function(self):
        print("this the message insite the class.")

myobjectx = MyClass("red")
myobjecty = MyClass("blue")

print(myobjectx.color)
print(myobjecty.color)


class Vehicle:
    name = " "
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $% worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Porter"
car1.color = "blue"
car1.kind = "long cabin"
car1.value = 450000

car2 = Vehicle()
car2.name = "Ford"
car2.color = "red"
car2.kind = "van"
car2.value = 50000

print(car1.description())
print(car2.description())