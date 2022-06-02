
from tkinter import*

root = Tk()

#Create text field space
e1 = Entry(root, width=50, bg="black", fg="white")
e1.pack()
e1.insert(0, "Enter first No.")
#second input
e2 = Entry (root, width=50, bg="white", fg="red")
e2.pack()
e2.insert(0,"Enter second No.")


#Create a task function
def myClick():
    f_no = float( e1.get())
    s_no = float(e2.get())
    sub = f_no - s_no
    add = f_no + s_no
    Div = f_no / s_no
    mult = f_no * s_no




    Ans = "Addition : " + str(add) + "sub : " +str(sub) +"Div : " +"mult : " + str(mult)
    My_Label = Label(root,text = Ans)
    My_Label.pack()

#Create a frame
My_Button = Button(root, text="calculate",command = myClick,fg="blue",bg="black")
#Pack it --Shove it in the window
My_Button.pack()

root.mainloop()