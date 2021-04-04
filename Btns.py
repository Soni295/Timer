from tkinter import *
from time import sleep
from threading import Thread

class Btn():
  def __init__(self, frame: Frame, min_unit):
    self.var = StringVar()
    self.var.set('Start')
    self.btn_up = Button(frame,
        textvariable=self.var,
        command=self.action)
    self.btn_up.grid(row=2, column=4, pady=10)
    self.min_unit = min_unit

  def action(self):

    self.options = {
      'Start': Thread(target=self.run).start,
      'Pause': self.pause,
      'Continue': Thread(target=self.run).start,
    }


    self.options[self.var.get()]()

  def run(self):
    self.var.set('Pause')
    self.min_unit.block()

    while self.var.get() == 'Pause':
      self.min_unit.countdown()
      sleep(1)

  def pause(self):
    self.var.set('Continue')
    print('estoy aca')
    self.min_unit.unblock()

