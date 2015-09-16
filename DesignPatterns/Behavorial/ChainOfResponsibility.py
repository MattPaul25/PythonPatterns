class Handler: #abstract handler
    """abstract handler"""

    def __init__(self, successor):
        #self.successor = #define who is the next handler

    def handle(self, request):
        #handled = #if haandled, stop here

        #otherwise, continue
        #if not handled:

    def _handle(self, request):
        raise NotImplementedError('Must provide implmentation in subclass!')

class ConcreteHandler1(Handler): inherits from the absttract handler