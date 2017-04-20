# Created By:
# Justin M. Shaner
# John Bassler
# Kieth Lara
# CS470 - Project 4: Halma Phase 1
# Started: April 14, 2017
# Completed: ------
#
# Reminder: We will be using Python 3.6.
#####################################################################
from tkinter import *
    
def onClick(x, y):
    col,row = boardFrame.grid_location(x, y)
    col = col
    row = row - 1

    testButton = boardFrame.grid_slaves(row = row + 1, column = col)

    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
        testButton[0].config(bg = "red")
    else:
        pass
    
def set16():
    unmarkTop = [(2, 11), (3, 11), (4, 11), (4, 12), (3, 12), (4, 13)]
    unmarkBot = [(12, 2), (12, 3), (12, 4), (13, 3), (13, 4), (14, 4)]
    for row in range(5):
        for col in range(5):
            if ((row,col+11) not in unmarkTop):
                testButton = boardFrame.grid_slaves(row = row + 1, column = col + 11)
                testButton[0].config(bg = "red")
    for row in range(5):
        for col in range(5):
            if ((row+12,col) not in unmarkBot):
                testButton = boardFrame.grid_slaves(row = row + 12, column = col)
                testButton[0].config(bg = "green")

def set10():
    unmarkTop = [(2, 6), (3, 6), (3, 7)]
    unmarkBot = [(7, 2), (7, 3), (8, 3)]
    for row in range(4):
        for col in range(4):
            if ((row,col+6) not in unmarkTop):
                testButton = boardFrame.grid_slaves(row = row + 1, column = col + 6)
                testButton[0].config(bg = "red")
    for row in range(4):
        for col in range(4):
            if ((row+7,col) not in unmarkBot):
                testButton = boardFrame.grid_slaves(row = row + 7, column = col)
                testButton[0].config(bg = "green")

def set8():
    unmarkTop = [(1, 5), (2, 5), (2, 6)]
    unmarkBot = [(6, 1), (6, 2), (7, 2)]
    for row in range(3):
        for col in range(3):
            if ((row,col+5) not in unmarkTop):
                testButton = boardFrame.grid_slaves(row = row + 1, column = col + 5)
                testButton[0].config(bg = "red")
    for row in range(3):
        for col in range(3):
            if ((row+6,col) not in unmarkBot):
                testButton = boardFrame.grid_slaves(row = row + 6, column = col)
                testButton[0].config(bg = "green")

def setBoardUp(size):
    allowedBoardSizes = [8, 10, 16]
    if (size not in allowedBoardSizes):
        print("Invalid Board")
    elif (size == 16):
        set16()
    elif (size == 10):
        set10()
    elif (size == 8):
        set8()
    else:
        print("Work to do")

def findMousePos(event):
    curX = boardFrame.winfo_rootx()
    curY = boardFrame.winfo_rooty()
    boardFrame.focus_set()
    onClick(event.x_root - curX, event.y_root - curY)


boardSize = 16
mainWindow = Tk()
Grid.rowconfigure(mainWindow, 0, weight = 1)
Grid.columnconfigure(mainWindow, 0, weight = 1)
boardFrame = Frame(mainWindow)
boardFrame.grid(row = 0, column = 0, stick = N + S + E + W)
titleLabel = Label(boardFrame, text = "Halma Game V0.00001")
titleLabel.grid(row = 0, column = 0, columnspan = boardSize, pady = 0)
buttonList = []
for num in range(boardSize * boardSize):
    buttonList.append(Button(boardFrame))
count = 0
for row in range(boardSize):
    Grid.rowconfigure(boardFrame, row + 1, weight = 1)
    for col in range(boardSize):
        Grid.columnconfigure(boardFrame, col, weight = 1)
        aButton = buttonList[count]
        if (row%2 == 0):
            if (col%2 == 0):
                aButton.config(bg = "snow")
            else:
                aButton.config(bg = "gray60")
        else:
            if (col%2 != 0):
                aButton.config(bg = "snow")
            else:
                aButton.config(bg = "gray60")
        aButton.grid(row = row + 1, column = col, sticky = N + S + E + W)
        aButton.bind("<Button-1>", findMousePos)
        count += 1
setBoardUp(boardSize)
mainWindow.wm_geometry("900x921")
mainWindow.resizable(0,0)

        
   

mainWindow.mainloop()

