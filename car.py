# class car with methods start(), stop(), drive().
# create multiple instances of car and demonstrate their behaviours

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.brand} {self.model} starts the car")
    
    def stop(self):
        print(f"{self.brand} {self.model} stops the car")
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving")
        

# Create instances of Car
car1 = Car("Cadillac", "CT5-V Blackwing", 2024)
car2 = Car("Jeep", "Wrangler", 2025)

# Demonstrate their behaviors
car1.start()
car1.drive()
car1.stop()

print()  # Add a line break for clarity

car2.start()
car2.drive()
car2.stop()
