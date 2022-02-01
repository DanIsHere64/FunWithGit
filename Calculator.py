from distutils import command
from tkinter import *

class Item(Frame):
    def __init__(self, master, kind, row, column, text, alignment=NSEW, colSpan=1, command = "0", borderWidth = 0, bg = "#856ff8", ipadx = 5, ipady = 5):
        Frame.__init__(self, master)
        self.master = master
        self.kind = kind
        self.row = row
        self.column = column
        self.text = text
        self.alignment = alignment
        self.colSpan = colSpan
        self.command = command
        self.borderWidth = borderWidth
        self.bg = bg
        self.ipadx = ipadx
        self.ipady = ipady
        self.whichKind()

    def whichKind(self):
        if self.kind == "button":
            self.setupButton()
        elif self.kind == "label":
            self.setupLabel()
        elif self.kind == "entry":
            self.setupEntry()
        else:
            print("not setting up")

    def setupLabel(self):
        lbl = Label(self.master, text=f"{self.text}", bg=self.bg)
        lbl.grid(row=self.row, column=self.column, sticky=self.alignment, ipady=self.ipady, ipadx=self.ipadx, columnspan=self.colSpan)

    def setupButton(self):
        if self.command != 0:
            btn = Button(self.master, text=f"{self.text}", command = self.command)
        else:
            btn = Button(self.master, text=f"{self.text}")
        btn.grid(row=self.row, column=self.column, sticky=self.alignment, ipady=self.ipady, ipadx=self.ipadx, columnspan=self.colSpan)

    def setupEntry(self):
        etry = Entry(self.master)
        if self.text != "\n":
            etry.insert(0, f"{self.text}")
        etry.grid(row=self.row, column=self.column, sticky=self.alignment, ipady=self.ipady, ipadx=self.ipadx, columnspan=self.colSpan)
     
outputText = ""
window = Tk()

def Addition():
    outputText = "+"
    Item(window, "label", 0, 0, outputText, colSpan=4, bg="WHITE", borderWidth=2)

output = Item(window, "label", 0, 0, outputText, colSpan=4, bg="WHITE", borderWidth=2)
seven = Item(window, "button", 1, 0, "7")
eight = Item(window, "button", 1, 1, "8")
nine = Item(window, "button", 1, 2, "9")
four = Item(window, "button", 2, 0, "4")
five = Item(window, "button", 2, 1, "5")
six = Item(window, "button", 2, 2, "6")
one = Item(window, "button", 3, 0, "1")
two = Item(window, "button", 3, 1, "2")
three = Item(window, "button", 3, 2, "3")
zero = Item(window, "button", 4, 2, "0")
enter = Item(window, "button", 4, 0, "=", colSpan=2)
plus = Item(window, "button", 1, 3, "+", command=Addition())

window.mainloop()