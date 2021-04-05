from tkinter import StringVar, Entry, Frame
from Btns.Btns_Change import Button_Add, Button_Subtract

class Unit():
  def __init__(self, frame: Frame, column: int, units: int, next=None):
    self.var = StringVar()
    self.var.set('00')
    self.entry = Entry(frame, textvariable=self.var)
    self.entry.grid(row=2, column=column, padx=10, pady=10)
    self.entry.config(bg='black', fg='white', justify='center')

    self.next = next
    self.state = True

    self.units = ['0' + str(i) if (10 > i) else str(i) for i in range(units)]
    self.btn_up = Button_Add(frame, column, self.var, self.units)
    self.btn_down = Button_Subtract(frame, column, self.var, self.units)

  def countdown(self):
    prev = int(self.var.get())

    if prev == 0:
      if self.next == None:
        self.state = False


      elif self.next.countdown() == 1:
        next = self.units[len(self.units) - 1]
        self.var.set(next)
    else:
      next = self.units[prev - 1]
      self.var.set(next)
      print(next)
      return 1

  def block(self, block):
    state = 'disabled' if block else 'normal'
    self.btn_up.btn['state'] = state
    self.btn_down.btn['state'] = state
    if self.next != None:  self.next.block(block)
