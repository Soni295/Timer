from tkinter import StringVar, Entry, Button, Frame

class Unit():
  def __init__(self, frame: Frame, column: int, units: int, next=None):
    self.var = StringVar()
    self.var.set('00')
    self.entry = Entry(frame, textvariable=self.var)
    self.entry.grid(row=2, column=column, padx=10, pady=10)
    self.entry.config(bg='black', fg='white', justify='center')


    self.next = next
    self.btns(frame, column)

    self.units = [ '0' + str(i) if (10 > i)  else str(i) for i in range(units)]

  def btns(self, frame, column):
    self.btn_up = Button(frame, text='add', command=self.add)
    self.btn_up.grid(row=1, column=column, pady=10)
    self.btn_down = Button(frame, text='subtract', command=self.subtract)
    self.btn_down.grid(row=3, pady=10, column=column)

  def add(self):
    prev = int(self.var.get())
    print(prev)
    print(len(self.units))

    if prev == len(self.units) -1 :
      self.var.set(self.units[0])
    else:
      self.var.set(self.units[prev + 1])

  def subtract(self):
    prev = int(self.var.get())
    print(prev)
    print(len(self.units))

    if prev == 0:
      self.var.set(self.units[0])
    else:
      self.var.set(self.units[prev - 1])

  def countdown(self):
    print('hola')

"""
    if next == (self.units[len(self.units)] - 1):
      self.var.set(self.units[0])
    else:
      self.var.set(self.units[int(next)])
"""


