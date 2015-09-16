
#The word proxy is an oagent or substitute authorized to act for another person or a 
#document which authorizes the agent so to act

#Proxy is handy when creating a resource intensive object
#Problem: Postpone object creation unless absolutely necessary


#Scenario -create a producer class when he is available (only a fixed number of producers can exist at a current time)
#Proxy is an artist to see when the producer becomes available
   #in charge of creating resource heavy object..



import time

class Producer:
    """Define the 'resource-intensive' object to instantiate"""
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Define the 'realatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """check if producer is available"""
        print('Artist checking if producer is availble....')

        if self.occupied == 'No':
            #if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            #make the producer meet the guest
            self.producer.meet()
        else:
            #otherwise, dont instantiate a producer
            time.sleep(2)
            print('Producer is busy..')

######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########
           
#instantiate a proxy 
p = Proxy()

#make the proxy: artist produce until producer is availble
p.produce()

p.occupied = 'Yes'

p.produce()