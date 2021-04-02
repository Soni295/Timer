from tkinter import StringVar, Entry, Button, Frame

class Unit():
  def __init__(self, frame: Frame, column: int, units: int):
    self.var = StringVar()
    self.var.set('00')
    self.entry = Entry(frame, textvariable=self.var)
    self.entry.grid(row=2, column=column, padx=10, pady=10)
    self.entry.config(bg='black', fg='white', justify='center')

    self.btn_up = Button(frame, text='add', command=self.add)
    self.btn_up.grid(row=3, column=column, pady=10)
    self.btn_down = Button(frame, text='subtract')
    self.btn_down.grid(row=4, column=column)

    self.units= [ '0' + str(i) if (10 > i)  else str(i) for i in range(units)]
    print(self.units)

  def add(self):
    prev = self.var.get()
    next = self.units.index(prev)
    print(next)



