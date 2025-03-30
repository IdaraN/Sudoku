from tkinter import *
import numpy as np

def grids(cstart,rstart,color,j):
    # create entry box for each sudoku box
    box1 = Entry(gui, textvariable=value[j][0],width=3,justify="center", bg=color)
    box2 = Entry(gui, textvariable=value[j][1],width=3,justify="center", bg=color)
    box3 = Entry(gui, textvariable=value[j][2],width=3,justify="center", bg=color)
    box4 = Entry(gui, textvariable=value[j][3],width=3,justify="center", bg=color)
    box5 = Entry(gui, textvariable=value[j][4],width=3,justify="center", bg=color)
    box6 = Entry(gui, textvariable=value[j][5],width=3,justify="center", bg=color)
    box7 = Entry(gui, textvariable=value[j][6],width=3,justify="center", bg=color)
    box8 = Entry(gui, textvariable=value[j][7],width=3,justify="center", bg=color)
    box9 = Entry(gui, textvariable=value[j][8],width=3,justify="center", bg=color)
  
    # align boxes in 3 by 3 grid pattern
    box1.grid(column=cstart,row=rstart)
    box2.grid(column=cstart+1,row=rstart)
    box3.grid(column=cstart+2,row=rstart)
    box4.grid(column=cstart,row=rstart+1)
    box5.grid(column=cstart+1,row=rstart+1)
    box6.grid(column=cstart+2,row=rstart+1)
    box7.grid(column=cstart,row=rstart+2)
    box8.grid(column=cstart+1,row=rstart+2)
    box9.grid(column=cstart+2,row=rstart+2)


if __name__ == "__main__":

    gui = Tk()

    # root window title and dimension
    gui.title("SUDOKU")
    gui.geometry('200x200')

    # use 1-D array to store values
    value = np.array([[StringVar(), StringVar(), StringVar(),
                         StringVar(), StringVar(), StringVar(),
                         StringVar(), StringVar(), StringVar()]])

    for i in range(0,8):
        arr = np.array([[StringVar(), StringVar(), StringVar(),
                         StringVar(), StringVar(), StringVar(),
                         StringVar(), StringVar(), StringVar()]])
        value = np.concatenate((value,arr), axis=0)
        

    #call grid creation function
    grids(0,0,"lightblue",0)
    grids(3,0,"lavender", 1)
    grids(6,0, "lightblue", 2)
    grids(0,3,"lavender", 3)
    grids(3,3,"lightblue", 4)
    grids(6,3,"lavender", 5)
    grids(0,6,"lightblue", 6)
    grids(3,6,"lavender", 7)
    grids(6,6,"lightblue", 8)
    

    gui.mainloop()