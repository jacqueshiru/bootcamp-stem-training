#GUI with python
from tkinter import*
from tkinter import Tk

# disables the button
root = Tk()
def myClick() :
    myLabel= Label(root,text= "Hey, you clicked")
    myLabel.pack()
myB=Button(root, text="click me!",command=myClick)
myB.pack()
    
root.mainloop()