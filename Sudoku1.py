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




def Result():
    """ Returns message to user about if they completed the sudoku"""

    global text
    text.destroy()
    win = Sudoku_Logic()

    if win == True:
        text = ttk.Label(text="You Win!")
        text.grid(column = 3, row = 4)

    else:
        text = ttk.Label(text="Not Quite!")
        text.grid(column = 3, row = 4)


def Quit():
    """   Ends the Program   """
    global root
    root.destroy()


#Window Creation
root = tk.Tk()

frame = ttk.Frame(root,padding=100)
frame.grid(column=0,row=0,columnspan=7,rowspan=5)


#initialisation
gridwidth = 9
x = np.arange(0,gridwidth,1)
y = np.arange(gridwidth,gridwidth*2,1)

entries = []
coords = []
final_vals = []

#These seems awkward
for i in range(len(x)):

    final_vals.append([])
    coords.append([])
    entries.append([])  
    # 2D list of lists containing entry box objects 
    # and the position of those boxes in the sudoku grid

    for j in range(len(y)):

        final_vals.append([])
        entries[i].append([])
        coords[i].append(random()) #My way of giving each entry box a unique linked variable thing

        entr = ttk.Entry(frame, width=5,font=('Arial 24'),textvariable=coords[i][j])
        entries[i][j].append([entr,x[i],y[j],0])


def Sudoku_Logic():
    h,v,subs = current_vals()

    print(h[0])
    row_sum = 0
    column_sum = 0
    sub_sum = 0
    #THIS PART DOESN'T WORK
    ################################################
    for row in h:
        for element in row:
            print(type(element))
            if type(element) == int:
                row_sum += element
        if row_sum != 45:
            print("failure, horizonal wrong",row_sum)
            return False
        row_sum = 0

    for column in v:
        for element in column:
            if type(element) == int:
                column_sum += element
        if column_sum != 45:
            print("failure, vert wrong",column_sum)
            return False
        column_sum = 0

    for sub in subs:
        for row in sub:
            for element in sub:
                if type(element) == int:
                    sub_sum += element
    
    if sub_sum != 45:
        print("failure, matrix wrong",sub_sum)
        return False
    sub_sum = 0
    ########################################################
    return True




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

    reshaped_horizonal = np.array(final_vals2).reshape((9,9))
    reshaped_vertical = reshaped_horizonal.transpose()

    starts = [0,3,6,9]
    submatrices = []

    for i in range(0,3):
        for j in range(0,3):
            h_left = starts[i]
            h_right = starts[i+1]

            v_left = starts[j]
            v_right = starts[j+1]

            submatrices.append(np.array([row[h_left:h_right] for row in reshaped_horizonal[v_left:v_right]]))

    return [reshaped_horizonal , reshaped_vertical, submatrices]


#placing labels
text = ttk.Label(text="SUDOKU", font=('Arial 24') )
text.grid(column = 3, row = 0)

text = ttk.Label(text="Submit",padding=15 )
text.grid(column = 3, row = 14)

#placing buttons
button = ttk.Button(frame,text = "Check",padding=15, command=Result)
button.grid(column = 4, row = 9)

button = ttk.Button(frame,text = "Quit", command=Quit)
button.grid(column = 4, row = 15)

button = ttk.Button(frame,text = "Vals", command=current_vals)
button.grid(column = 4, row = 15)

#Placing entry boxes
for i in range(len(x)):
    for j in range(len(y)):
        entries[i][j][0][0].grid(row = entries[i][j][0][1], column = entries[i][j][0][2])

root.mainloop()
