from tkinter import *

root = Tk()

def printName():
    print("Hello my name is Shrinidhi!")

# button_1 = Button(root, text="Print my name", command=printName)
# button_1.pack()

# another way of doing the same
def printMyName(event):
    print("Hello SAV!")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printMyName)
button_1.pack()

root.mainloop()