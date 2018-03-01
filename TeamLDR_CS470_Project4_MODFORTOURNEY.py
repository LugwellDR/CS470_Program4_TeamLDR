from tkinter import *
import time
import random
import math

class HalmaBoard():

    def __init__(self):
        self.fontSize = 22
        self.boardRes = "900x942" #1300x1342 on surface
        self.boardSize = 0
        self.isHuman = False
        self.currentTurn = False
        self.betweenMove = False
        self.mainWindow = Tk()
        self.timerCount = 0
        self.boardFrame = Frame(self.mainWindow)
        self.titleLabel = Label(self.boardFrame, text = "Halma Game", font=("Georgia",self.fontSize))
        self.greenPlayer = Label(self.boardFrame, text = "", font=("Georgia",self.fontSize))
        self.redPlayer = Label(self.boardFrame, text = "", font=("Georgia",self.fontSize))
        self.buttonList = []
        self.turnLabel = Label(self.boardFrame, text = "Green Turn: Starting Move", font=("Georgia",self.fontSize))
        self.moveToLabel = Label(self.boardFrame, text = "", font=("Georgia",self.fontSize))
        self.redScoreLabel = Label(self.boardFrame, text = "", font=("Georgia",self.fontSize))
        self.greenScoreLabel = Label(self.boardFrame, text = "", font=("Georgia",self.fontSize))
        self.moveNumberLabel = Label(self.boardFrame, text = "Move Count: 0", font=("Georgia",self.fontSize))
        self.labelListLetters = []
        self.labelListNumbers = []
        self.currentGridX = 0
        self.currentGridY = 0
        self.toGridX = 0
        self.toGridY = 0
        self.whichColor = ""
        self.greenScore = 0
        self.redScore = 0
        self.moveTotal = 0
        self.alpha16 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        self.gameOver = False
        self.potentialMoves = []
        self.greenPiecesCurrentPosition = [(5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (8, 3)]
        self.redPiecesCurrentPosition = [(1, 4), (1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 6), (3, 7), (4, 7)]
        self.redColor = "red"
        self.redHighlightColor = "magenta"
        self.redCornerColor = "pink"
        self.greenColor = "darkgreen"
        self.greenHighlightColor = "lawngreen"
        self.greenCornerColor = "palegreen"
        self.moveToHighlightColor = "yellow"
        self.boardTileLight = "snow"
        self.boardTileDark = "gray60"
        self.redCornerUnmark = [(1, 5), (2, 5), (2, 6), (3, 5), (3, 6), (3, 7)]
        self.greenCornerUnmark = [(6, 1), (6, 2), (7, 2), (6, 3), (7, 3), (8, 3)]
        self.redCorner = [(1, 4), (1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 6), (3, 7), (4, 7)]
        self.greenCorner = [(5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (8, 3)]
        self.redGoodness = {10:((7, 0)),
                            9:((5, 0), (6, 0), (7, 1), (7, 2)),
                            8:((6, 1), (4, 0), (7, 3) ),
                            7:((5, 1), (6, 2)),
                            6:((5, 2), (4, 1), (6, 3)),
                            5:((3, 1), (4, 2), (4, 3), (5, 3), (6, 4), (3, 0), (7, 4)),
                            4:((3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (2, 0), (2, 1), (6, 5), (7, 5)),
                            3:((2, 2), (2, 3), (4, 5), (5, 5), (1, 0), (7, 6)),
                            2:((1, 1), (1, 2), (1, 3), (1, 4), (3, 6), (4, 6), (5, 6), (6, 6), (2, 5), (2, 4), (3, 5)),
                            1:((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (1, 5), (1, 6), (2, 6))
                            }
        
        self.greenGoodness = {10:((0, 7)),
                              9:((0, 5), (0, 6), (1, 7), (2, 7)),
                              8:((2, 6), (0, 4), (3, 7)),
                              7:((1, 6), (1, 5)),
                              6:((1, 4), (2, 5), (3, 6)),
                              5:((1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (4, 7), (0, 3)),
                              4:((2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (0, 2), (1, 2), (5, 6), (5, 7)),
                              3:((2, 2), (3, 2), (5, 4), (5, 5), (0, 1), (6, 7)),
                              2:((1, 1), (2, 1), (3, 1), (4, 1), (6, 3), (6, 4), (6, 5), (6, 6), (5, 2), (4, 2), (5, 3)),
                              1:((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (5, 1), (6, 1), (6, 2))
                              }


    # Board setup ========================================================================================
    def set8(self):
        for row in range(4):
            for col in range(4):
                if ((row,col+5) not in self.redCornerUnmark):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 4)
                    testButton[0].config(bg = self.redColor)
        for row in range(4):
            for col in range(4):
                if ((row+6,col) not in self.greenCornerUnmark):
                    testButton = self.boardFrame.grid_slaves(row = row + 5, column = col)
                    testButton[0].config(bg = self.greenColor)
                    
    def setBoardUp(self, size):
        allowedBoardSizes = [8]
        if (size not in allowedBoardSizes):
            print("Invalid Board")
            self.turnLabel.config(text = "Invalid Board: Reset Game With board size [8]!", font=("Georgia",22))
            self.gameOver = True
        else:
            self.set8()

    def boardRefresh(self):
        self.greenPiecesCurrentPosition = []
        self.redPiecesCurrentPosition = []
        if (self.betweenMove == False):
            for row in range(self.boardSize):
                for col in range (self.boardSize):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col)
                    if (testButton[0].cget("bg") == self.redHighlightColor):
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = self.redHighlightColor
                    if (testButton[0].cget("bg") == self.greenHighlightColor):
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = self.greenHighlightColor
                    if (testButton[0].cget("bg") == self.moveToHighlightColor or testButton[0].cget("bg") == self.greenHighlightColor or testButton[0].cget("bg") == self.redHighlightColor):
                        if (row%2 == 0):
                            if (col%2 == 0):
                                testButton[0].config(bg = self.boardTileLight)
                            else:
                                testButton[0].config(bg = self.boardTileDark)
                        else:
                            if (col%2 != 0):
                                testButton[0].config(bg = self.boardTileLight)
                            else:
                                testButton[0].config(bg = self.boardTileDark)
                    else:
                        if (testButton[0].cget("bg") == self.greenColor):
                            self.greenPiecesCurrentPosition.append((row + 1, col))
                        elif (testButton[0].cget("bg") == self.redColor):
                            self.redPiecesCurrentPosition.append((row + 1, col))
                        pass
        else:
            for row in range(self.boardSize):
                for col in range (self.boardSize):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col)
                    if (testButton[0].cget("bg") == self.greenHighlightColor):
                        testButton[0].config(bg = self.greenColor)
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = self.greenHighlightColor
                    if (testButton[0].cget("bg") == self.redHighlightColor):
                        testButton[0].config(bg = self.redColor)
                        self.moveFromRow = row + 1
                        self.moveFromCol = col
                        self.whichColor = self.redHighlightColor
                    if (testButton[0].cget("bg") == self.moveToHighlightColor or testButton[0].cget("bg") == self.greenHighlightColor or testButton[0].cget("bg") == self.redHighlightColor):
                        if (row%2 == 0):
                            if (col%2 == 0):
                                testButton[0].config(bg = self.boardTileLight)
                            else:
                                testButton[0].config(bg = self.boardTileDark)
                        else:
                            if (col%2 != 0):
                                testButton[0].config(bg = self.boardTileLight)
                            else:
                                testButton[0].config(bg = self.boardTileDark)
                    else:
                        if (testButton[0].cget("bg") == self.greenColor):
                            self.greenPiecesCurrentPosition.append((row + 1, col))
                        elif (testButton[0].cget("bg") == self.redColor):
                            self.redPiecesCurrentPosition.append((row + 1, col))
                        pass
        for row in range(4):
            for col in range(4):
                if ((row,col+5) not in self.redCornerUnmark):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 4)
                    if (testButton[0].cget("bg") == self.boardTileLight or testButton[0].cget("bg") == self.boardTileDark):
                        testButton[0].config(bg = self.redCornerColor)
        for row in range(4):
            for col in range(4):
                if ((row+6,col) not in self.greenCornerUnmark):
                    testButton = self.boardFrame.grid_slaves(row = row + 5, column = col)
                    if (testButton[0].cget("bg") == self.boardTileLight or testButton[0].cget("bg") == self.boardTileDark):
                        testButton[0].config(bg = self.greenCornerColor)
        """
        print("Current POS for Green: ", end="")
        print(self.greenPiecesCurrentPosition)
        print("Current POS for Red: ", end="")
        print(self.redPiecesCurrentPosition)
        """

    # Click detection on grid ============================================================================
    def onClick(self, x, y):
        #print("Current Turn: " + str(self.currentTurn)) # TESTING
        #print("In Move: " + str(self.betweenMove)) # TESTING
        col,row = self.boardFrame.grid_location(x, y)
        col = col
        row = row
        self.setCurrentGridCoordinates(row - 1, col)
        #print(self.currentGridX, self.currentGridY) #TESTING
        self.setCurrentToGridCoordinates(row - 1, col)
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

    # Override functions to ensure our opponent can make a valid move ===================================
    def findMousePosOVERRIDE(self, event):
        if (self.gameOver == False):
            curX = self.boardFrame.winfo_rootx()
            curY = self.boardFrame.winfo_rooty()
            clickX = event.x_root
            clickY = event.y_root
            curPosClickX = clickX - curX
            curPosClickY = clickY - curY
            self.boardFrame.focus_set()
            self.onClickOVERRIDE(curPosClickX, curPosClickY)
        else:
            pass

    def onClickOVERRIDE(self, x, y):
        col,row = self.boardFrame.grid_location(x, y)
        col = col
        row = row
        self.setCurrentGridCoordinates(row - 1, col)
        self.setCurrentToGridCoordinates(row - 1, col)
        self.validateMoveSequenceOVERRIDE(row, col)

    def validateMoveSequenceOVERRIDE(self, row, col):
        self.potentialMoves = []
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (self.betweenMove == True): # Second Click
            if (self.currentTurn == True):
                if (buttonPos[0].cget("bg") == self.moveToHighlightColor
                    or buttonPos[0].cget("bg") == self.boardTileLight
                    or buttonPos[0].cget("bg") == self.boardTileDark
                    or buttonPos[0].cget("bg") == self.redCornerColor): # Moves
                    self.moveTo(row, col)
                    self.nextTurn()
                    self.boardRefresh()
                    self.moveTotal += 1
                    self.moveNumberLabel.config(text = "Move Count: " + str(self.moveTotal))  
                    #self.checkWinCond(self.boardSize)
                    print("Green move Overridden")
                    self.setBetweenMove()
                    self.betweenMove = False
                elif (buttonPos[0].cget("bg") == self.greenColor): # Resets
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
                    self.findFarthestDistance(row, col)
            else:
                if (buttonPos[0].cget("bg") == self.moveToHighlightColor
                    or buttonPos[0].cget("bg") == self.boardTileLight
                    or buttonPos[0].cget("bg") == self.boardTileDark
                    or buttonPos[0].cget("bg") == self.greenCornerColor): # Moves
                    self.moveTo(row, col)
                    self.nextTurn()
                    self.boardRefresh()
                    self.moveTotal += 1
                    self.moveNumberLabel.config(text = "Move Count: " + str(self.moveTotal))  
                    #self.checkWinCond(self.boardSize)
                    print("Red move Overridden")
                    self.setBetweenMove()
                    self.betweenMove = False
                elif (buttonPos[0].cget("bg") == self.redColor): # Resets
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
        ###print(self.potentialMoves)
        #self.findFarthestDistance(row, col)

    #Create board and start main loop ==========================================================
    def createBoard(self, size):
        self.boardSize = size
        Grid.rowconfigure(self.mainWindow, 0, weight = 1)
        Grid.columnconfigure(self.mainWindow, 0, weight = 1)
        self.boardFrame.grid(row = 0, column = 0, stick = N + S + E + W)
        self.titleLabel.grid(row = 0, column = 2, columnspan = 4, pady = 0)
        self.greenPlayer.grid(row = 0, column = 0, columnspan = 2, pady = 0)
        self.redPlayer.grid(row = 0, column = 6, columnspan = 2, pady = 0)
        self.turnLabel.grid(row = self.boardSize + 3, column = 0, columnspan = self.boardSize, pady = 0)
        self.moveToLabel.grid(row = self.boardSize + 4, column = 0, columnspan = self.boardSize, pady = 0)
        if (self.boardSize == 8):
            self.greenScoreLabel.grid(row = self.boardSize + 2, column = 0, columnspan = 2, pady = 0)
            self.moveNumberLabel.grid(row = self.boardSize + 2, column = 2, columnspan = 4, pady = 0)
            self.redScoreLabel.grid(row = self.boardSize + 2, column = 6, columnspan = 2, pady = 0)
        for num in range(self.boardSize * self.boardSize):
            self.buttonList.append(Button(self.boardFrame))
        for num in range(self.boardSize):
            self.labelListLetters.append(Label(self.boardFrame, text = self.alpha16[num], font=("Georgia",self.fontSize)))
            self.labelListNumbers.append(Label(self.boardFrame, text = str(num + 1), font=("Georgia",self.fontSize)))
        for col in range(self.boardSize):
            self.labelListLetters[col].grid(row = self.boardSize + 1, column = col, pady = 0)
            self.labelListNumbers[col].grid(row = col + 1, column = self.boardSize + 1, padx = 7)
        count = 0
        for row in range(self.boardSize):
            Grid.rowconfigure(self.boardFrame, row + 1, weight = 1)
            for col in range(self.boardSize):
                Grid.columnconfigure(self.boardFrame, col, weight = 1)
                aButton = self.buttonList[count]
                if (row%2 == 0):
                    if (col%2 == 0):
                        aButton.config(bg = self.boardTileLight)
                    else:
                        aButton.config(bg = self.boardTileDark)
                else:
                    if (col%2 != 0):
                        aButton.config(bg = self.boardTileLight)
                    else:
                        aButton.config(bg = self.boardTileDark)
                aButton.grid(row = row + 1, column = col, sticky = N + S + E + W)
                aButton.bind("<Button-1>", self.findMousePos)
                aButton.bind("<Button-3>", self.findMousePosOVERRIDE)
                count += 1
        self.setBoardUp(self.boardSize)
        self.mainWindow.wm_geometry(self.boardRes) #942 -> 42 comes from the height of the titleLabel+turnLabel.
        self.mainWindow.resizable(0,0)

    def startMainLoop(self):
        self.mainWindow.mainloop()
    
    # Move related functions =============================================================================
    def validateMoveSequence(self, row, col):
        self.potentialMoves = []
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (self.betweenMove == False): # First Click
            if (self.currentTurn == True):
                if (buttonPos[0].cget("bg") != self.greenColor):
                    self.turnLabel.config(text = "Green Turn: Click on a Green square to move!")
                else:
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
            else:
                if (buttonPos[0].cget("bg") != self.redColor):
                    self.turnLabel.config(text = "Red Turn: Click on a Red square to move!")
                else:
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
            self.findFarthestDistance(row, col)
        else: # Second Click
            if (self.currentTurn == True):
                if (buttonPos[0].cget("bg") == self.moveToHighlightColor): # Moves
                    self.moveTo(row, col)
                    #self.checkWinCond(self.boardSize)
                    self.nextTurn()
                    self.boardRefresh()
                    self.moveTotal += 1
                    self.moveNumberLabel.config(text = "Move Count: " + str(self.moveTotal))  
                    self.setBetweenMove()
                    self.betweenMove = False
                elif (buttonPos[0].cget("bg") == self.greenColor): # Resets
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
                    self.findFarthestDistance(row, col)
            else:
                if (buttonPos[0].cget("bg") == self.moveToHighlightColor): # Moves
                    self.moveTo(row, col)
                    #self.checkWinCond(self.boardSize)
                    self.nextTurn()
                    self.boardRefresh()
                    self.moveTotal += 1
                    self.moveNumberLabel.config(text = "Move Count: " + str(self.moveTotal))  
                    self.setBetweenMove()
                    self.betweenMove = False
                elif (buttonPos[0].cget("bg") == self.redColor): # Resets
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
        ###print(self.potentialMoves)
        #self.findFarthestDistance(row, col)

    def onClickHighlight(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        #self.findGridName(row, col)
        #self.findFarthestDistance(row, col)
        if (buttonPos[0].cget("bg") == self.redColor):
            buttonPos[0].config(bg = self.redHighlightColor)
        elif (buttonPos[0].cget("bg") == self.greenColor):
            buttonPos[0].config(bg = self.greenHighlightColor)

    def checkAroundPos(self, row, col):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (row == r and c == col):
                    pass
                else:
                    if (self.currentTurn == True): #GREENTURN
                        if ((row, col) in self.greenCorner):
                            self.checkMove(r, c, True, False)
                            self.checkJump(r, c, True, False)
                        elif ((row, col) in self.redCorner):
                            self.checkMove(r, c, False, True)
                            self.checkJump(r, c, False, True)
                        else:
                            self.checkMove(r, c, False, False)
                            self.checkJump(r, c, False, False)
                    else: #REDTURN
                        if ((row, col) in self.redCorner):
                            self.checkMove(r, c, True, False)
                            self.checkJump(r, c, True, False)
                        elif ((row, col) in self.greenCorner):
                            self.checkMove(r, c, False, True)
                            self.checkJump(r, c, False, True)
                        else:
                            self.checkMove(r, c, False, False)
                            self.checkJump(r, c, False, False)
                    
    def setCurrentToGridCoordinates(self, row, col):
        self.toGridX = row
        self.toGridY = col
    
    def setCurrentGridCoordinates(self, row, col):
        self.currentGridX = row
        self.currentGridY = col
        #print(self.currentGridX, self.currentGridY) #TESTING
        
    def checkMove(self, row, col, inOwnGoal, inOtherGoal): # Highlights potential basic moves
        try:
            buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
            if (inOwnGoal == False and inOtherGoal == False):
                if (self.currentTurn == True): #GREENTURN
                    if (buttonPos[0].cget("bg") == self.boardTileLight or buttonPos[0].cget("bg") == self.boardTileDark
                        or buttonPos[0].cget("bg") == self.redCornerColor):
                        buttonPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((row, col))
                    else:
                        pass
                else: #REDTURN
                    if (buttonPos[0].cget("bg") == self.boardTileLight or buttonPos[0].cget("bg") == self.boardTileDark
                        or buttonPos[0].cget("bg") == self.greenCornerColor):
                        buttonPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((row, col))
                    else:
                        pass
            elif (inOtherGoal == True):
                if (self.currentTurn == True): #GREENTURN
                    if (buttonPos[0].cget("bg") == self.redCornerColor):
                        buttonPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((row, col))
                    else:
                        pass
                else: #REDTURN
                    if (buttonPos[0].cget("bg") == self.greenCornerColor):
                        buttonPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((row, col))
                    else:
                        pass
            else:
                if (buttonPos[0].cget("bg") == self.boardTileLight or buttonPos[0].cget("bg") == self.boardTileDark
                    or buttonPos[0].cget("bg") == self.greenCornerColor or buttonPos[0].cget("bg") == self.redCornerColor):
                    buttonPos[0].config(bg = self.moveToHighlightColor)
                    self.potentialMoves.append((row, col))
                else:
                    pass 
        except (IndexError, TclError):
            pass

    def checkMultiJump(self, row, col):
        #testPos = self.boardFrame.grid_slaves(row = row, column = col) #TESTING
        #testPos[0].config(bg = "blue") #TESTING
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (row == r and c == col):
                    pass
                else:
                    if (self.currentTurn == True): #GREENTURN
                        if ((row, col) in self.greenCorner):
                            self.checkJump(r, c, True, False)
                        elif ((row, col) in self.redCorner):
                            self.checkJump(r, c, False, True)
                        else:
                            self.checkJump(r, c, False, False)
                    else: #REDTURN
                        if ((row, col) in self.redCorner):
                            self.checkJump(r, c, True, False)
                        elif ((row, col) in self.greenCorner):
                            self.checkJump(r, c, False, True)
                        else:
                            self.checkJump(r, c, False, False)
                    #print(self.toGridX, self.toGridY, self.currentGridX, self.currentGridY) #TESTING
        #print("===") # TESTING

    def moveTo(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (self.currentTurn == True):        
            buttonPos[0].config(bg = self.greenColor)
            self.turnLabel.config(text = "Red Turn: Click on a Red square to move!")
            self.setBetweenMove()
        else:
            buttonPos[0].config(bg = self.redColor)
            self.turnLabel.config(text = "Green Turn: Click on a Green square to move!")
            self.setBetweenMove()

    def setBetweenMove(self):
        if (self.betweenMove == False):
            self.betweenMove = True
        else:
            self.betweenMove = False

    def nextTurn(self):
        self.checkWinCond(self.boardSize)
        if (self.currentTurn == True):
            self.currentTurn = False
            if (self.gameOver == False):
                self.moveToLabel.config(text = "Human Turn")
            else:
                self.moveToLabel.config(text = "Game Over")
            if (self.isHuman == True):
                self.findBestMove()
            #self.findBestMove()
        else:
            self.currentTurn = True
            if (self.gameOver == False):
                self.moveToLabel.config(text = "Human Turn")
            else:
                self.moveToLabel.config(text = "Game Over")
            if (self.isHuman == False):
                self.findBestMove()
            #self.findBestMove()
           

    def jumpAround(self, tox, toy, ovx, ovy, pox, poy, cux, cuy, inOwnGoal, inOtherGoal):
        try:
            jumpToPos = self.boardFrame.grid_slaves(row = self.toGridX + tox, column = self.toGridY + toy)
            jumpOverPos = self.boardFrame.grid_slaves(row = self.toGridX + ovx, column = self.toGridY + ovy)
            #jumpToPos[0].config(bg = "purple") #TESTING
            #jumpOverPos[0].config(bg = "red") #TESTING
            if (inOwnGoal == False and inOtherGoal == False):
                if (self.currentTurn == True): #GREENTURN
                    if ((jumpToPos[0].cget("bg") == self.boardTileLight or jumpToPos[0].cget("bg") == self.boardTileDark
                         or jumpToPos[0].cget("bg") == self.redCornerColor)
                        and (jumpOverPos[0].cget("bg") == self.greenColor or jumpOverPos[0].cget("bg") == self.redColor)):
                        jumpToPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((self.toGridX + pox, self.toGridY + poy))
                        self.setCurrentToGridCoordinates(self.toGridX + cux, self.toGridY + cuy)
                        #testPos = self.boardFrame.grid_slaves(row = self.toGridX, column = self.toGridY) #TESTING
                        #testPos[0].config(bg = "pink") #TESTING
                        self.checkMultiJump(self.toGridX, self.toGridY)
                        self.setCurrentToGridCoordinates(self.currentGridX, self.currentGridY)
                    else:
                        pass
                else: #REDTURN
                    if ((jumpToPos[0].cget("bg") == self.boardTileLight or jumpToPos[0].cget("bg") == self.boardTileDark
                         or jumpToPos[0].cget("bg") == self.greenCornerColor)
                        and (jumpOverPos[0].cget("bg") == self.greenColor or jumpOverPos[0].cget("bg") == self.redColor)):
                        jumpToPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((self.toGridX + pox, self.toGridY + poy))
                        self.setCurrentToGridCoordinates(self.toGridX + cux, self.toGridY + cuy)
                        self.checkMultiJump(self.toGridX, self.toGridY)
                        self.setCurrentToGridCoordinates(self.currentGridX, self.currentGridY)
                    else:
                        pass
            elif (inOtherGoal == True):
                if (self.currentTurn == True): #GREENTURN
                    if ((jumpToPos[0].cget("bg") == self.redCornerColor)
                        and (jumpOverPos[0].cget("bg") == self.greenColor or jumpOverPos[0].cget("bg") == self.redColor)):
                        jumpToPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((self.toGridX + pox, self.toGridY + poy))
                        self.setCurrentToGridCoordinates(self.toGridX + cux, self.toGridY + cuy)
                        self.checkMultiJump(self.toGridX, self.toGridY)
                        self.setCurrentToGridCoordinates(self.currentGridX, self.currentGridY)
                    else:
                        pass
                else: #REDTURN
                    if ((jumpToPos[0].cget("bg") == self.greenCornerColor)
                        and (jumpOverPos[0].cget("bg") == self.greenColor or jumpOverPos[0].cget("bg") == self.redColor)):
                        jumpToPos[0].config(bg = self.moveToHighlightColor)
                        self.potentialMoves.append((self.toGridX + pox, self.toGridY + poy))
                        self.setCurrentToGridCoordinates(self.toGridX + cux, self.toGridY + cuy)
                        self.checkMultiJump(self.toGridX, self.toGridY)
                        self.setCurrentToGridCoordinates(self.currentGridX, self.currentGridY)
                    else:
                        pass
            else:
                if ((jumpToPos[0].cget("bg") == self.boardTileLight or jumpToPos[0].cget("bg") == self.boardTileDark
                     or jumpToPos[0].cget("bg") == self.greenCornerColor or jumpToPos[0].cget("bg") == self.redCornerColor)
                    and (jumpOverPos[0].cget("bg") == self.greenColor or jumpOverPos[0].cget("bg") == self.redColor)):
                    jumpToPos[0].config(bg = self.moveToHighlightColor)
                    self.potentialMoves.append((self.toGridX + pox, self.toGridY + poy))
                    self.setCurrentToGridCoordinates(self.toGridX + cux, self.toGridY + cuy)
                    self.checkMultiJump(self.toGridX, self.toGridY)
                    self.setCurrentToGridCoordinates(self.currentGridX, self.currentGridY)
                else:
                    pass
        except (IndexError, TclError):
            pass
                          
    def checkJump(self, row, col, inOwnGoal, inOtherGoal):
        try:
            buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
            if (buttonPos[0].cget("bg") == self.greenColor or buttonPos[0].cget("bg") == self.redColor or buttonPos[0].cget("bg") == self.moveToHighlightColor):
                try:
                    if (self.currentTurn == True): # GREEN PLAYER
                        self.jumpAround(1, 2, 1, 1, 1, 2, 0, 2, inOwnGoal, inOtherGoal)
                        self.jumpAround(-1, 0, 0, 0, -1, 0, -2, 0, inOwnGoal, inOtherGoal)
                        self.jumpAround(-1, 2, 0, 1, -1, 2, -2, 2, inOwnGoal, inOtherGoal)
                        self.jumpAround(-1, -2, 0, -1, -1, -2, -2, -2, inOwnGoal, inOtherGoal)
                        self.jumpAround(3, 0, 2, 0, 3, 0, 2, 0, inOwnGoal, inOtherGoal)
                        self.jumpAround(3, -2, 2, -1, 3, -2, 2, -2, inOwnGoal, inOtherGoal)
                        self.jumpAround(1, -2, 1, -1, 1, -2, 0, -2, inOwnGoal, inOtherGoal)
                        self.jumpAround(3, 2, 2, 1, 3, 2, 2, 2, inOwnGoal, inOtherGoal)
                    else: # RED PLAYER
                        self.jumpAround(3, 0, 2, 0, 3, 0, 2, 0, inOwnGoal, inOtherGoal)
                        self.jumpAround(1, -2, 1, -1, 1, -2, 0, -2, inOwnGoal, inOtherGoal)
                        self.jumpAround(3, -2, 2, -1, 3, -2, 2, -2, inOwnGoal, inOtherGoal)
                        self.jumpAround(3, 2, 2, 1, 3, 2, 2, 2, inOwnGoal, inOtherGoal)
                        self.jumpAround(-1, 0, 0, 0, -1, 0, -2, 0, inOwnGoal, inOtherGoal)
                        self.jumpAround(-1, 2, 0, 1, -1, 2, -2, 2, inOwnGoal, inOtherGoal)
                        self.jumpAround(1, 2, 1, 1, 1, 2, 0, 2, inOwnGoal, inOtherGoal)
                        self.jumpAround(-1, -2, 0, -1, -1, -2, -2, -2, inOwnGoal, inOtherGoal) 
                except (IndexError, TclError):
                    pass                
            else:
                pass
        except (IndexError, TclError):
            pass

    # Win Conditions =====================================================================================
    def checkWinCond(self, size):
        if (size == 8):
            self.checkWinCondition8()
    
    def checkWinCondition8(self):
        greenScoreCounter = [False, False, False, False, False, False, False, False, False, False]
        redScoreCounter = [False, False, False, False, False, False, False, False, False, False]
        redPos1, redPos2, redPos3, redPos4, redPos5, redPos6, redPos7, redPos8, redPos9, redPos10 = False, False, False, False, False, False, False, False, False, False
        greenPos1, greenPos2, greenPos3, greenPos4, greenPos5, greenPos6, greenPos7, greenPos8, greenPos9, greenPos10 = False, False, False, False, False, False, False, False, False, False
        for row in range(4):
            for col in range(4):
                if ((row,col+5) not in self.redCornerUnmark):
                    testButton = self.boardFrame.grid_slaves(row = row + 1, column = col + 4)
                    if (testButton[0].cget("bg") == self.boardTileLight or testButton[0].cget("bg") == self.boardTileDark):
                        testButton[0].config(bg = self.redCornerColor)
                    else:
                        if (row == 0 and col + 5 == 6):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos1 = True
                                greenScoreCounter[0] = True
                            else:
                                greenPos1 = False
                                greenScoreCounter[0] = False
                        if (row == 0 and col + 5 == 7):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos2 = True
                                greenScoreCounter[1] = True
                            else:
                                greenPos2 = False
                                greenScoreCounter[1] = False
                        if (row == 0 and col + 5 == 8):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos3 = True
                                greenScoreCounter[2] = True
                            else:
                                greenPos3 = False
                                greenScoreCounter[2] = False
                        if (row == 1 and col + 5 == 7):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos4 = True
                                greenScoreCounter[3] = True
                            else:
                                greenPos4 = False
                                greenScoreCounter[3] = False
                        if (row == 1 and col + 5 == 8):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos5 = True
                                greenScoreCounter[4] = True
                            else:
                                greenPos5 = False
                                greenScoreCounter[4] = False
                        if (row == 2 and col + 5 == 8):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos6 = True
                                greenScoreCounter[5] = True
                            else:
                                greenPos6 = False
                                greenScoreCounter[5] = False
                        if (row == 0 and col + 5 == 5):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos7 = True
                                greenScoreCounter[6] = True
                            else:
                                greenPos7 = False
                                greenScoreCounter[6] = False
                        if (row == 1 and col + 5 == 6):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos8 = True
                                greenScoreCounter[7] = True
                            else:
                                greenPos8 = False
                                greenScoreCounter[7] = False
                        if (row == 2 and col + 5 == 7):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos9 = True
                                greenScoreCounter[8] = True
                            else:
                                greenPos9 = False
                                greenScoreCounter[8] = False
                        if (row == 3 and col + 5 == 8):
                            if (testButton[0].cget("bg") == self.greenColor):
                                greenPos10 = True
                                greenScoreCounter[9] = True
                            else:
                                greenPos10 = False
                                greenScoreCounter[9] = False
        for row in range(4):
            for col in range(4):
                if ((row+6,col) not in self.greenCornerUnmark):
                    testButton = self.boardFrame.grid_slaves(row = row + 5, column = col)
                    if (testButton[0].cget("bg") == self.boardTileLight or testButton[0].cget("bg") == self.boardTileDark):
                        testButton[0].config(bg = self.greenCornerColor)
                    else:
                        if (row + 6 == 7 and col == 0):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos1 = True
                                redScoreCounter[0] = True
                            else:
                                redPos1 = False
                                redScoreCounter[0] = False
                        if (row + 6 == 8 and col == 0):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos2 = True
                                redScoreCounter[1] = True
                            else:
                                redPos2 = False
                                redScoreCounter[1] = False
                        if (row + 6 == 8 and col == 1):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos3 = True
                                redScoreCounter[2] = True
                            else:
                                redPos3 = False
                                redScoreCounter[2] = False
                        if (row + 6 == 9 and col == 0):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos4 = True
                                redScoreCounter[3] = True
                            else:
                                redPos4 = False
                                redScoreCounter[3] = False
                        if (row + 6 == 9 and col == 1):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos5 = True
                                redScoreCounter[4] = True
                            else:
                                redPos5 = False
                                redScoreCounter[4] = False
                        if (row + 6 == 9 and col == 2):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos6 = True
                                redScoreCounter[5] = True
                            else:
                                redPos6 = False
                                redScoreCounter[5] = False
                        if (row + 6 == 6 and col == 0):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos7 = True
                                redScoreCounter[6] = True
                            else:
                                redPos7 = False
                                redScoreCounter[6] = False
                        if (row + 6 == 7 and col == 1):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos8 = True
                                redScoreCounter[7] = True
                            else:
                                redPos8 = False
                                redScoreCounter[7] = False
                        if (row + 6 == 8 and col == 2):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos9 = True
                                redScoreCounter[8] = True
                            else:
                                redPos9 = False
                                redScoreCounter[8] = False
                        if (row + 6 == 9 and col == 3):
                            if (testButton[0].cget("bg") == self.redColor):
                                redPos10 = True
                                redScoreCounter[9] = True
                            else:
                                redPos10 = False
                                redScoreCounter[9] = False
        if (greenPos1 == True and greenPos2 == True and greenPos3 == True and greenPos4 == True and greenPos5 == True and greenPos6 == True
            and greenPos7 == True and greenPos8 == True and greenPos9 == True and greenPos10 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Green! You won!!!!!")
            for TF in greenScoreCounter:
                if (TF == True):
                    self.greenScore += 1
            for TF in redScoreCounter:
                if (TF == True):
                    self.redScore += 1
            self.gameOver = True
            self.redScoreLabel.config(text = "Red Score: " + str(self.redScore))
            self.greenScoreLabel.config(text = "Green Score: " + str(self.greenScore))
            self.moveNumberLabel.config(text = "Move Count Final: " + str(self.moveTotal))
        elif (redPos1 == True and redPos2 == True and redPos3 == True and redPos4 == True and redPos5 == True
              and redPos6 == True and redPos7 == True and redPos8 == True and redPos9 == True and redPos10 == True):
            self.turnLabel.config(text = "CONGRATULATIONS Red! You won!!!!!")
            for TF in greenScoreCounter:
                if (TF == True):
                    self.greenScore += 1
            for TF in redScoreCounter:
                if (TF == True):
                    self.redScore += 1
            self.gameOver = True
            self.redScoreLabel.config(text = "Red Score: " + str(self.redScore))
            self.greenScoreLabel.config(text = "Green Score: " + str(self.greenScore))
            self.moveNumberLabel.config(text = "Move Count Final: " + str(self.moveTotal))
            self.moveToLabel.config(text = "Game Over")
            
    # Timer/Countdown ===================================================================================
    def setTimerCount(self, timeIn):
        self.timerCount = timeIn

    def countdown(self, t):
        startTime = math.floor(time.time())
        endTime = startTime + t
        while(startTime != endTime):
            startTime = math.floor(time.time())
            print(time.time())
        print("Time up!")

    # Basic "AI" ========================================================================================
    def setHuman(self, colorIn):
        if (colorIn == "green"):
            self.isHuman = True
            self.greenPlayer.config(text = "Human")
            self.redPlayer.config(text = "Computer")                       
        elif (colorIn == "red"):
            self.isHuman = False
            self.greenPlayer.config(text = "Computer")
            self.redPlayer.config(text = "Human")    
            
    def computeMove(self, greenMapIn, redMapIn):
        listOfMoves = []
        secondaryList = []
        listOfAllMoves = []
        finalMove = (((0, 0), 0, 0), ((0, 0), 0))
        currentHigh = -20
        currentPriority = 0
        if (self.currentTurn == True):
            for x,y in greenMapIn:
                currPos, highPos = self.findFarthestDistance(x, y)
                self.boardRefresh()
                currPosPos, currPosVal, currPosPriority = currPos
                highPosPos, highPosVal = highPos
                valDiff = highPosVal - currPosVal
                if (len(listOfMoves) == 0):
                    listOfMoves.append((currPos, highPos))
                    currentHigh = valDiff
                else:
                    if (valDiff > currentHigh):
                        listOfMoves = []
                        currentHigh = valDiff
                    if (valDiff == currentHigh):
                        listOfMoves.append((currPos, highPos))
                #print(currPos, highPos, valDiff)
                listOfAllMoves.append((currPos, highPos, valDiff))
            #print(listOfMoves)
        else:
            for x,y in redMapIn:
                currPos, highPos = self.findFarthestDistance(x, y)
                self.boardRefresh()
                currPosPos, currPosVal, currPosPriority = currPos
                highPosPos, highPosVal = highPos
                valDiff = highPosVal - currPosVal
                if (len(listOfMoves) == 0):
                    listOfMoves.append((currPos, highPos))
                    currentHigh = valDiff
                else:
                    if (valDiff > currentHigh):
                        listOfMoves = []
                        currentHigh = valDiff
                    if (valDiff == currentHigh):
                        listOfMoves.append((currPos, highPos))
                #print(currPos, highPos, valDiff)
                listOfAllMoves.append((currPos, highPos, valDiff))
            #print(listOfMoves)

        if (len(listOfMoves) == 1):
            finalMove = listOfMoves[0]
        else:
            currentPriority = 0
            for first, second in listOfMoves:
                first1, first2, first3 = first
                if (len(secondaryList) == 0):
                    secondaryList.append((first, second))
                    currentPriority = first3
                else:
                    if (first3 > currentPriority):
                        secondaryList = []
                        currentPriority = first3
                    if (first3 == currentPriority):
                        secondaryList.append((first, second))
            #print(secondaryList)
            if (len(secondaryList) == 1):
                finalMove = secondaryList[0]
            else:
                tieBreaker = random.randint(0, len(secondaryList) - 1)
                finalMove = secondaryList[tieBreaker]
        #self.calculateMapGoodness(greenMapIn, redMapIn) #For testing, eventually called in findBestMove()
        self.findGridName(finalMove) #For testing, eventually called in findBestMove()
        return(listOfAllMoves)
            
    def findGridNameCont(self, row, col):
        #print(self.alpha16[col] + str(row))
        return (self.alpha16[col] + str(row))

    def findGridName(self, tupleIn):
        first, second = tupleIn
        first1, first2, first3 = first
        second1, second2 = second
        first1x, first1y = first1
        second1x, second1y = second1
        fromStr = self.findGridNameCont(first1x, first1y)
        toStr = self.findGridNameCont(second1x, second1y)
        ####self.checkWinCondition8()
        if (self.gameOver == True):
            self.moveToLabel.config(text = "Game Over")
        else:
            if (self.currentTurn == True):
                self.moveToLabel.config(text = "Green should move " + fromStr + " to " + toStr)
                #print("Green should move " + fromStr + " to " + toStr)
            else:
                self.moveToLabel.config(text = "Red should move " + fromStr + " to " + toStr)
                #print("Red should move " + fromStr + " to " + toStr)
    
    def findFarthestDistance(self, row, col):
        if (len(self.potentialMoves) == 0):
            self.setCurrentToGridCoordinates(row - 1, col)
            self.setCurrentGridCoordinates(row - 1, col)
            self.checkAroundPos(row, col)            
        currentPosValue = ((0, 0), 0, 0)
        potentialMove = ((0, 0), 0)
        testInList = ((0, 0), 0)
        currentHighMoves = []
        tieBreaker = 0
        currentPosString = self.findGridNameCont(row, col)
        goToPosString = ""
        finalHighMove = ((0, 0), 0)
        #print("------------")
        if (self.currentTurn == True):
            for gPoint in self.greenGoodness:
                if ((row-1, col) in self.greenGoodness[gPoint] or (row-1, col) == self.greenGoodness[gPoint]):
                    for rPoint in self.redGoodness:
                        if ((row-1, col) in self.redGoodness[rPoint] or (row-1, col) == self.redGoodness[rPoint]):
                            currentPosValue = ((row, col), gPoint, rPoint)
                            #print("CurrPosVal: " + str(currentPosValue))
            for point in self.greenGoodness:
                for x,y in self.potentialMoves:
                    if ((x-1,y) in self.greenGoodness[point] or (x-1, y) == self.greenGoodness[point]):
                        potentialMove = ((x, y), point)
                        #print("POTMOVE: ", end="")
                        #print(potentialMove)
                        if (len(currentHighMoves) == 0):
                            currentHighMoves.append(potentialMove)
                            testInList = potentialMove
                        else:
                            pos,val = testInList
                            if (point == val):
                                currentHighMoves.append(potentialMove)
        else:
            for gPoint in self.redGoodness:
                if ((row-1, col) in self.redGoodness[gPoint] or (row-1, col) == self.redGoodness[gPoint]):
                    for rPoint in self.greenGoodness:
                        if ((row-1, col) in self.greenGoodness[rPoint] or (row-1, col) == self.greenGoodness[rPoint]):
                            currentPosValue = ((row, col), gPoint, rPoint)
                            #print("CurrPosVal: " + str(currentPosValue))
            for point in self.redGoodness:
                for x,y in self.potentialMoves:
                    if ((x-1,y) in self.redGoodness[point] or (x-1, y) == self.redGoodness[point]):
                        potentialMove = ((x, y), point)
                        #print("POTMOVE: ", end="")
                        #print(potentialMove)
                        if (len(currentHighMoves) == 0):
                            currentHighMoves.append(potentialMove)
                            testInList = potentialMove
                        else:
                            pos,val = testInList
                            if (point == val):
                                currentHighMoves.append(potentialMove)        
        try:
            if (len(currentHighMoves) > 1):
                tieBreaker = random.randint(0, len(currentHighMoves) - 1)
                finalHighMove = currentHighMoves[tieBreaker]
            else:
                finalHighMove = currentHighMoves[0]
        except (IndexError):
            pass
        goPos,goVal = finalHighMove
        goX,goY = goPos
        goToPosString = self.findGridNameCont(goX, goY)
        #print("Move " + currentPosString + " to " + goToPosString, end=" ")
        #print("ListOfMoves: " + str(currentHighMoves))
        self.potentialMoves = []
        return (currentPosValue, finalHighMove)

    
    def calculateMapGoodness(self, greenCurrentMap, redCurrentMap):
        greenMap = greenCurrentMap
        redMap = redCurrentMap
        greenMapCount = 0
        redMapCount = 0
        for greenPosX,greenPosY in greenMap:
            for key in self.greenGoodness:
                if ((greenPosX-1, greenPosY) in self.greenGoodness[key]
                    or (greenPosX-1, greenPosY) == self.greenGoodness[key]):
                    greenMapCount += key
                else:
                    pass
        for redPosX,redPosY in redMap:
            for key in self.greenGoodness:
                if ((redPosX-1, redPosY) in self.redGoodness[key]
                    or (redPosX-1, redPosY) == self.redGoodness[key]):
                    redMapCount += key
                else:
                    pass
        #print("Green Map Count: ", end="")
        #print(greenMapCount)
        #print("Red Map Count: ", end="")
        #print(redMapCount)
        return(greenMapCount, redMapCount)

    def findBestMove(self):
        currentRedMap = self.redPiecesCurrentPosition
        currentGreenMap = self.greenPiecesCurrentPosition
        listOfMoves = self.computeMove(currentGreenMap, currentRedMap)
        mapStrength = self.calculateMapGoodness(currentGreenMap, currentRedMap)
        modRedMap = currentRedMap
        modGreenMap = currentGreenMap
        #for item in listOfMoves:
        #    print(item)
        
    

newGame = HalmaBoard()
newGame.createBoard(8)
newGame.setHuman("red")
newGame.setTimerCount(5)
newGame.nextTurn()
newGame.startMainLoop()


        
