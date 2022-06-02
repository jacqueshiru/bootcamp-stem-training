#GUI with python
from tkinter import*
from tkinter import Tk

# disables the button
root = Tk()
myButton=Button(root, text="click me!", padx=10, pady=50)
myButton.pack()

root.mainloop()