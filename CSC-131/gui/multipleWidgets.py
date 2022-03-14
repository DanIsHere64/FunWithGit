from tkinter import *

window = Tk()

label1 = Label(window, text="lmao", bg="green", fg="white")

label1.pack(fill=X)

label2 = Label(window, text="lol", bg="blue", fg="white")
label2.pack(fill=X)

label3 = Label(window, text="lmfao", bg="red", fg="white")
label3.pack(fill=X)

window.mainloop()


