######################################################################################################################
# Name: Daniel Taylor
# Date: 3/23/22
# Description: Plots points on a graph
######################################################################################################################

from tkinter import *
from math import sqrt
from random import randint

# the 2D point class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def midpt(self, point):
        return Point(self.x+point.x/2, self.y+point.y/2)

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    def __init__(self, master):
        self.master = master
        self.coordSystem = Canvas(self.master, height=800, width=800)
        self.coordSystem.pack()

    def plotPoints(self, num):
        hexVals = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        rgb = hexVals[randint(0,15)] + hexVals[randint(0,15)] + hexVals[randint(0,15)] + hexVals[randint(0,15)] + hexVals[randint(0,15)] + hexVals[randint(0,15)]
        for i in range(num + 1):
            w = Point(randint(0, 799), randint(0, 799))
            oval = self.coordSystem.create_oval(w.x,w.y,w.x+1,w.y+1, fill=f"#{rgb}")
            





##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
