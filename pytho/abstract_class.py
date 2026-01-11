from abc import ABC, abstractmethod

class Vehicle(ABC): 
    

    @abstractmethod
    def go(self):
        pass
        pass


    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


car = Car()

car.go()
car.stop()
