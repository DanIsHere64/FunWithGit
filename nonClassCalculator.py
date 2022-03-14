from tkinter import *


def button(master, text, command=0):
    if command != 0:
        return Button(master, text=text, command=command)
    else:
        return Button(master, text=text)

def grid(item, row, column, sticky=NSEW, padx=2, pady=2, cSpan=1, ipadx=2, ipady=2):
    item.grid(row=row,column=column,sticky=sticky,padx=padx,pady=pady,columnspan=cSpan,ipady=ipady,ipadx=ipadx)


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equals():
    global expression
    try:
        total = str(eval(expression))
        print(total)
        equation.set(total)
        expression=""
    except:
        equation.set(" error ")
        expression = ""


window = Tk()
expression = ""
equation = StringVar()
output=Entry(window, justify=RIGHT, textvariable=equation)
grid(output, 0, 0, cSpan=5)

zero = button(window, "0", command=lambda: press(0))
grid(zero, 4, 2)
one = button(window, "1", command=lambda: press(1))
grid(one, 3, 0)
two = button(window, "2", command=lambda: press(2))
grid(two, 3, 1)
three = button(window, "3", command=lambda: press(3))
grid(three, 3, 2)
four = button(window, "4", command=lambda: press(4))
grid(four, 2, 0)
five = button(window, "5", command=lambda: press(5))
grid(five, 2, 1)
six = button(window, "6", command=lambda: press(6))
grid(six, 2, 2)
seven = button(window, "7", command=lambda: press(7))
grid(seven, 1, 0)
eight = button(window, "8", command=lambda: press(8))
grid(eight, 1, 1)
nine = button(window, "9", command=lambda: press(9))
grid(nine, 1, 2)
equals = button(window, "=", command=equals)
grid(equals, 4, 0, cSpan=2)
plus = button(window, "+", command=lambda: press("+"))
grid(plus, 2, 3)
minus = button(window, "-", command=lambda: press("-"))
grid(minus, 3, 3)
multiply = button(window, "*", command= lambda: press("*"))
grid(multiply, 2, 4)
divide = button(window, "/", command=lambda: press("/"))
grid(divide, 3, 4)
openParenthesis = button(window, "(", command=lambda: press("("))
grid(openParenthesis, 1, 3)
closeParenthesis = button(window, ")", command=lambda: press(")"))
grid(closeParenthesis, 1, 4)
caret = button(window, "^", command=lambda: press("**"))
grid(caret, 4, 3)
window.mainloop()