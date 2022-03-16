class Vehicle:
    def __init__(self, name):
        self.owner = name
        self.engine = None
        self.tires = None

    def __str__(self):
        return f"Owner: {self.owner}; Engine: {self.engine}; Tires: {self.tires}"

class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.engine = True
        self.tires = 4
    
    def __str__(self):
        return f"Type: Car; {super().__str__()}"

class Truck(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.engine = True
        self.tires = 4
    
    def __str__(self):
        return f"Type: Truck; {super().__str__()}"

class Cycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2
    
    def __str__(self):
        return f"{super().__str__()}"

class Bicycle(Cycle):
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = False
    
    def __str__(self):
        return f"Type: Bicycle; {super().__str__()}"

class Motorcycle(Cycle):
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = True
    
    def __str__(self):
        return f"Type: Motorcycle; {super().__str__()}"