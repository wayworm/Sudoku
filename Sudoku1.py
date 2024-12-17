# This project is my attempt to demostrate my python ability to myself
# I want to create a window containing a sudoku grid which the user can
# interact with by placing numbers into the grid and I would like 
# The solver to verify if the sudoku has been solved (restrcicted by sudoku rules)

#Front end:
#tkinter is simply but ugly

#backend:
# This project is mostly array manipulation
# and checking that the constraints have not been violated

import tkinter as tk
import numpy as np
from tkinter import ttk
from random import random

def Sudoku_Logic(entry_vals):
    for i in entry_vals:
        print(i)


def Result():
    global text
    text.destroy()
    win = Sudoku_Logic([1])

    if win == True:
        text = ttk.Label(text="You Win!")
        text.grid(column = 3, row = 4)

    else:
        text = ttk.Label(text="Not Quite!")
        text.grid(column = 3, row = 4)


def Quit():
    global root
    root.destroy()

root = tk.Tk()

frame = ttk.Frame(root,padding=100)
frame.grid(column=0,row=0,columnspan=7,rowspan=5)

gridwidth = 9

entries = []
x = np.arange(0,gridwidth,1)
y = np.arange(gridwidth,gridwidth*2,1)

coords = []

for i in range(len(x)):
    coords.append([])
    for j in range(len(y)):
        coords[i].append(random())
        entr = ttk.Entry(frame, width=5,font=('Arial 24'),textvariable=coords[i][j])
        entries.append([entr,x[i],y[j]])




text = ttk.Label(text="SUDOKU", font=('Arial 24') )
text.grid(column = 3, row = 0)


button = ttk.Button(frame,text = "Check",padding=15, command=Result)
button.grid(column = 4, row = 9)



text = ttk.Label(text="Submit",padding=15 )
text.grid(column = 3, row = 14)


button = ttk.Button(frame,text = "Quit", command=Quit)
button.grid(column = 4, row = 15)

def current_vals():
    global coords

    for i in range(0,gridwidth):
        for j in range(0,gridwidth):
            coords[i][j] == entries[i+j].get()
    print(coords)

button = ttk.Button(frame,text = "Vals", command=current_vals)
button.grid(column = 4, row = 15)


for entry,posx,posy in entries:
    entry.grid(row = posx, column = posy)


root.mainloop()
