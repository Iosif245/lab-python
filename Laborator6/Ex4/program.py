class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def manage_team(self):
        return f"{self.name} is managing the team."

class Engineer(Employee):
    def develop_software(self):
        return f"{self.name} is developing software."

class Salesperson(Employee):
    def make_sale(self):
        return f"{self.name} is making a sale."

manager = Manager(name="Alice", salary=80000)
engineer = Engineer(name="Bob", salary=70000)
salesperson = Salesperson(name="Charlie", salary=50000)

print("Manager:")
print(manager.manage_team())

print("\nEngineer:")
print(engineer.develop_software())

print("\nSalesperson:")
print(salesperson.make_sale())