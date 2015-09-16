#Chain of command pattern works by delegating tasks to different handlers of the task (acts a bit like a case statement)



class Handler: #abstract handler
    """abstract handler"""

    def __init__(self, successor):
        self._successor = successor #define who is the next handler


    def handle(self, request):
        handled = self._handle(request) #if haandled, stop here

        #otherwise, continue
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implmentation in subclass!')

class ConcreteHandler1(Handler):  #inherits from the absttract handler
    """concrete handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: #provide implementation for handling
            print("Request {} handled in handler 1".format(request))
            return True #indicates that the request has been handled

class ConcreteHandler2(Handler):  #inherits from the absttract handler
    """concrete handler 1"""
    def _handle(self, request):
        if 10 < request <= 20: #provide implementation for handling
            print("Request {} handled in handler 2".format(request))
            return True #indicates that the request has been handled

class DefaultHandler(Handler):
    """default handler"""
    def _handle(self, request):
        """if there is no handler available"""
        #No condition checking due to being a default handler
        print("End of chain, no handler for {}".format(request))
        return True #indicates that the request has been handled

class Client: #use handlers
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(DefaultHandler(None))) #Create handlers and use them in a sequence youu want
    def delegate(self, requests): #send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


######### ~~~~~~~~~~~~~~~ RUNNING THE PATTERN ~~~~~~~~~~~~~~~ #########

#Create a client
c = Client()

#create the sequence
requests = [2, 100, 5, 20, 30]

c.delegate(requests)