
from tkinter import*

root = Tk()
#Create a task function
def myClick():
    My_Label = Label(root,text = "Hey!, You clicked")
    My_Label.pack()

#Create a frame
My_Button = Button(root, text="Click me",command = myClick,fg="blue",bg="black")
#Pack it --Shove it in the window
My_Button.pack()

root.mainloop()