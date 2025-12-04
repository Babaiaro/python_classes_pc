class Microwave:
    def __init__(self, brand: str, power_rating:str)-> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on:bool = True

    def turn_on(self)-> None:
        if self.turned_on:
            print(f"Microwave {self.brand} is already turned on")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is now turned on")

    def turn_off(self)-> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave {self.brand} is now turned off")
        else:
            print(f"Microwave {self.brand} is already turned off")

    def run(self, second:int)-> None:
        if self.turned_on:
            print(f"Running ({self.brand}) for ({second}) seconds)")
        else:
            print(f"A mystical force whispers: 'Turn on your microwave first'")

    def __add__(self, other):
        return f"Microwave {self.brand} + {other.brand}"

    def __mul__(self, other):
        return f"Microwave {self.brand} * {other.brand}"

    def __str__(self):
        return f"Microwave {self.brand}(Rating: {self.power_rating})"

    def __repr__(self):
        return "REPR"





smeg: Microwave = Microwave("Smeg", "A")
bosch: Microwave = Microwave("bosch", "A")

print(repr(smeg))
print(repr(bosch))