import imp
import tkinter
from tkinter import *
pane = Tk()
b1 = Button(pane, text = "Click me !")
b1.pack(fill=Y, expand = True)
# Button 2
b2 = Button(pane, text = "Click me too")
b2.pack(fill = X, expand = True)
# Execute Tkinter
pane.mainloop()
