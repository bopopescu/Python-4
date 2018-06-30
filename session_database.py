from tkinter import *


def onClick():
    name=entryName.get()
    email=entryEmail.get()
    print("you entered {},{}".format(name,email))


root = Tk()

print(type(root))

#Textual info
lbl=Label(root,text="Hello Aaishwarya")
lbl.pack()

#lbl.grid(row=0,column=0)
lblName=Label(root,text="Enter your name")
lblName.pack()

entryName = Entry(root)
entryName.pack()

lblEmail=Label(root,text="Enter your email")
lblEmail.pack()

entryEmail = Entry(root)
entryEmail.pack()

btnSubmit = Button(root,text="Submit",command=onClick)
btnSubmit.pack()


root.mainloop()