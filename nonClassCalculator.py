from tkinter import *

window = Tk()
def button(master, text, command=0):
    if command != 0:
        return Button(master, text=text, command=command)
    else:
        return Button(master, text=text)

def grid(item, row, column, sticky=NSEW, padx=2, pady=2, cSpan=1, ipadx=2, ipady=2):
    item.grid(row=row,column=column,sticky=sticky,padx=padx,pady=pady,columnspan=cSpan,ipady=ipady,ipadx=ipadx)

zero = button(window, "0")
grid(zero, 4, 2)
one = button(window, "1")
grid(one, 3, 0)
two = button(window, "2")
grid(two, 3, 1)
three = button(window, "3")
grid(three, 3, 2)
four = button(window, "4")
grid(four, 2, 0)
five = button(window, "5")
grid(five, 2, 1)
six = button(window, "6")
grid(six, 2, 2)
seven = button(window, "7")
grid(seven, 1, 0)
eight = button(window, "8")
grid(eight, 1, 1)
nine = button(window, "9")
grid(nine, 1, 2)
equals = button(window, "=")
grid(equals, 4, 0, cSpan=2)
output=Entry(window, justify=RIGHT)
grid(output, 0, 0, cSpan=4)


window.mainloop()