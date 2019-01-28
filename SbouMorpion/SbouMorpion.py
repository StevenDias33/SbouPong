import tkinter
from tkinter import *

can = Tk()


def hello():
    print("salut")

B1 = Button(can, text="Quitter", command=hello)



B1.pack()
can.mainloop()


