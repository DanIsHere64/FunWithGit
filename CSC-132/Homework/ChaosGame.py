# Name: Daniel Taylor
# Date: 3/30/22
# Desc: This uses a 2D Point class to graph the Sierpinski triangle
###################################################################

# imports
from tkinter import * 
from random import choice, randint
from math import sqrt

# constants
WIDTH = 600
HEIGHT = 520
POINT_COLORS = ["black", "green", "blue", "orange", "yellow", "purple"]
NUM_POINTS = 50000
MAX_Y = 510
MIN_Y = 10
MAX_X = 590
MIN_X = 10
MID_X = (MIN_X + MAX_X) / 2
MID_Y = (MIN_Y + MAX_Y) / 2

# 2D Point Class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # getters and setters
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def midpt(self, point):
        return Point((self.x+point.x)/2, (self.y+point.y)/2)

# our custom class
class ChaosGame(Canvas):
    
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plot_all_points(self, num_points):
        # Plot the vertices of an equilateral triangle
        vertices = [Point(MIN_X, MAX_Y), Point(MID_X, MIN_Y), Point(MAX_X, MAX_Y)]
        
        for point in vertices:
            self.plot_point(point, rad=3, color="orange")
        
        # Choose two vertices (randomly)
        p1 = choice(vertices)
        p2 = choice(vertices)

        # Find the midpoint between them
        mid = p1.midpt(p2)
        
        # Plot the midpoint
        self.plot_point(mid)

        # Repeat for many times
        for _ in range(num_points):
            # Choose a random vertex
            p1 = choice(vertices)
            # Find the midpoint between previous midpoint and new vertex
            new_mid = p1.midpt(mid)
            # plot new midpoint
            self.plot_point(new_mid)
            # set old midpoint as new midpoint
            mid = new_mid

    # Function for plotting points
    def plot_point(self, point, rad=0, color=NONE):
        if color == NONE:
            color = choice(POINT_COLORS)
        self.create_oval(point.x - rad, point.y - rad, point.x + rad, point.y + rad, fill=color)

# main program

window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("The Chaos Game")

p = ChaosGame(window)
p.plot_all_points(NUM_POINTS)

window.mainloop()