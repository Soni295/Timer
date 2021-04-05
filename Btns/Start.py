from tkinter import *
from time import sleep
from threading import Thread

class Btn():
  def __init__(self, frame: Frame, min_unit, max_unit):
    self.var = StringVar()
    self.var.set('Start')
    self.btn_up = Button(frame,
        textvariable=self.var,
        command=self.action)
    self.btn_up.grid(row=2, column=4, pady=10)
    self.min_unit = min_unit
    self.max_unit = max_unit

  def action(self):
    self.options = {
      'Start': Thread(target=self.run).start,
      'Pause': self.pause
    }

    self.options[self.var.get()]()

  def run(self):
    self.var.set('Pause')
    self.min_unit.block(True)

    while self.var.get() == 'Pause' and self.max_unit.state == True:
      self.min_unit.countdown()
      sleep(1)


  def pause(self):
    self.var.set('Start')
    self.min_unit.block(False)
    self.max_unit.state = True
