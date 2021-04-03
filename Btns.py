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
      'Start': Thread(target=self.start).start,
      'Pause': self.pause,
      'Continue': self.conti,
    }
    print(self.var.get())
    self.options[self.var.get()]()

  def start(self):
    self.var.set('Pause')

    while self.var.get() == 'Pause':
      print(self.var.get())
      sleep(1)
      self.min_unit.countdown()

  def pause(self):
    print('estoy aca')
    self.var.set('Continue')

  def conti(self):
    self.var.set('Pause')

