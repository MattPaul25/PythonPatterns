#The iterator pattern -- allows a client to have sequential access to the elements of an aggregate object
#without exposing its underlying structure

#Iterator goes through german counting words based on client input

#provides interface for accessing items of aggregate object

#related to composite pattern

def count_to(count):
    """our iterator implementation"""

    #our list 
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    #our built in iterator creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german) 
    #iterate through our iterable list
    for position, number in iterator:
        #returns a generator containing numbers in german
        yield number


######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########
for num in count_to(2):
    print('{}'.format(num))