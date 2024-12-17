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
    win = Sudoku_Logic(current_vals)

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

x = np.arange(0,gridwidth,1)
y = np.arange(gridwidth,gridwidth*2,1)

entries = []
coords = []
final_vals = []

for i in range(len(x)):

    final_vals.append([])
    coords.append([])
    entries.append([])

    for j in range(len(y)):

        final_vals.append([])
        entries[i].append([])
        coords[i].append(random())

        entr = ttk.Entry(frame, width=5,font=('Arial 24'),textvariable=coords[i][j])
        entries[i][j].append([entr,x[i],y[j],0])




text = ttk.Label(text="SUDOKU", font=('Arial 24') )
text.grid(column = 3, row = 0)

button = ttk.Button(frame,text = "Check",padding=15, command=Result)
button.grid(column = 4, row = 9)

text = ttk.Label(text="Submit",padding=15 )
text.grid(column = 3, row = 14)


button = ttk.Button(frame,text = "Quit", command=Quit)
button.grid(column = 4, row = 15)

def current_vals():


    """"
    Function that will eventually be part of sudoku logic.

    This is extracting the values entered into the entry boxes.

    Gives raw data.
    
    """
    global entries
    final_vals2 = []
    for i in range(0,gridwidth):
        for j in range(0,gridwidth):
            entries[i][j][0][3] = entries[i][j][0][0].get()
            final_vals2.append(entries[i][j][0][0].get())

    reshaped = np.array(final_vals2).reshape((9,9))
    print(reshaped)
    return final_vals2

button = ttk.Button(frame,text = "Vals", command=current_vals)
button.grid(column = 4, row = 15)


for i in range(len(x)):
    for j in range(len(y)):
        entries[i][j][0][0].grid(row = entries[i][j][0][1], column = entries[i][j][0][2])

root.mainloop()
