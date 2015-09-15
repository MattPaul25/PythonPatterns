#bridge untangles complex class hierarchy

#two parallel or othogonal abstractions (one is implemntation specific, one is implemtnation dependent)
    #related to abstract factory

#in the below example there are two implementations of drawing a cirlce - then the circle object can handle both implementations
#add note

class DrawingAPIOne(object):
    """Implemntation-specific abstraction: concrete class one""" #a pretend difference of different circle drawing apis
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """implemtation-sepcific abstraction: concreate class two""" #a pretend difference of different circle drawing apis
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class Circle(object):
    """implementation-independent abstraction: for example, there could be a rectangle class !"""
    def __init__(self, x, y,radius, drawing_api):
        """initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implemntation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """implementation-independent"""
        self._radius *= percent


#Build the first circle object using API one
circle1 = Circle(1,2,3, DrawingAPIOne())

#Draw a circle
circle1.draw()

#build a second circle object using API2
circle2 = Circle(2,3,4, DrawingAPITwo())

circle2.draw()