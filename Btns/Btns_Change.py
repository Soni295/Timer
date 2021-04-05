from tkinter import StringVar, Entry, Button, Frame
class Button_Count():

  def __init__(self, frame: Frame, column: int, var: StringVar, units: list):
    self.var = var
    self.units = units
    self.btn = Button(frame, command=self.handle_click)
    self.btn.grid(column=column, pady=10)

  def handle_click(self):
    pass

class Button_Add(Button_Count):
  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)
    self.btn.grid(row=1)
    self.btn.config(text='+')

  def handle_click(self):
    prev = int(self.var.get())
    next = '00' if prev == len(self.units) -1 else self.units[prev + 1]
    self.var.set(next)

class Button_Subtract(Button_Count):
  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)
    self.btn.grid(row=3)
    self.btn.config(text='-')

  def handle_click(self):
    prev = int(self.var.get())
    next = '00' if prev == 0 else self.units[prev - 1]
    self.var.set(next)
