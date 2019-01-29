import tkinter
from tkinter import *

can = Tk()


def hello(i,s):
    print(i,s)


for i in range(3):
    for s in range(3):
        Button(can, text="Quitter", command=hello(i, s)).grid(row=i, column=s)
        



can.mainloop()


