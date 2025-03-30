from tkinter import *
import numpy as np
import time

def grids(cstart,rstart,color,i):
    box1 = Entry(gui, textvariable=value[i],width=3,justify="center", bg=color)
    box2 = Entry(gui, textvariable=value[i+1],width=3,justify="center", bg=color)
    box3 = Entry(gui, textvariable=value[i+2],width=3,justify="center", bg=color)
    box4 = Entry(gui, textvariable=value[i+3],width=3,justify="center", bg=color)
    box5 = Entry(gui, textvariable=value[i+4],width=3,justify="center", bg=color)
    box6 = Entry(gui, textvariable=value[i+5],width=3,justify="center", bg=color)
    box7 = Entry(gui, textvariable=value[i+6],width=3,justify="center", bg=color)
    box8 = Entry(gui, textvariable=value[i+7],width=3,justify="center", bg=color)
    box9 = Entry(gui, textvariable=value[i+8],width=3,justify="center", bg=color)
  
    box1.grid(column=cstart,row=rstart)
    box2.grid(column=cstart+1,row=rstart)
    box3.grid(column=cstart+2,row=rstart)
    box4.grid(column=cstart,row=rstart+1)
    box5.grid(column=cstart+1,row=rstart+1)
    box6.grid(column=cstart+2,row=rstart+1)
    box7.grid(column=cstart,row=rstart+2)
    box8.grid(column=cstart+1,row=rstart+2)
    box9.grid(column=cstart+2,row=rstart+2)

def initial_check():
    for i in range(0,81):
        if value[i].get():
            try:
                a = int(value[i].get())
            except:
                return 0
        
    return 1

#checks if box is empty or not
def press():
    if initial_check():
        pass
    else:
        a = Label(gui, text="Error: Non-integer value in a Box")
        a.grid(columnspan=10)
        a.forget()
        
    if value[0].get():
        value[1].set(2)
    else:
        value[0].set(2)

    
    
    

if __name__ == "__main__":

    gui = Tk()

    # root window title and dimension
    gui.title("SUDOKU")
    gui.geometry('250x250')

    value = np.array(StringVar())
    for i in range(0,81):
        value = np.append(value, StringVar())

    grids(0,0,"lightblue",0)
    grids(3,0,"lavender", 9)
    grids(6,0, "lightblue", 18)
    grids(0,3,"lavender", 27)
    grids(3,3,"lightblue", 36)
    grids(6,3,"lavender", 45)
    grids(0,6,"lightblue", 54)
    grids(3,6,"lavender", 63)
    grids(6,6,"lightblue", 72)
    
    solve = Button(gui, text="Solve", bg="lightgreen", height=2, width=8, command=press)
    solve.grid(row=18, columnspan=8)

    initial_check()
    gui.mainloop()