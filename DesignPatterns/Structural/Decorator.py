#Decorator feature 
#changes the result of the function by adding on to it (decorates a function)
#in the below example make_blink is our decorator that alters the result of the hello_world() function

from functools import wraps #wraps keep decorators on the D.L.

def make_blink(function):
    """defines the decorator"""

    #This makes the decorator transparent in terms of its name a nd docstring
    @wraps(function)

    def decorator():
        #Grab the return value of the function being decorated
        ret = function()
        #Add new functionality to the function being decorated
        return '<blink>' + ret + '</blink>'

    return decorator

#Apply the decorator here
@make_blink
def hello_world():
    """Original Function""" #these are doc strings
    return "Hello, World!"

#check the result of decorating
print(hello_world())

#check if function name is still the same name of the funciton being decorated
print(hello_world.__name__)

#check if the docstring is still the same as the function being decorated
print(hello_world.__doc__)

