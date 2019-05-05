class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2.0 * (self.width + self.height)

    def contains(self, p):
        if (p.x < self.corner.x) or (p.y < self.corner.y) or (p.x >= (self.corner.x + self.width)) or (p.y >= (self.corner.y + self.height)):
            print("False")
        else:
            print("True")
class Circle: 
    """A class to create circles""" 
    def __init__(self, posn, r): 
        self.center = posn 
        self.radius = r
