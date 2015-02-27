import random

class shape(object):
    
    # Create based on class name:
    @staticmethod
    def factory(type):
        #return eval(type + "()")
        if type == "circle": return circle()
        if type == "square": return square()
        assert 0, "Bad shape creation: " + type

class circle(shape):
    def draw(self): print("circle.draw")
    def erase(self): print("circle.erase")

class square(shape):
    def draw(self): print("square.draw")
    def erase(self): print("square.erase")

# Generate shape name strings:
def shapeNameGen(n):
    types = shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__
