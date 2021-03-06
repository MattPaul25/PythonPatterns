import copy


class Prototype: # we use this to clone objects (thats why we import copy)

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car: 
    def __init__(self):
        self.name = "SkyLark"
        self.color = "Red"
        self.options = "Ex"

        def __str__(self):
            return " {} | {} | {}".format(self.name, self.color, self.options)

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

my_car =  Car()
prototype = Prototype()
prototype.register_object("Skylar", my_car)
print(my_car)

my_car2 = prototype.clone("Skylar")
print(my_car2)