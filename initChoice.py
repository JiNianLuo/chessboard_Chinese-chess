# -*- coding: cp936 -*-
from Tkinter import *

def sel():
    selection = "You selected the Mode " + str(var.get())
    label.config(text = selection)

root = Tk()

var = IntVar()
R1 = Radiobutton(root, text="Mode 1: Normal Mode", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Mode 2: Free Mode", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

label = Label(root)
label.pack()

root.mainloop()

print var.get()
raw_input()
