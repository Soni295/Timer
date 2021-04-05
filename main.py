#!/usr/bin/python

from tkinter import *
from Unit import Unit
from Btns.Start import Btn

if __name__ == '__main__':
  root = Tk()
  my_frame = Frame(root)
  my_frame.pack()

  Title = Label(my_frame, text='Tempo')
  Title.grid(row=1, column=1, columnspan=3)

  hours = Unit(my_frame, 1, 24)
  minutes = Unit(my_frame, 2, 60, hours)
  seconds = Unit(my_frame, 3, 60, minutes)
  btns = Btn(my_frame, seconds, hours)
  root.mainloop()
