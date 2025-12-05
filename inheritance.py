class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old ")

    def speak(self):
        print("hey there amigo")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old  and i am {self.color}  ")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Barrry", 10)
p.show()
c = Cat("Tom", 8, "green")
c.show()
# c.speak()
d = Dog("It", 9)
# d.show()
d.speak()
f = Fish("Mucho", 5)
f.speak()