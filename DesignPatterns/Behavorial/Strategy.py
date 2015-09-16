#offers family of interchangable behaviors to a client ;
#scenario -- abstract strategy class with a default set of behaviors

#allows adding methods dynamically by importing types module

import types 

class Strategy:
    """the strategy pattern class"""
    def __init__(self, function = None):  
        self.name = "Default Stategy"
        if function != None:
            self.execute = function  
        else:
            self.execute = self.default_execute  

        #if a reference to a function is provided, replace the execute method with the given function

    def default_execute(self): #This gets replaced by another version if another strategy is provided
        """the default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

    #def alsoExecute(self): #this method also gets the same treatment as execute if a function name is provided
    #    print ("yehhawwww {}".format(self.name))


    #replacement method one
def strategy_one():
     print("Strategy 1 is used to execute method 1")

#replacement method two
def strategy_two():
     print("Strategy 2 is used to execute method 2")

#let's create our default strategy




######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.execute()

s1 = Strategy(function = strategy_two)
s1.execute()