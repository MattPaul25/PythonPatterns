#builder is a solution to an anti-pattern called a telescoping constructing 
#telescoping constructor is when a complex object is created with man constructors

#Scenario -- Building Cars
    #Tires, Engine, Doors, etc.

#Builder partitions building a complex object by partitioning, builder class provides all the interfaces for buildling an object (abstract builder)
# Concrete builder inherits form the builder class - 

#Abstract Builder (interfaces)
    #Concrete Builder: implements the abstract bulder or  interfaces -> 


class Director():
    """Director"""
    def __init__(self, builder):
        self._builder = builder
        
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car
        

class Builder(): #abstract class that creates the car object -- generic object that is assigned by the concrete builder
    """abstract builder"""
    def __init__(self):
        self.car = None
        
    def create_new_car(self):
        self.car = Car()




class Car():
    """product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)

class SkyLarkBuilder(Builder): #inherits from builder as to get the car() attribute in builder
    """Concrete Builder --> provides parts and tools to work on the parts """
    def add_model(self):
        self.car.model = "SkyLark"

    def add_tires(self):
        self.car.tires = "Bridgestone"

    def add_engine(self):
        self.car.engine = "V8"


class E350Builder(Builder):
    """another concrete builder"""
    def add_model(self):
        self.car.model = "E350"

    def add_tires(self):
        self.car.tires = "firestone"

    def add_engine(self):
        self.car.engine = "V6"

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

#actionable code - the above code executes first and creates the classes that these commands create objects from
builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)

builder2 = E350Builder()
director2 = Director(builder2)
director2.construct_car()
car2 = director2.get_car()
print(car2)

