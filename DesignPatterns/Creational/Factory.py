#Factory is an object that specializes in creating other objects - useful when your not sure about what objects you will need
#system needs to be able to handle cats and dogs


class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):  #factory method that creates new pet objects from above classes
    """ the factory method """
    pets = dict(dog=Dog("Doge"), cat=Cat("Ferguson")) 

    return pets[pet]


######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

c = get_pet("cat")
d = get_pet("dog")

print(d.speak())
print(c.speak())