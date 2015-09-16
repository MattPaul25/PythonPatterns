#adapter converts interface of a class to another one the client is expecting

#example translator - server is expecting english, client speaks korean, adapter convers korean to english and vice versa


class Korean:
    """korean speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """english speaker"""
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "hello!"

class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object
        
        #Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        #for example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""
        return getattr(self._object, attr)

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

#List to store speaker objects
objects = []

#Create a korean object
korean = Korean()

#Create a british object
british = British()

objects.append(Adapter(korean, speak = korean.speak_korean)) #the speak argument is a key value pair that is added to the adapter dictionary
objects.append(Adapter(british, speak = british.speak_english))

for obj in objects:
    print ('{} says "{}" \n'.format(obj.name, obj.speak()))