from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Humans can live upto 120 years.')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like me?')

if answer == 'yes':
    print(' : ) ')

else:
    print(' : ( ')

root.mainloop()