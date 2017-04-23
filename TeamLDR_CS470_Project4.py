from tkinter import *
import asyncio

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

    # Board setup.    
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
        unmarkTop = [(2, 6), (3, 6), (3, 7)]
        unmarkBot = [(7, 2), (7, 3), (8, 3)]
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
        unmarkTop = [(1, 5), (2, 5), (2, 6)]
        unmarkBot = [(6, 1), (6, 2), (7, 2)]
        for row in range(3):
            for col in range(3):
                if ((row,col+5) not in unmarkTop):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 5)
                    testButton[0].config(bg = "red")
        for row in range(3):
            for col in range(3):
                if ((row+6,col) not in unmarkBot):
                    testButton = self.boardFrame.grid_slaves(row = row + 6, column = col)
                    testButton[0].config(bg = "green")
                    
    def setBoardUp(self, size):
        allowedBoardSizes = [8, 10, 16]
        if (size not in allowedBoardSizes):
            print("Invalid Board")
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
                    if (testButton[0].cget("bg") == "yellow" or testButton[0].cget("bg") == "lightgreen"):
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
                    if (testButton[0].cget("bg") == "yellow" or testButton[0].cget("bg") == "lightgreen" ):
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

    # Click detection on grid.
    def onClick(self, x, y):
        print("Current Turn: " + str(self.currentTurn))
        print("In Move: " + str(self.betweenMove))
        col,row = self.boardFrame.grid_location(x, y)
        col = col
        row = row
        self.validateMoveSequence(row, col)
    
    def findMousePos(self, event):
        curX = self.boardFrame.winfo_rootx()
        curY = self.boardFrame.winfo_rooty()
        clickX = event.x_root
        clickY = event.y_root
        curPosClickX = clickX - curX
        curPosClickY = clickY - curY
        self.boardFrame.focus_set()
        self.onClick(curPosClickX, curPosClickY)


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
        self.mainWindow.wm_geometry("500x542") #942 -> 42 comes from the height of the titleLabel+turnLabel.
        self.mainWindow.resizable(0,0)

    def startMainLoop(self):
        self.mainWindow.mainloop()


    
    # Move related functions.
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
            if (buttonPos[0].cget("bg") == "yellow"):
                #self.testYellow(row, col)
                self.moveTo(row, col)
                self.boardRefresh()
            elif (buttonPos[0].cget("bg") == "green"):
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
        #print("rowIn: " + str(row) + " colIn: " + str(col))
        for r in range(row - 1, row + 2):
            if (r == 0 or r == self.boardSize + 1):
                print("Would be Row error, Pass here")
            else:
                #print("Row: " + str(r))
                for c in range(col - 1, col + 2):
                    if (c == -1 or c == self.boardSize):
                        print("Would be Column error, Pass here")
                    else:
                        if (row == r and c == col):
                            pass
                        else:
                            # Check around
                            self.checkMove(r, c)
                            # print("Row: " + str(r) + " Col: " + str(c))
        print("=====")

    def checkMove(self, row, col): # Highlights potential jumps
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (buttonPos[0].cget("bg") == "snow" or buttonPos[0].cget("bg") == "gray60"):
            buttonPos[0].config(bg = "yellow")
        else:
            # Account for jumps here.
            pass
        
    #def testYellow(self, row, col):
    #    testButton = self.boardFrame.grid_slaves(row = row, column = col)
    #    if (testButton[0].cget("bg") == "yellow"):
    #        self.boardRefresh()
    #    else:
    #        if (self.currentTurn == True):
    #            if (testButton[0].cget("bg") == "green"):
    #                pass
    #        else:
    #            pass
   
    def moveTo(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (self.currentTurn == True):        
            buttonPos[0].config(bg = "green")
            self.setBetweenMove()
        else:
            buttonPos[0].config(bg = "red")

    def setBetweenMove(self):
        if (self.betweenMove == False):
            self.betweenMove = True
        else:
            self.betweenMove = False

    # Player turns.



newGame = HalmaBoard()
newGame.createBoard(16)
newGame.startMainLoop()
        
