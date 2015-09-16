
class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"
    
class Cat:

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"

class DogFactory:
   def get_pet(self):
      #returns dog object
      return Dog()

   def get_food(self):
      #returns dog food
      return "Dog Food!"


class CatFactory:
   def get_pet(self):
      #returns dog object
      return Cat()

   def get_food(self):
      #returns dog food
      return "Cat Food!"

class PetStore:
    #petstore houses our abstract factory
    def __init__ (self, pet_factory = None):
        """ pet_factory is our abstract factory """
        self._pet_factory = pet_factory



    def show_pet(self):
        """ utility method to display the details of the objects returned by the dog factory """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello '{}'!".format(pet.speak()))
        print("The pets food is '{}'!".format(pet_food))

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

#create a concrete factory
factory = DogFactory()

#Create a pet store housing our abstract factory
shop = PetStore(factory)

#invoke the utility to show the details of our pet
shop.show_pet()

#same thing useing the cat object
c_factory = CatFactory()
c_shop = PetStore(c_factory)
c_shop.show_pet()