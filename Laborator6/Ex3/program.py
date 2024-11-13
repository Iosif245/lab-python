class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def calculate_mileage(self, fuel_used, miles_driven):
        return miles_driven / fuel_used

class Motorcycle(Vehicle):
    def calculate_mileage(self, fuel_used, miles_driven):
        return miles_driven / fuel_used

class Truck(Vehicle):
    def towing_capacity(self, load_weight):
        if load_weight <= 10000:
            return "Can tow this load"
        else:
            return "Exceeds towing capacity"

car = Car(make="Toyota", model="Corolla", year=2020)
motorcycle = Motorcycle(make="Yamaha", model="MT-07", year=2019)
truck = Truck(make="Ford", model="F-150", year=2018)

print("Car Mileage Calculation:")
print("Mileage:", car.calculate_mileage(fuel_used=10, miles_driven=300), "miles per gallon")

print("\nMotorcycle Mileage Calculation:")
print("Mileage:", motorcycle.calculate_mileage(fuel_used=5, miles_driven=200), "miles per gallon")

print("\nTruck Towing Capacity:")
print(truck.towing_capacity(load_weight=8000))
print(truck.towing_capacity(load_weight=12000))