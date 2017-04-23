from tkinter import *
import time

class HalmaBoard():

    def __init__(self):
        self.boardSize = 0
        self.currentTurn = True
        self.betweenMove = False
        self.mainWindow = Tk()
        self.boardFrame = Frame(self.mainWindow)
        self.titleLabel = Label(self.boardFrame, text = "Hamla Game V0.000002")
        self.buttonList = []
        self.turnLabel = Label(self.boardFrame, text = "Green Turn: Starting Move")
        self.currentGridX = 0
        self.currentGridY = 0
        self.moveFromRow = 0
        self.moveFromCol = 0
        self.whichColor = ""
        self.gameOver = False

    # Board setup ========================================================================================
    def set16(self):
        unmarkTop = [(2, 11), (3, 11), (4, 11), (4, 12), (3, 12), (4, 13)]
        unmarkBot = [(12, 2), (12, 3), (12, 4), (13, 3), (13, 4), (14, 4)]
        for row in range(5):
            for col in range(5):
                if ((row,col+11) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 11)
                    testButton[0].config(bg = "red")
        for row in range(5):
            for col in range(5):
                if ((row+12,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 12, column = col)
                    testButton[0].config(bg = "green")

    def set10(self):
        unmarkTop = [(2, 6), (3, 6), (3, 7), (1, 6), (2, 7), (3, 8)]
        unmarkBot = [(7, 2), (7, 3), (8, 3), (7, 1), (8, 2), (9, 3)]
        for row in range(4):
            for col in range(4):
                if ((row,col+6) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 6)
                    testButton[0].config(bg = "red")
        for row in range(4):
            for col in range(4):
                if ((row+7,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 7, column = col)
                    testButton[0].config(bg = "green")

    def set8(self):
        unmarkTop = [(1, 5), (2, 5), (2, 6), (3, 5), (3, 6), (3, 7)]
        unmarkBot = [(6, 1), (6, 2), (7, 2), (6, 3), (7, 3), (8, 3)]
        for row in range(4):
            for col in range(4):
                if ((row,col+5) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 4)
                    testButton[0].config(bg = "red")
        for row in range(4):
            for col in range(4):
                if ((row+6,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 5, column = col)
                    testButton[0].config(bg = "green")
                    
    def setBoardUp(self, size):
        allowedBoardSizes = [8, 10, 16]
        if (size not in allowedBoardSizes):
            print("Invalid Board")
            self.turnLabel.config(text = "Invalid Board: Reset Game With board size [8, 10, 16]!")
            self.gameOver = True
        elif (size == 16):
            self.set16()
        elif (size == 10):
            self.set10()
        elif (size == 8):
            self.set8()

    def boardRefresh(self):
        if (self.betweenMove == False):
            for row in range(self.boardSize):
                for col in range (self.boardSize):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col)
                    if (testButton[0].cget("bg") == "maroon"):
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = "maroon"
                    if (testButton[0].cget("bg") == "lightgreen"):
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = "lightgreen"
                    if (testButton[0].cget("bg") == "yellow" or testButton[0].cget("bg") == "lightgreen" or testButton[0].cget("bg") == "maroon"):
                        if (row%2 == 0):
                            if (col%2 == 0):
                                testButton[0].config(bg = "snow")
                            else:
                                testButton[0].config(bg = "gray60")
                        else:
                            if (col%2 != 0):
                                testButton[0].config(bg = "snow")
                            else:
                                testButton[0].config(bg = "gray60")
                    else:
                        pass
        else:
            for row in range(self.boardSize):
                for col in range (self.boardSize):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col)
                    if (testButton[0].cget("bg") == "lightgreen"):
                        testButton[0].config(bg = "green")
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = "lightgreen"
                    if (testButton[0].cget("bg") == "maroon"):
                        testButton[0].config(bg = "red")
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = "maroon"
                    if (testButton[0].cget("bg") == "yellow" or testButton[0].cget("bg") == "lightgreen" or testButton[0].cget("bg") == "maroon"):
                        if (row%2 == 0):
                            if (col%2 == 0):
                                testButton[0].config(bg = "snow")
                            else:
                                testButton[0].config(bg = "gray60")
                        else:
                            if (col%2 != 0):
                                testButton[0].config(bg = "snow")
                            else:
                                testButton[0].config(bg = "gray60")
                    else:
                        pass
    

    def blinkAfter(self): # Broken still
        blinkPos = self.boardFrame.grid_slaves(row = self.moveFromRow, column = self.moveFromCol)
        currentColor = blinkPos[0].cget("bg")
        for blinks in range(3):
            for interval in range(10000):
                if (blinks%2 == 0):
                    blinkPos[0].config(bg = currentColor)
                    #print("T")
                else:
                    blinkPos[0].config(bg = self.whichColor)
                    #print("F")

        


        
    # Click detection on grid ============================================================================
    def onClick(self, x, y):
        #print("Current Turn: " + str(self.currentTurn)) # TESTING
        #print("In Move: " + str(self.betweenMove)) # TESTING
        col,row = self.boardFrame.grid_location(x, y)
        col = col
        row = row
        self.setCurrentGridCoordinates(row - 1, col)
        self.validateMoveSequence(row, col)
    
    def findMousePos(self, event):
        if (self.gameOver == False):
            curX = self.boardFrame.winfo_rootx()
            curY = self.boardFrame.winfo_rooty()
            clickX = event.x_root
            clickY = event.y_root
            curPosClickX = clickX - curX
            curPosClickY = clickY - curY
            self.boardFrame.focus_set()
            self.onClick(curPosClickX, curPosClickY)
        else:
            pass

    def createBoard(self, size):
        self.boardSize = size
        Grid.rowconfigure(self.mainWindow, 0, weight = 1)
        Grid.columnconfigure(self.mainWindow, 0, weight = 1)
        self.boardFrame.grid(row = 0, column = 0, stick = N + S + E + W)
        self.titleLabel.grid(row = 0, column = 0, columnspan = self.boardSize, pady = 0)
        self.turnLabel.grid(row = self.boardSize + 1, column = 0, columnspan = self.boardSize, pady = 0)
        for num in range(self.boardSize * self.boardSize):
            self.buttonList.append(Button(self.boardFrame))
        count = 0
        for row in range(self.boardSize):
            Grid.rowconfigure(self.boardFrame, row + 1, weight = 1)
            for col in range(self.boardSize):
                Grid.columnconfigure(self.boardFrame, col, weight = 1)
                aButton = self.buttonList[count]
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
                aButton.bind("<Button-1>", self.findMousePos)
                count += 1
        self.setBoardUp(self.boardSize)
        self.mainWindow.wm_geometry("1000x1042") #942 -> 42 comes from the height of the titleLabel+turnLabel.
        self.mainWindow.resizable(0,0)

    def startMainLoop(self):
        self.mainWindow.mainloop()
    
    # Move related functions =============================================================================
    def validateMoveSequence(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (self.betweenMove == False):
            if (self.currentTurn == True):
                if (buttonPos[0].cget("bg") != "green"):
                    self.turnLabel.config(text = "Green Turn: Click on a Green square to move!")
                else:
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
            else:
                if (buttonPos[0].cget("bg") != "red"):
                    self.turnLabel.config(text = "Red Turn: Click on a Red square to move!")
                else:
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
                
        else:
            if (self.currentTurn == True):
                if (buttonPos[0].cget("bg") == "yellow"):
                    self.moveTo(row, col)
                    self.nextTurn()
                    self.boardRefresh()
                    self.checkWinCond(self.boardSize) #TESTING
                elif (buttonPos[0].cget("bg") == "green"):
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
            else:
                if (buttonPos[0].cget("bg") == "yellow"):
                    self.moveTo(row, col)
                    self.nextTurn()
                    self.boardRefresh()
                    self.checkWinCond(self.boardSize) #TESTING
                elif (buttonPos[0].cget("bg") == "red"):
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()                

    def onClickHighlight(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (buttonPos[0].cget("bg") == "red"):
            buttonPos[0].config(bg = "maroon")
        elif (buttonPos[0].cget("bg") == "green"):
            buttonPos[0].config(bg = "lightgreen")

    def checkAroundPos(self, row, col):
        #print("rowIn: " + str(row) + " colIn: " + str(col)) #TESTING
        for r in range(row - 1, row + 2):
            if (r <= 0 or r >= self.boardSize + 1):
                pass
                #print("Would be Row error, Pass here") #TESTING
            else:
                #print("Row: " + str(r)) #TESTING
                for c in range(col - 1, col + 2):
                    if (c <= -1 or c >= self.boardSize):
                        pass
                        #print("Would be Column error, Pass here") #TESTING
                    else:
                        if (row == r and c == col):
                            pass
                        else:
                            self.checkMove(r, c)
                            self.checkJump(r, c)
                            # print("Row: " + str(r) + " Col: " + str(c)) #TESTING
        #print("=====") # TESTING

    def setCurrentGridCoordinates(self, row, col):
        self.currentGridX = row
        self.currentGridY = col
        #print(self.currentGridX, self.currentGridY) #TESTING
        
    def checkMove(self, row, col): # Highlights potential basic moves
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (buttonPos[0].cget("bg") == "snow" or buttonPos[0].cget("bg") == "gray60" or buttonPos[0].cget("bg") == "lightblue"):
            buttonPos[0].config(bg = "yellow")
        else:
            pass

    def checkJump(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (buttonPos[0].cget("bg") == "green" or buttonPos[0].cget("bg") == "red"):
            try:
                if (self.currentTurn == True): # This was screwing with me with the corners so i had to arrange the Jumps in a certain order depending on the corner...
                    try:
                        #RightJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY + 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY + 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:   
                    #TopJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX - 1, column = self.currentGridY)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX, column = self.currentGridY)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:    
                        #TopRightJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX - 1, column = self.currentGridY + 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX, column = self.currentGridY + 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:    
                        #TopLeftJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + - 1, column = self.currentGridY - 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX, column = self.currentGridY - 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:    
                        #BotJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 3, column = self.currentGridY)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 2, column = self.currentGridY)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:    
                        #BotLeftJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 3, column = self.currentGridY - 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 2, column = self.currentGridY - 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:    
                        #LeftJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY - 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY - 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:   
                        #BotRightJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 3, column = self.currentGridY + 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 2, column = self.currentGridY + 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass     
                else:
                    try:
                        #BotJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 3, column = self.currentGridY)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 2, column = self.currentGridY)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass 
                    try:
                        #LeftJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY - 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY - 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass 
                    try:    
                        #BotLeftJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 3, column = self.currentGridY - 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 2, column = self.currentGridY - 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass 
                    try:    
                        #BotRightJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 3, column = self.currentGridY + 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 2, column = self.currentGridY + 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass 
                    try:    
                        #TopJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX - 1, column = self.currentGridY)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX, column = self.currentGridY)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass 
                    try:    
                        #TopRightJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX - 1, column = self.currentGridY + 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX, column = self.currentGridY + 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass 
                    try:    
                        #RightJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY + 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX + 1, column = self.currentGridY + 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass
                    try:    
                        #TopLeftJump
                        jumpToPos = self.boardFrame.grid_slaves(row = self.currentGridX + - 1, column = self.currentGridY - 2)
                        jumpOverPos = self.boardFrame.grid_slaves(row = self.currentGridX, column = self.currentGridY - 1)
                        if ((jumpToPos[0].cget("bg") == "snow" or jumpToPos[0].cget("bg") == "gray60" or jumpToPos[0].cget("bg") == "lightblue") and (jumpOverPos[0].cget("bg") == "green" or jumpOverPos[0].cget("bg") == "red")):
                            jumpToPos[0].config(bg = "yellow")
                    except (IndexError, TclError):
                        pass     
            except (IndexError, TclError):
                pass                
        else:
            pass

    def moveTo(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (self.currentTurn == True):        
            buttonPos[0].config(bg = "green")
            self.turnLabel.config(text = "Red Turn: Click on a Red square to move!")
            self.setBetweenMove()
        else:
            buttonPos[0].config(bg = "red")
            self.turnLabel.config(text = "Green Turn: Click on a Green square to move!")
            self.setBetweenMove()

    def setBetweenMove(self):
        if (self.betweenMove == False):
            self.betweenMove = True
        else:
            self.betweenMove = False

    def nextTurn(self):
        if (self.currentTurn == True):
            self.currentTurn = False
        else:
            self.currentTurn = True

    # Win Conditions =====================================================================================
    def checkWinCond(self, size):
        if (size == 8):
            self.checkWinCondition8()
        elif (size == 10):
            self.checkWinCondition10()
        elif (size == 16):
            self.checkWinCondition16()
    
    def checkWinCondition8(self):
        unmarkTop = [(1, 5), (2, 5), (2, 6), (3, 5), (3, 6), (3, 7)]
        unmarkBot = [(6, 1), (6, 2), (7, 2), (6, 3), (7, 3), (8, 3)]
        redPos1 = False
        redPos2 = False
        redPos3 = False
        redPos4 = False
        redPos5 = False
        redPos6 = False
        redPos7 = False
        redPos8 = False
        redPos9 = False
        redPos10 = False
        greenPos1 = False
        greenPos2 = False
        greenPos3 = False
        greenPos4 = False
        greenPos5 = False
        greenPos6 = False
        greenPos7 = False
        greenPos8 = False
        greenPos9 = False
        greenPos10 = False
        for row in range(4):
            for col in range(4):
                if ((row,col+5) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 4)
                    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
                        testButton[0].config(bg = "lightblue")
                    else:
                        if (row == 0 and col + 5 == 5):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos1 = True
                            else:
                                greenPos1 = False
                        if (row == 0 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos2 = True
                            else:
                                greenPos2 = False
                        if (row == 0 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos3 = True
                            else:
                                greenPos3 = False
                        if (row == 1 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos4 = True
                            else:
                                greenPos4 = False
                        if (row == 1 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos5 = True
                            else:
                                greenPos5 = False
                        if (row == 2 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos6 = True
                            else:
                                greenPos6 = False
                        if (row == 0 and col + 5 == 5):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos7 = True
                            else:
                                greenPos7 = False
                        if (row == 1 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos8 = True
                            else:
                                greenPos8 = False
                        if (row == 2 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos9 = True
                            else:
                                greenPos9 = False
                        if (row == 3 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos10 = True
                            else:
                                greenPos10 = False
        for row in range(4):
            for col in range(4):
                if ((row+6,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 5, column = col)
                    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
                        testButton[0].config(bg = "lightblue")
                    else:
                        if (row + 6 == 6 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos1 = True
                            else:
                                redPos1 = False
                        if (row + 6 == 7 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos2 = True
                            else:
                                redPos2 = False
                        if (row + 6 == 7 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos3 = True
                            else:
                                redPos3 = False
                        if (row + 6 == 8 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos4 = True
                            else:
                                redPos4 = False
                        if (row + 6 == 8 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos5 = True
                            else:
                                redPos5 = False
                        if (row + 6 == 8 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos6 = True
                            else:
                                redPos6 = False
                        if (row + 6 == 6 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos7 = True
                            else:
                                redPos7 = False
                        if (row + 6 == 7 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos8 = True
                            else:
                                redPos8 = False
                        if (row + 6 == 8 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos9 = True
                            else:
                                redPos9 = False
                        if (row + 6 == 9 and col == 3):
                            if (testButton[0].cget("bg") == "red"):
                                redPos10 = True
                            else:
                                redPos10 = False
        if (greenPos1 == True and greenPos2 == True and greenPos3 == True and greenPos4 == True and greenPos5 == True and greenPos6 == True and greenPos7 == True and greenPos8 == True and greenPos9 == True and greenPos10 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Green! You won!!!!!")
            self.gameOver = True
        elif (redPos1 == True and redPos2 == True and redPos3 == True and redPos4 == True and redPos5 == True and redPos6 == True and redPos7 == True and redPos8 == True and redPos9 == True and redPos10 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Red! You won!!!!!")
            self.gameOver = True
        

    def checkWinCondition10(self):
        unmarkTop = [(2, 6), (3, 6), (3, 7), (1, 6), (2, 7), (3, 8)]
        unmarkBot = [(7, 2), (7, 3), (8, 3), (7, 1), (8, 2), (9, 3)]
        redPos1 = False
        redPos2 = False
        redPos3 = False
        redPos4 = False
        redPos5 = False
        redPos6 = False
        redPos7 = False
        redPos8 = False
        redPos9 = False
        redPos10 = False
        greenPos1 = False
        greenPos2 = False
        greenPos3 = False
        greenPos4 = False
        greenPos5 = False
        greenPos6 = False
        greenPos7 = False
        greenPos8 = False
        greenPos9 = False
        greenPos10 = False
        for row in range(4):
            for col in range(4):
                if ((row,col+6) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 6)
                    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
                        testButton[0].config(bg = "lightblue")
                    else:
                        if (row == 0 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos1 = True
                            else:
                                greenPos1 = False
                        if (row == 0 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos2 = True
                            else:
                                greenPos2 = False
                        if (row == 0 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos3 = True
                            else:
                                greenPos3 = False
                        if (row == 1 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos4 = True
                            else:
                                greenPos4 = False
                        if (row == 1 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos5 = True
                            else:
                                greenPos5 = False
                        if (row == 2 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos6 = True
                            else:
                                greenPos6 = False
                        if (row == 0 and col + 5 == 5):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos7 = True
                            else:
                                greenPos7 = False
                        if (row == 1 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos8 = True
                            else:
                                greenPos8 = False
                        if (row == 2 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos9 = True
                            else:
                                greenPos9 = False
                        if (row == 3 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos10 = True
                            else:
                                greenPos10 = False
        for row in range(4):
            for col in range(4):
                if ((row+7,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 7, column = col)
                    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
                        testButton[0].config(bg = "lightblue")
                    else:
                        if (row + 6 == 6 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos1 = True
                            else:
                                redPos1 = False
                        if (row + 6 == 7 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos2 = True
                            else:
                                redPos2 = False
                        if (row + 6 == 7 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos3 = True
                            else:
                                redPos3 = False
                        if (row + 6 == 8 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos4 = True
                            else:
                                redPos4 = False
                        if (row + 6 == 8 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos5 = True
                            else:
                                redPos5 = False
                        if (row + 6 == 8 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos6 = True
                            else:
                                redPos6 = False
                        if (row + 6 == 9 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos7 = True
                            else:
                                redPos7 = False
                        if (row + 6 == 9 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos8 = True
                            else:
                                redPos8 = False
                        if (row + 6 == 9 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos9 = True
                            else:
                                redPos9 = False
                        if (row + 6 == 9 and col == 3):
                            if (testButton[0].cget("bg") == "red"):
                                redPos10 = True
                            else:
                                redPos10 = False
        if (greenPos1 == True and greenPos2 == True and greenPos3 == True and greenPos4 == True and greenPos5 == True and greenPos6 == True and greenPos7 == True and greenPos8 == True and greenPos9 == True and greenPos10 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Green! You won!!!!!")
            self.gameOver = True
        elif (redPos1 == True and redPos2 == True and redPos3 == True and redPos4 == True and redPos5 == True and redPos6 == True and redPos7 == True and redPos8 == True and redPos9 == True and redPos10 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Red! You won!!!!!")
            self.gameOver = True
        print(redPos1)
        print(redPos2)
        print(redPos3)
        print(redPos4)
        print(redPos5)
        print(redPos6)
        print(redPos7)
        print(redPos8)
        print(redPos9)
        print(redPos10)
        print("--")


        
    def checkWinCondition16(self):
        unmarkTop = [(2, 11), (3, 11), (4, 11), (4, 12), (3, 12), (4, 13)]
        unmarkBot = [(12, 2), (12, 3), (12, 4), (13, 3), (13, 4), (14, 4)]
        redPos1 = False
        redPos2 = False
        redPos3 = False
        redPos4 = False
        redPos5 = False
        redPos6 = False
        redPos7 = False
        redPos8 = False
        redPos9 = False
        redPos10 = False
        redPos11 = False
        redPos12 = False
        redPos13 = False
        redPos14 = False
        redPos15 = False
        redPos16 = False
        redPos17 = False
        redPos18 = False
        redPos19 = False
        greenPos1 = False
        greenPos2 = False
        greenPos3 = False
        greenPos4 = False
        greenPos5 = False
        greenPos6 = False
        greenPos7 = False
        greenPos8 = False
        greenPos9 = False
        greenPos10 = False
        greenPos11 = False
        greenPos12 = False
        greenPos13 = False
        greenPos14 = False
        greenPos15 = False
        greenPos16 = False
        greenPos17 = False
        greenPos18 = False
        greenPos19 = False
        for row in range(5):
            for col in range(5):
                if ((row,col+11) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 11)
                    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
                        testButton[0].config(bg = "lightblue")
                    else:
                        if (row == 0 and col + 5 == 7):
                            
                            if (testButton[0].cget("bg") == "green"):
                                greenPos1 = True
                            else:
                                greenPos1 = False
                        if (row == 0 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos2 = True
                            else:
                                greenPos2 = False
                        if (row == 0 and col + 5 == 9):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos3 = True
                            else:
                                greenPos3 = False
                        if (row == 1 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos4 = True
                            else:
                                greenPos4 = False
                        if (row == 1 and col + 5 == 9):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos5 = True
                            else:
                                greenPos5 = False
                        if (row == 2 and col + 5 == 9):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos6 = True
                            else:
                                greenPos6 = False
                        if (row == 0 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos7 = True
                            else:
                                greenPos7 = False
                        if (row == 1 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos8 = True
                            else:
                                greenPos8 = False
                        if (row == 2 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos9 = True
                            else:
                                greenPos9 = False
                        if (row == 3 and col + 5 == 9):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos10 = True
                            else:
                                greenPos10 = False
                        if (row == 0 and col + 5 == 5):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos11 = True
                            else:
                                greenPos11 = False
                        if (row == 1 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos12 = True
                            else:
                                greenPos12 = False
                        if (row == 2 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos13 = True
                            else:
                                greenPos13 = False
                        if (row == 3 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos14 = True
                            else:
                                greenPos14 = False
                        if (row == 4 and col + 5 == 9):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos15 = True
                            else:
                                greenPos15 = False
                        if (row == 1 and col + 5 == 5):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos16 = True
                            else:
                                greenPos16 = False
                        if (row == 2 and col + 5 == 6):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos17 = True
                            else:
                                greenPos17 = False
                        if (row == 3 and col + 5 == 7):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos18 = True
                            else:
                                greenPos18 = False
                        if (row == 4 and col + 5 == 8):
                            if (testButton[0].cget("bg") == "green"):
                                greenPos19 = True
                            else:
                                greenPos19 = False
        for row in range(5):
            for col in range(5):
                if ((row+12,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 12, column = col)
                    if (testButton[0].cget("bg") == "snow" or testButton[0].cget("bg") == "gray60"):
                        testButton[0].config(bg = "lightblue")
                    else:
                        if (row + 6 == 7 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos1 = True
                            else:
                                redPos1 = False
                        if (row + 6 == 8 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos2 = True
                            else:
                                redPos2 = False
                        if (row + 6 == 8 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos3 = True
                            else:
                                redPos3 = False
                        if (row + 6 == 9 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos4 = True
                            else:
                                redPos4 = False
                        if (row + 6 == 9 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos5 = True
                            else:
                                redPos5 = False
                        if (row + 6 == 9 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos6 = True
                            else:
                                redPos6 = False
                        if (row + 6 == 10 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos7 = True
                            else:
                                redPos7 = False
                        if (row + 6 == 10 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos8 = True
                            else:
                                redPos8 = False
                        if (row + 6 == 10 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos9 = True
                            else:
                                redPos9 = False
                        if (row + 6 == 10 and col == 3):
                            if (testButton[0].cget("bg") == "red"):
                                redPos10 = True
                            else:
                                redPos10 = False
                        if (row + 6 == 6 and col == 0):
                            if (testButton[0].cget("bg") == "red"):
                                redPos11 = True
                            else:
                                redPos11 = False
                        if (row + 6 == 7 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos12 = True
                            else:
                                redPos12 = False
                        if (row + 6 == 8 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos13 = True
                            else:
                                redPos13 = False
                        if (row + 6 == 9 and col == 3):
                            if (testButton[0].cget("bg") == "red"):
                                redPos14 = True
                            else:
                                redPos14 = False
                        if (row + 6 == 10 and col == 4):
                            if (testButton[0].cget("bg") == "red"):
                                redPos15 = True
                            else:
                                redPos15 = False
                        if (row + 6 == 6 and col == 1):
                            if (testButton[0].cget("bg") == "red"):
                                redPos16 = True
                            else:
                                redPos16 = False
                        if (row + 6 == 7 and col == 2):
                            if (testButton[0].cget("bg") == "red"):
                                redPos17 = True
                            else:
                                redPos17 = False
                        if (row + 6 == 8 and col == 3):
                            if (testButton[0].cget("bg") == "red"):
                                redPos18 = True
                            else:
                                redPos18 = False
                        if (row + 6 == 9 and col == 4):
                            if (testButton[0].cget("bg") == "red"):
                                redPos19 = True
                            else:
                                redPos19 = False
        if (greenPos1 == True and greenPos2 == True and greenPos3 == True and greenPos4 == True and greenPos5 == True and greenPos6 == True and greenPos7 == True and greenPos8 == True and greenPos9 == True and greenPos10 == True and greenPos11 == True and greenPos12 == True and greenPos13 == True and greenPos14 == True and greenPos15 == True and greenPos16 == True and greenPos17 == True and greenPos18 == True and greenPos19 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Green! You won!!!!!")
            self.gameOver = True
        elif (redPos1 == True and redPos2 == True and redPos3 == True and redPos4 == True and redPos5 == True and redPos6 == True and redPos7 == True and redPos8 == True and redPos9 == True and redPos10 == True and redPos11 == True and redPos12 == True and redPos13 == True and redPos14 == True and redPos15 == True and redPos16 == True and redPos17 == True and redPos18 == True and redPos19 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Red! You won!!!!!")
            self.gameOver = True
        print(redPos1)
        print(redPos2)
        print(redPos3)
        print(redPos4)
        print(redPos5)
        print(redPos6)
        print(redPos7)
        print(redPos8)
        print(redPos9)
        print(redPos10)
        print(redPos11)
        print(redPos12)
        print(redPos13)
        print(redPos14)
        print(redPos15)
        print(redPos16)
        print(redPos17)
        print(redPos18)
        print(redPos19)
        print("--")



newGame = HalmaBoard()
newGame.createBoard(8)
newGame.startMainLoop()
        
