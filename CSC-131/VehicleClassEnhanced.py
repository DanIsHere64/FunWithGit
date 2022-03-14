#########################################################
# Name: Jean Gourd
# Date: 2017-11-28
# Description: Implements vehicle, truck and car classes.
#########################################################

# the vehicle class
# a vehicle has a year, make, and model
# a vehicle is instantiated with a make and model
class Vehicle():
    def __init__(self, make, model, year=2000):
        self.make = make
        self.model = model
        self.year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if 2000 <= year <= 2018:
            self._year = year
        else:
            self._year = 2000
    
    def __str__(self):
        return (f"{self.year} {self.make} {self.model}")

# the truck class
class Truck(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model, year)
# a truck is a vehicle
# a truck is instantiated with a make and model


# the car class
# a car is a vehicle
# a car is instantiated with a make and model
class Car(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model, year)

# the Dodge Ram class
# a Dodge Ram is a truck
# a Dodge Ram is instantiated with a year
# all Dodge Rams have the same make and model
class DodgeRam(Truck):
    make = "Dodge"
    model = "Ram"
    def __init__(self, year):
        Truck.__init__(self, DodgeRam.make, DodgeRam.model, year)

# the Honda Civic class
# a Honda Civic is a car
# a Honda Civic is instantiated with a year
# all Honda Civics have the same make and model
class HondaCivic(Car):
    make = "Honda"
    model = "Civic"
    def __init__(self, year):
        Car.__init__(self, HondaCivic.make, HondaCivic.model, year)

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print(ram)

civic1 = HondaCivic(2007)
print(civic1)

civic2 = HondaCivic(1999)
print(civic2)