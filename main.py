from tkinter import *

root = Tk()
my_frame = Frame(root)
my_frame.pack()

# - Variables -----------------------------------------------------------------

Title = Label(my_frame, text='Tempo')
Title.grid(row=1, column=1, columnspan=3)

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

# Button(miFrame2, font=(16), text=self.texto, width=5, height=2,padx=10, command=lambda:conexionBD(funcion)).grid(row=self.row, column=self.column)

class Unit():
  def __init__(self, column):

    pass


button_up = Button(my_frame, text='add').grid(row=3, column=1)
button_up = Button(my_frame, text='subtract').grid(row=4, column=1)

hours_entry = Entry(my_frame, textvariable=hours)
hours_entry.grid(row=2, column=1, padx=30, pady=30)
hours_entry.config(bg="black", fg="white", justify='center')

minutes_entry = Entry(my_frame, textvariable=minutes)
minutes_entry.grid(row=2, column=2, padx=30, pady=30)
minutes_entry.config(bg="black", fg="white", justify='center')

seconds_entry = Entry(my_frame, textvariable=seconds)
seconds_entry.grid(row=2, column=3, padx=30, pady=30)
seconds_entry.config(bg="black", fg="white", justify='center')


array = [i for i in range(60)]
print(array)
root.mainloop()
