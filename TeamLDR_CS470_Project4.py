from tkinter import *
import time

class HalmaBoard():

    def __init__(self):
        self.boardSize = 0
        self.currentTurn = True
        self.betweenMove = False
        self.mainWindow = Tk()
        self.boardFrame = Frame(self.mainWindow)
        self.titleLabel = Label(self.boardFrame, text = "Halma Game")
        self.buttonList = []
        self.turnLabel = Label(self.boardFrame, text = "Green Turn: Starting Move")
        self.redScoreLabel = Label(self.boardFrame, text = "")
        self.greenScoreLabel = Label(self.boardFrame, text = "")
        self.moveNumberLabel = Label(self.boardFrame, text = "Move Count: 0")
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
        self.greenPiecesCurrentPosition = []
        self.redPiecesCurrentPosition = []
        self.redColor = "red"
        self.redHighlightColor = "maroon"
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
            self.turnLabel.config(text = "Invalid Board: Reset Game With board size [8]!")
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
        
    def findMousePosOVERRIDE(self, event):
        if (self.gameOver == False):
            print("OverRide")
        else:
            pass

    def createBoard(self, size):
        self.boardSize = size
        Grid.rowconfigure(self.mainWindow, 0, weight = 1)
        Grid.columnconfigure(self.mainWindow, 0, weight = 1)
        self.boardFrame.grid(row = 0, column = 0, stick = N + S + E + W)
        self.titleLabel.grid(row = 0, column = 0, columnspan = self.boardSize, pady = 0)
        self.turnLabel.grid(row = self.boardSize + 3, column = 0, columnspan = self.boardSize, pady = 0)
        if (self.boardSize == 8):
            self.greenScoreLabel.grid(row = self.boardSize + 2, column = 0, columnspan = 2, pady = 0)
            self.moveNumberLabel.grid(row = self.boardSize + 2, column = 2, columnspan = 4, pady = 0)
            self.redScoreLabel.grid(row = self.boardSize + 2, column = 6, columnspan = 2, pady = 0)
        elif (self.boardSize == 10):
            self.greenScoreLabel.grid(row = self.boardSize + 2, column = 0, columnspan = 3, pady = 0)
            self.moveNumberLabel.grid(row = self.boardSize + 2, column = 3, columnspan = 4, pady = 0)
            self.redScoreLabel.grid(row = self.boardSize + 2, column = 7, columnspan = 3, pady = 0)
        elif (self.boardSize == 16):
            self.greenScoreLabel.grid(row = self.boardSize + 2, column = 0, columnspan = 5, pady = 0)
            self.moveNumberLabel.grid(row = self.boardSize + 2, column = 5, columnspan = 6, pady = 0)
            self.redScoreLabel.grid(row = self.boardSize + 2, column = 11, columnspan = 5, pady = 0)
        for num in range(self.boardSize * self.boardSize):
            self.buttonList.append(Button(self.boardFrame))
        for num in range(self.boardSize):
            self.labelListLetters.append(Label(self.boardFrame, text = self.alpha16[num]))
            self.labelListNumbers.append(Label(self.boardFrame, text = str(num + 1)))
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
        self.mainWindow.wm_geometry("400x442") #942 -> 42 comes from the height of the titleLabel+turnLabel.
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
                
        else: # Second Click
            if (self.currentTurn == True):
                if (buttonPos[0].cget("bg") == self.moveToHighlightColor): # Moves
                    self.moveTo(row, col)
                    self.nextTurn()
                    self.boardRefresh()
                    self.moveTotal += 1
                    self.moveNumberLabel.config(text = "Move Count: " + str(self.moveTotal))  
                    self.checkWinCond(self.boardSize)
                elif (buttonPos[0].cget("bg") == self.greenColor): # Resets
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()
            else:
                if (buttonPos[0].cget("bg") == self.moveToHighlightColor): # Moves
                    self.moveTo(row, col)
                    self.nextTurn()
                    self.boardRefresh()
                    self.moveTotal += 1
                    self.moveNumberLabel.config(text = "Move Count: " + str(self.moveTotal))  
                    self.checkWinCond(self.boardSize)
                elif (buttonPos[0].cget("bg") == self.redColor): # Resets
                    self.boardRefresh()
                    self.setBetweenMove()
                    self.onClickHighlight(row, col)
                    self.checkAroundPos(row, col)
                    self.setBetweenMove()                

    def onClickHighlight(self, row, col):
        buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
        if (buttonPos[0].cget("bg") == self.redColor):
            buttonPos[0].config(bg = self.redHighlightColor)
        elif (buttonPos[0].cget("bg") == self.greenColor):
            buttonPos[0].config(bg = self.greenHighlightColor)

    def checkAroundPos(self, row, col):
        print("CurPos: " + str(row) + str(col))
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (row == r and c == col):
                    pass
                else:
                    if (self.currentTurn == True): #GREENTURN
                        if ((row, col) in self.greenCorner):
                            print("In GreenCorner")
                            self.checkMove(r, c, True, False)
                            self.checkJump(r, c, True, False)
                        elif ((row, col) in self.redCorner):
                            print("InGoalState")
                            self.checkMove(r, c, False, True)
                            self.checkJump(r, c, False, True)
                        else:
                            print("NOT In GreenCorner")
                            self.checkMove(r, c, False, False)
                            self.checkJump(r, c, False, False)
                    else: #REDTURN
                        if ((row, col) in self.redCorner):
                            print("In RedCorner")
                            self.checkMove(r, c, True, False)
                            self.checkJump(r, c, True, False)
                        elif ((row, col) in self.greenCorner):
                            print("InGoalState")
                            self.checkMove(r, c, False, True)
                            self.checkJump(r, c, False, True)
                        else:
                            print("NOT In RedCorner")
                            self.checkMove(r, c, False, False)
                            self.checkJump(r, c, False, False)
        print("++++++++++++")
        """
        #for x,y in self.potentialMoves:
        #    print("PotentialMove: ", end="")
        #    print(x, y)
        #    self.setCurrentToGridCoordinates(x + 1, y)
        #    self.checkJump(x + 1, y)
        #    print("Checked: " + str(x) + " " + str(y))
        ####print(self.potentialMoves)
        """
                    
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
        if (self.currentTurn == True):
            self.currentTurn = False
        else:
            self.currentTurn = True

    def jumpAround(self, tox, toy, ovx, ovy, pox, poy, cux, cuy):
        try:
            jumpToPos = self.boardFrame.grid_slaves(row = self.toGridX + tox, column = self.toGridY + toy)
            jumpOverPos = self.boardFrame.grid_slaves(row = self.toGridX + ovx, column = self.toGridY + ovy)
            #jumpToPos[0].config(bg = "purple") #TESTING
            #jumpOverPos[0].config(bg = "red") #TESTING






            
            if ((jumpToPos[0].cget("bg") == self.boardTileLight or jumpToPos[0].cget("bg") == self.boardTileDark
                 or jumpToPos[0].cget("bg") == self.greenCornerColor or jumpToPos[0].cget("bg") == self.redCornerColor)
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





            
        except (IndexError, TclError):
            pass
                          
    def checkJump(self, row, col, inOwnGoal, inOtherGoal):
        try:
            buttonPos = self.boardFrame.grid_slaves(row = row, column = col)
            if (buttonPos[0].cget("bg") == self.greenColor or buttonPos[0].cget("bg") == self.redColor or buttonPos[0].cget("bg") == self.moveToHighlightColor):
                try:
                    if (self.currentTurn == True): # GREEN PLAYER
                        self.jumpAround(1, 2, 1, 1, 1, 2, 0, 2)
                        self.jumpAround(-1, 0, 0, 0, -1, 0, -2, 0)
                        self.jumpAround(-1, 2, 0, 1, -1, 2, -2, 2)
                        self.jumpAround(-1, -2, 0, -1, -1, -2, -2, -2)
                        self.jumpAround(3, 0, 2, 0, 3, 0, 2, 0)
                        self.jumpAround(3, -2, 2, -1, 3, -2, 2, -2)
                        self.jumpAround(1, -2, 1, -1, 1, -2, 0, -2)
                        self.jumpAround(3, 2, 2, 1, 3, 2, 2, 2)
                    else: # RED PLAYER
                        self.jumpAround(3, 0, 2, 0, 3, 0, 2, 0)
                        self.jumpAround(1, -2, 1, -1, 1, -2, 0, -2)
                        self.jumpAround(3, -2, 2, -1, 3, -2, 2, -2)
                        self.jumpAround(3, 2, 2, 1, 3, 2, 2, 2)
                        self.jumpAround(-1, 0, 0, 0, -1, 0, -2, 0)
                        self.jumpAround(-1, 2, 0, 1, -1, 2, -2, 2)
                        self.jumpAround(1, 2, 1, 1, 1, 2, 0, 2)
                        self.jumpAround(-1, -2, 0, -1, -1, -2, -2, -2) 
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
            
    # Timer/Countdown ===================================================================================
    def countdown(self, t):
        while t >= 0:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            if (t == 0):
                print(timeformat, end="")
                print(" Time Up!")
                break
            else:
                print(timeformat)
            time.sleep(1)
            t -= 1

    

newGame = HalmaBoard()
newGame.createBoard(8)
newGame.countdown(0)
newGame.startMainLoop()

        
