from tkinter import *

from numpy import right_shift


class ChallengeGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setup_GUI(self):
        l1 = Label(self.master, text="A Label")
        l1.grid(row=0,column=0, sticky=W)

        l2 = Label(self.master, text="Another Label")
        l2.grid(row=1, column=0, sticky=W)

        l3 = Label(self.master, text="A third label, centered")
        l3.grid(row=2, column=0, columnspan=2)

        entry1 = Entry(self.master)
        entry1.grid(row=0,column=1)

        entry2 = Entry(self.master, justify=RIGHT)
        entry2.insert(0, 'user input')
        entry2.grid(row=1,column=1,sticky=E)

        c1 = Checkbutton(self.master, text="some checkbutton option")
        c1.grid(row=3,column=2)

        b1 = Button(self.master, text="A button")
        b1.grid(row=3,column=2)

        b2 = Button(self.master, text="Another button")
        b2.grid(row=3, column=3)


window = Tk()
ch = ChallengeGUI(window)
ChallengeGUI.setup_GUI(window)

window.mainloop()