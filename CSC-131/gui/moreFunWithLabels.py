from tkinter import *
WIDTH = 300
HEIGHT = 300

window = Tk()

label1 = Label(window)
label1.grid(row=0, column=0)

label2 = Label(window)
label2.grid(row=0, column=1)

entry1 = Entry(window)
entry2 = Entry(window)



window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Working with grid")