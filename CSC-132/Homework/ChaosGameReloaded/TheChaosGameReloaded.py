#####################################################################
# Name: Daniel Taylor
# Date: 4/20/22
# Desc: Making Fractals Using Object Oriented Programming
#####################################################################
from tkinter import *
from Module import *
from random import choice

class ChaosGame(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def make(self, f):
        # find which fractal to make
        if f == "SierpinskiTriangle":
            shape = SierpinskiTriangle(dimensions)
        elif f == "SierpinskiCarpet":
            shape = SierpinskiCarpet(dimensions)
        elif f == "Pentagon":
            shape = Pentagon(dimensions)
        elif f == "Hexagon":
            shape = Hexagon(dimensions)
        elif f == "Octagon":
            shape = Octagon(dimensions)
        else:
            print("Fractal Not Recgonized!")
            quit()     

        # plot all of the vertices
        for vertex in shape.vertices:
            self.plot_point(vertex, rad=3, color="red")

        # choose two random vertices
        p1 = choice(shape.vertices)
        p2 = choice(shape.vertices)

        # plot a point between them
        interpt = p1.interpt(p2, shape.r)
        self.plot_point(interpt)

        # repeat for number of fractal needs
        for _ in range(0, shape.num_points):
            # choose a random vertex
            p1 = choice(shape.vertices)
            # find new interpoint between last interpoint and new vertex
            new_interpt = p1.interpt(interpt, shape.r)
            # plot new interpoint
            self.plot_point(new_interpt)
            interpt = new_interpt


    def plot_point(self, point, color=NONE, rad=0):
        if color == NONE:
            color = "black"
        self.create_oval(point.x - rad, point.y - rad, point.x + rad, point.y + rad, fill=color)

    

#####################################################################

# defaultsize of the canvas is 600*520
WIDTH = 600
HEIGHT = 520

dimensions = {
    "min_x": 5,
    "max_x": WIDTH - 5,
    "min_y": 5, 
    "max_y": HEIGHT - 5
}

dimensions["mid_x"] = (dimensions["min_x"] + dimensions["max_x"]) / 2
dimensions["mid_y"] = (dimensions["min_y"] + dimensions["max_y"]) / 2

# the implemented fractals
FRACTALS = ["SierpinskiTriangle","SierpinskiCarpet","Pentagon",\
            "Hexagon", "Octagon"]

# create the fractals in individual, but sequential windows
for f in FRACTALS:
    window = Tk()
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.title("The Chaos Game...Reloaded")
    # create the game as a Tkinter canvas inside the window
    s = ChaosGame(window)
    # make the current fractal
    s.make(f)
    # wait for the window to close
    window.mainloop()
