#Observer establishes a 1:many relationship between a subject and multiple observers

#subject is modified and observers are notified when there is a change in the subject

#observers are registered

#solution: abstract class called subject: Attach, Detach, Notify

#related to singleton

class Subject(object): #Represents what is being 'observed' Inherits from object because its a new style object with properties (not needed in python 3)
    
    def __init__(self):
        self._observers = [] #this is where references to all observers are stored
                             #Note that this is a one to many relationship: there wil be one subject to eb observered by multiple observers

    def attach(self, observer):
        """attaches the observer to the observers lists"""
        if observer not in self._observers: #if observer does not exist within the observer list then append it
            self._observers.append(observer)
        else:
            print("object is already observing subject")

    def detach(self, observer):
        """detaches the observer from the observer list"""
        try: 
            self._observers.remove(observer)
        except ValueError:
            print (ValueError.message)
            pass

    def notify(self, modifier = None):
        for observer in self._observers:  #for all the observers in the list
            if modifier != observer: #Dont notify the observer who is actually updating the temperature
                observer.update(self)  #alter the observers
       


class Core(Subject): #inherits from subject class
    """represents the nuclear core (and its temperature)"""

    def __init__(self, name=""):
       Subject.__init__(self)
       self._name = name
       self._temp = 0 #initializes temperature to zero

    @property #getter that gets the core temperature
    def temp(self):
        return self._temp

    #@temp.setter
    def set_temp(self, temp, changer=None):
        self._temp = temp
        self.notify(changer)


class TempViewer: #this is an observer class

    def __init__(self, name):
        self._name = name

    def update(self, subject): #alert method that is invoked when the notify() method in a concrete subject is invoked
        print("{}: {} has Temperature {}".format(self._name, subject._name, subject._temp))

    def change_temp(self, subject): #the observer can change the temp
        subject.set_temp(50, self)

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########
#Lets create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#Lets create our observers
v1 = TempViewer("viewer 1")
v2 = TempViewer("viewer 2")

#Lets attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

#Lets change the temperature of first core
c1.set_temp(60) #setting the temp of the core
c1.set_temp(70)

v1.change_temp(c1) #using the observer to set the temp of the core

