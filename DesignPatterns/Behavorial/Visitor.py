#visitor allows adding new features to existing class heirarchy without changing it

#scenario: house class, HVAC specialist is a vistor, 
#Electrician is visitor 2 -- new actions to be performed on an existing class heirarchy.




class House(object): #the class being visited
    """this is the object that gets visited"""
    def accept(self, visitor):
        """interface to accept a visitor"""
        #Triggers the visitng operation
        visitor.visit(self)
        

    def work_on_hvac(self, hvac_specialist):
        print(self.__str__() + " worked on by " + hvac_specialist.__class__.__name__) #note that we now have a reference to hvac specailist object in the house object

    def work_on_electricity(self, electrician):
        print(self.__str__() + " worked on by " + electrician.__class__.__name__)#Not that we now have a reference to the electrician object in the house object

    def __str__(self):
        """simply return the class name when the house object is printed"""
        return self.__class__.__name__ + '\n' + self.__class__.__doc__

class Visitor(object):
    """abstract visitor"""
    def __str__(self):
        """simply return the class name when the visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    """concrete visitor: hvac"""
    def visit(self, house):
        house.work_on_hvac(self) #visitor has a reference to the house object


class Electrician(Visitor):
    """concrete visitor: electrician"""
    def visit(self, house):
        house.work_on_electricity(self) #visitor has a reference to the house object

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

#create an hvac specialist
hv = HvacSpecialist()
elec = Electrician()

home = House()

home.accept(hv)
home.accept(elec)

print(home)