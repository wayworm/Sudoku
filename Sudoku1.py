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


def current_vals():
    """"
    This is extracting the values entered into the entry boxes.
    Returns a numpy array of 3 elements.
    1st element is an array of the rows of the sudoku.
    2nd element is an array of the columns of the sudoku
    3rd element is an array of the 3x3 boxes in our sudoku 
    ( these boxes are an array of 3 rows of len 3)
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


def Sudoku_Logic():
    """
    Checks if the entries satisfies the rules of sudoku,
    outputs whether we have a valid sudoku.

    Rules:
    - All integers 1 - 9 should appear in each row once
    - All integers 1 - 9 should appear in each column once
    - All integers 1 - 9 should appear in each submatrix once
    """

    h,v,subs = current_vals()
    vals = ["1","2","3","4","5","6","7","8","9"]

    for row in h:
        hused = [None,'']
        for helement in row:
            if True in [helement == i for i in vals] :
                pass
            else:
                print("invalid input")
                return 0
            if True not in [helement == i for i in hused]:
                hused.append(helement)
            else:
                print("failure, duplicates in horizontal")
                print([str(helement) == i for i in vals])
                return 1
    print("horizonal rules not violated.")

   
    for column in v:
        vused = [None]
        for velement in column:
            if True in [velement == i for i in vals] :
                pass
            else:
                print("invalid input")
                return 0
            if True not in [velement == i for i in vused]:
                vused.append(velement)
            else:
                print([str(velement) == i for i in vals])
                print("failure, duplicates in vertical")
                return 2
    print("column rules not violated.")


    #3x3 logic
    for sub in subs:
        sub_used = [None,'']
        for row in sub:
            for subh_element in row:
                if True in [subh_element == i for i in vals] :
                    pass
                else:
                    print("invalid input")
                    return 0

                if True not in [subh_element == i for i in sub_used]:
                    sub_used.append(subh_element)
                else:
                    print("failure, duplicates in 3x3")
                    print([str(subh_element) == i for i in vals])
                    return 3

        print("3x3 rules not violated.")

    return True


def Result():
    """ Returns message to user about if they completed the sudoku
    as well as hints as to what they've done wrong"""

    global text
    text.destroy()
    win = Sudoku_Logic()

    if win == True:
        text = ttk.Label(text="You Win!")
        text.grid(column = 3, row = 4)
    elif win == 0:
        text = ttk.Label(text="You've used invalid characters, only use 1 - 9.")
        text.grid(column = 3, row = 4)
    elif win == 1:
        text = ttk.Label(text="There's a mistake in one of your rows.")
        text.grid(column = 3, row = 4)
    elif win == 2:
        text = ttk.Label(text="There's a mistake in one of your columns.")
        text.grid(column = 3, row = 4)
    elif win == 3:
        text = ttk.Label(text="There's a mistake in one of your boxes.")
        text.grid(column = 3, row = 4)
    else:
        text = ttk.Label(text="ERROR!")
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

        entr = ttk.Entry(frame, width=5,font=('Arial 20'),textvariable=coords[i][j])
        entries[i][j].append([entr,x[i],y[j],0])




#placing labels
text = ttk.Label(text="SUDOKU", font=('Arial 24') )
text.grid(column = 3, row = 0)



#placing buttons
button1 = ttk.Button(frame,text = "Check",padding=10, command=Result)
button1.grid(column = 12, row = 12,sticky="s", columnspan=3 )

button2 = ttk.Button(frame,text = "Quit", command=Quit)
button2.grid(column = 13, row = 13)

# Button for debugging/developing the curernt_vals function
# button = ttk.Button(frame,text = "Vals", command=current_vals)
# button.grid(column = 13, row = 14)



# THIS TIMER DOESN'T WORK
# import time
# def timer():
#     global elapsed_time
#     now = time.time()
#     elapsed_time =  str((time.time() - now))
#     text = "Time Elapsed: " + str((time.time() - now))
#     timer_var.set(text)
#     root.after(2000, timer)

# timer_var= tk.StringVar()

# Timer = ttk.Label(text= timer_var,padding=15 )
# Timer.grid(column = 3, row = 14)
##########################

submit = ttk.Label(text="Submit",padding=15 )
submit.grid(column = 3, row = 15)


#Placing entry boxes
for i in range(len(x)):
    for j in range(len(y)):
        entries[i][j][0][0].grid(row = entries[i][j][0][1], column = entries[i][j][0][2])

#root.after(1000, timer)
root.mainloop()
