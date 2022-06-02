# GUI with python
from tkinter import*
from tkinter import Tk

# disables the button
root = Tk()
myButton=Button(root, text="click me!", state= DISABLED)
myButton.pack()

root.mainloop()