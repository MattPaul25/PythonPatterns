#a recursive tree data structure would be a good example of this 
    #element of a tree has its child item 
    #menut and submenu iotems for composite 

class Component(object):
    """abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def composite_function(self):
        pass

class Child(Component): #Inherits from the abstract class, component
    """concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #this is where we store the name of your child item
        self.name = args[0]

    def component_function(self):
        #print the name of your child item here
        print("{}".format(self.name))

class Composite(Component): #inherits from the abstract class, component
     """concrete class and maintins the tree recursive structure"""

     def __init__(self, *args, **kwargs):
         Component.__init__(self, *args, **kwargs)
         #this is where we store the name of the composite object
         self.name = args[0]

         self.childeren = []

     def appen_child(self, child):
         """method to add a new child item"""
         self.childeren.append(child)

     def remove_child(self, child):
         """method to remove a child"""
         self.childeren.remove(child)

     def component_function(self):
         #print the name of the composite object
         print('{}'.format(self.name))


         #iterate through the child objects and invoke their component funciton printing their names
         for i in self.childeren:
             i.component_function()

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

#Build a composite submenu 1
sub1 = Composite('submenu1')

#Create a new child sub_submenu 11
sub11 = Child('sub_submenu 11')

#create a new child sub_submenu 12
sub12 = Child('sub_submenu 12')

#Add the sub_submenu 11 to submenu 1
sub1.appen_child(sub11)
sub1.appen_child(sub12)

#build a top level composite menu
top = Composite('top_menu')


#build a submenu2 that is not a composite
sub2 = Child('submenu2')

#add the composite submenu1 to the top-level composite menu
top.appen_child(sub1)

#add the plain submenu 2 to the top level composite menu
top.appen_child(sub2)

#lets test if our composite pattern works!
top.component_function()