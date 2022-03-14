class Vehicle():
    def __init__(self, kind, owner, engine, tires):
        self.kind = kind
        self.owner = owner
        self.engine = engine
        self.tires = tires

class Cars():
    def __init__(self, owner):
        self.owner = owner
        Vehicle.__init__('Car', self.owner, 'True', '4')

class Trucks():
    def __init__(self, owner):
        self.owner = owner
        Vehicle.__init__('Truck', self.owner, 'True', '4')

class Cycles():
    def __init__(self, owner, type, engine):
        self.owner = owner
        self.type = type
        self.engine = engine
        Vehicle.__init__(self.type, self.owner, self.engine, '2')
 
