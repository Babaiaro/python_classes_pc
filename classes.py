class Robot:
    def __init__(self, name:str, color:str, weight:int) :
        self.name = name
        self.color = color
        self.weight = weight

    def intruduce_self(self):
        print(r1.name, r1.color, r1.weight)

r1 = Robot("R2D2", "Silver", 120)

# r1 = Robot("""""")

r1.name = "Tom"
r1.color = "red"
r1.weight = 10

r1.intruduce_self()