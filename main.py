from tkinter import *
from Unit import Unit

root = Tk()
my_frame = Frame(root)
my_frame.pack()

# - Variables -----------------------------------------------------------------

Title = Label(my_frame, text='Tempo')
Title.grid(row=1, column=1, columnspan=3)

hours = Unit(my_frame, 1, 24)
minutes = Unit(my_frame, 2, 60)
seconds = Unit(my_frame, 3, 60)

root.mainloop()
