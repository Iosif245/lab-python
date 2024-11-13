class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} gives birth without egg."

class Bird(Animal):
    def fly(self):
        return f"{self.name} can fly."

class Fish(Animal):
    def swim(self):
        return f"{self.name} swims in water."

mammal = Mammal(name="Elephant", habitat="Savannah")
bird = Bird(name="Eagle", habitat="Mountains")
fish = Fish(name="Shark", habitat="Ocean")

print("Mammal:")
print(mammal.give_birth())

print("\nBird:")
print(bird.fly())

print("\nFish:")
print(fish.swim())