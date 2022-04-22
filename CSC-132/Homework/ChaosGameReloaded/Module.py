###################################################################
# Name: Daniel Taylor
# Date: 4/20/22
# Desc: Module file that holds additional classes and such for 
#       Chaos Game... Reloaded
###################################################################
from tkinter import Canvas
from math import *

# This is a class for storing point data
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, point):
        # distance formula
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def midpt(self, point):
        # midpoint formula
        return Point(self.x+point.x/2, self.y+point.y/2)

    def interpt(self, other, r):
        # Make sure that the distance ratio is expressed from a 
        # smaller component value to a larger one
        # first, the x-component
        rx = r
        if (self.x > other.x):
            rx = 1.0 - r
        # next, the y-component
        ry = r
        if (self.y > other.y):
            ry = 1.0 - r
        # calculate the new point's coordinates
        # the difference i the components (distance between the points)
        # the minimum of the components is then added back in order
        # to obtain the coordinates in between the two points (and
        # not with respect to the origin)
        x = abs(self.x - other.x) * rx + min(self.x, other.x)
        y = abs(self.y - other.y) * ry + min(self.y, other.y)

        return Point(x,y)

class Fractal(Point, Canvas):
    def __init__(self, dimensions, vertices):
        # the canvas dimensions
        self.dimensions = dimensions
        # the default number of ponts to plot is 50,000
        self.num_points = 50000
        # the default distance ratio is halfway
        self.r = 0.5
        self.vertices = vertices

    def frac_x(self, r):
        return int((self.dimensions["max_x"] - self.dimensions["min_x"]) * r) + self.dimensions["min_x"]

    def frac_y(self, r):
        return int((self.dimensions["max_y"] - self.dimensions["min_y"]) * r) + self.dimensions["min_y"]

class SierpinskiTriangle(Fractal):
    def __init__(self, dimensions):
        vertices = [
            Point(dimensions["mid_x"], dimensions["min_y"]),
            Point(dimensions["min_x"], dimensions["max_y"]),
            Point(dimensions["max_x"], dimensions["max_y"])
        ]
        Fractal.__init__(self, dimensions, vertices)

class SierpinskiCarpet(Fractal):
    def __init__(self, dimensions):
        vertices = [
            Point(dimensions["min_x"], dimensions["min_y"]),
            Point(dimensions["mid_x"], dimensions["min_y"]),
            Point(dimensions["max_x"], dimensions["min_y"]),
            Point(dimensions["min_x"], dimensions["mid_y"]),
            Point(dimensions["max_x"], dimensions["mid_y"]),
            Point(dimensions["min_x"], dimensions["max_y"]),
            Point(dimensions["mid_x"], dimensions["max_y"]),
            Point(dimensions["max_x"], dimensions["max_y"])
        ]
        Fractal.__init__(self,dimensions, vertices)
        self.r = 0.33
        self.num_points = 100000

class Pentagon(Fractal, Point):
    def __init__(self, dimensions):
        vertices = []
        Fractal.__init__(self,dimensions,vertices)
        self.vertices = [
            Point(dimensions["mid_x"]+dimensions["mid_x"]*cos(2*pi/5+60),(self.frac_y(0.5375)+dimensions["mid_y"]*sin(2*pi/5+60))),
            Point(dimensions["mid_x"]+dimensions["mid_x"]*cos(4*pi/5+60),(self.frac_y(0.5375)+dimensions["mid_y"]*sin(4*pi/5+60))),
            Point(dimensions["mid_x"]+dimensions["mid_x"]*cos(6*pi/5+60),(self.frac_y(0.5375)+dimensions["mid_y"]*sin(6*pi/5+60))),
            Point(dimensions["mid_x"]+dimensions["mid_x"]*cos(8*pi/5+60),(self.frac_y(0.5375)+dimensions["mid_y"]*sin(8*pi/5+60))),
            Point(dimensions["mid_x"]+dimensions["mid_x"]*cos(10*pi/5+60),(self.frac_y(0.5375)+dimensions["mid_y"]*sin(10*pi/5+60)))
        ]
        self.r = 0.382

class Hexagon(Fractal, Point):
    def __init__(self, dimensions):
        vertices = []
        Fractal.__init__(self,dimensions,vertices)
        self.vertices = [
            Point(dimensions["mid_x"], dimensions["min_y"]),
            Point(dimensions["min_x"], self.frac_y(0.25)),
            Point(dimensions["max_x"], self.frac_y(0.25)),
            Point(dimensions["min_x"], self.frac_y(0.75)),
            Point(dimensions["max_x"], self.frac_y(0.75)),
            Point(dimensions["mid_x"], dimensions["max_y"])
        ]
        self.r = 0.335

class Octagon(Fractal, Point):
    def __init__(self,dimensions):
        vertices = []
        Fractal.__init__(self,dimensions,vertices)
        self.vertices = [
            Point(self.frac_x(0.2925), dimensions["min_y"]),
            Point(self.frac_x(0.7075), dimensions["min_y"]),
            Point(dimensions["min_x"], self.frac_y(0.2925)),
            Point(dimensions["max_x"], self.frac_y(0.2925)),
            Point(dimensions["min_x"], self.frac_y(0.7075)),
            Point(dimensions["max_x"], self.frac_y(0.7075)),
            Point(self.frac_x(0.2925), dimensions["max_y"]),
            Point(self.frac_x(0.7075), dimensions["max_y"])
        ]
        self.num_points = 75000
        self.r = 0.295