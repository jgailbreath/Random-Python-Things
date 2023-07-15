#
# This example uses a class to create a base blueprint for the structure and behavior
# of objects.  Objects are instances of classes that encapsulate data (the attributes)
# and functionality (the methods).  OOP gives programs a modular approach to modeling
# real-world entities and their interactions.
#

# Define a class representing a car
class Car:
    # Constructor method to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start(self):
        self.is_running = True
        print("The car is running.")

    # Method to stop the car
    def stop(self):
        self.is_running = False
        print("The car has stopped.")

    # Method to get the car's details
    def get_details(self):
        return f"{self.year} {self.make} {self.model}"


# Create objects of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Access attributes and call methods on objects
print(car1.get_details())  # Output: 2022 Toyota Camry
car2.start()  # Output: The car is running.
car2.stop()  # Output: The car has stopped.

#
# Expanded example including inheritance and polymorphism.
# Creating a hierarchy of vehicle classes with specialized subclasses.
#

# Base class representing a vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print("The vehicle is running.")

    def stop(self):
        self.is_running = False
        print("The vehicle has stopped.")

    def get_details(self):
        return f"{self.year} {self.make} {self.model}"


# Subclass representing a car
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_doors(self):
        print(f"The {self.make} {self.model} has {self.num_doors} doors. Doors are open.")


# Subclass representing a motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def wheelie(self):
        print("Performing a wheelie!")


# Create objects of different vehicle types
car1 = Car("Toyota", "Camry", 2022, 4)
motorcycle1 = Motorcycle("Honda", "CBR1000RR", 2021)

# Access attributes and call methods on objects
print(car1.get_details())  # Output: 2022 Toyota Camry
car1.start()  # Output: The vehicle is running.
car1.open_doors()  # Output: The Toyota Camry has 4 doors. Doors are open.

print(motorcycle1.get_details())  # Output: 2021 Honda CBR1000RR
motorcycle1.start()  # Output: The vehicle is running.
motorcycle1.wheelie()  # Output: Performing a wheelie!

#
# This example has 2 subclasses, with each one having a unique attribute.
# It also has subclass specific methods.
#
