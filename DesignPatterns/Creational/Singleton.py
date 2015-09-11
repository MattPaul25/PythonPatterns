#singleton is the pattern when you only want one instance of object
#a global variable in object oriented way is a singleton
#tpyically has a cache of information

#using the Borg design pattern******** 8)

class Borg:
    """description of class"""
    _shared_state = {} #attribute dictionary

    def __init__ (self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    """this class now shares all its attributes among its various instances """
    #this makes the singleton objects an object orineted global variablle

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #returns the attribute dictionary for printing
        return str(self._shared_state)


x = Singleton(HTTP = "Hyper Text Transfer Protocal", FTP = "File Transfer Protocal")
print(x)


class SomeClass(Borg): #just to show that now everything that inherits from Borg class has the dictionary key values pairs
  
    def print_vals(self): #notice i can't append to the borg dictionary - if i i intistated a new borg class it creates a new dictionary
        print(str(self._shared_state))


y = SomeClass()
y.print_vals()

z = Singleton(SNMP = "Simple Network Management Protocal") #if i use singleton again i can append to the same version of borg
print(z)