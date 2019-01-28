import tkinter
from tkinter import *

can = Tk()


def hello():
    print("salut")


for i in range(3):
    for s in range(3):
        Button(can, text="Quitter", command=hello).grid(row=i, column=s)
    print(i)



can.mainloop()


