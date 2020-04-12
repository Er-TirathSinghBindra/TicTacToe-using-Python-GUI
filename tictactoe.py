'''
Author : Tirath Singh Bindra

Description:

This code is to create a two player TicTacToe game using Python GUI. It uses Tkinter library for creating the graphical user interface of game.
For backend an algorithm based on matrix multiplications is used which decide on the basis of scores whether a person has won or not.

License: This code is licensed under GNU General Public License v3.0

It gives following permissions to the user for this code:
Permissions to use:
 Commercial use
 Modification
 Distribution
 Patent use
 Private use

Any commercial use, modification, distribution, patent use and private use of this code can be done only if following coditions are met:
 License and copyright notice : Copyright and license notices must be preserved. Each modification of this code must always carry this same doc report.
 State changes : All the changes made to code must be documented and shared along with source code.
 Disclose source : The source code of modifications should be made publicaly avaialable.
 Same license : Any modifications of code must carry the same license.

For detailed information kindly refer to LICENSE file.
'''

# Python GUI Library
import tkinter as tk
# To create a Tkinter variable
from tkinter import StringVar
# For random selection of starting player
import random
# For matrix manipulations. Used in main algorithm.
import numpy as np

# Global Variables
players = ['X','O']


valueX = +1
valueO = -1 

class Board:
    '''It contains all the methods to create board and backend methods.'''
    # Initializing Class Board and Storing Class Level Variables
    def __init__(self, width=400, height=400): 
        # Creating root Window
        self.root = tk.Tk() 
        self.root.resizable(width=False, height=False)

        # Storing Width and Height of Canvas to draw on: 
        # Default Width = 400 Height=400
        self.width  = width 
        self.height = height

        # Label Text Variable
        self.infoText = StringVar()

        # Initialize all the game variables
        self.gameVarInit()
        # Creating canvas
        self.createCanvas()
        # Creating board on canvas
        self.createBoard()

    # Initializing Game Variables
    def gameVarInit(self):
        # Board Variables
        self.boardStatus = np.array([
            ['','',''],
            ['','',''],
            ['','','']
        ])
        # Maintaining scores of each position
        self.boardScore = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ])

        # Choosing start player randomly
        self.currPlayer = random.choice(players)
        # Storing player index from list
        self.playerIndex = players.index(self.currPlayer)

        boardSize = len(self.boardStatus)
        # Storing remaining moves of the game
        self.remainingMoves =pow(boardSize,2)
        # Variables to check game over and game won conditions
        self.gameWon = False
        self.gameOver = False

        # For main algorithm matrix multiplication
        self.mulMat = np.array([1]*boardSize).reshape(boardSize,1)

    # Function to create and initialize a canvas with width and height
    def createCanvas(self):
        self.mainCanvas = tk.Canvas(self.root, width=self.width, height=self.height)
        # Adding button press event to main canvas
        self.mainCanvas.bind("<ButtonPress-1>", self.locToIndex)
        # To pack the canvas on root window
        self.mainCanvas.pack()
        self.infoLabel = tk.Label(self.root,bg='#87ceeb', textvariable = self.infoText)
        self.infoLabel.pack(fill=tk.X) #tk.X makes the label as wide as the parent window 

    # Function to create board
    def createBoard(self):
        # Line thickness for boundary lines
        linewidth = 5
       
        # Creating Vertical Lines
        self.mainCanvas.create_line(self.width/3,0,self.width/3,self.height, width=linewidth)
        self.mainCanvas.create_line(2*self.width/3,0,2*self.width/3,self.height, width=linewidth)

        # Creating Horizontal Lines
        self.mainCanvas.create_line(0,self.height/3,self.width,self.height/3, width=linewidth)
        self.mainCanvas.create_line(0,2*self.height/3,self.width,2*self.height/3, width=linewidth)

        # Displaying Current Player on Screen
        self.infoText.set(f'Player {self.currPlayer} start')
   
    # Function to Update Board Status. For debugging purposes only.
    def updateBoard(self):
        for i in range(3):
            for j in range(3):
                data=self.boardStatus[i][j]
                #print(f'Data at {i},{j} is {data}')
                self.drawCharacter(data, i , j)

    # To draw character based on player moved
    def drawCharacter(self, data, row, col):
        heightOffset = 0.1 * self.height
        widthOffset = 0.1 * self.width
        charWidth = 3

        # Determining x,y coordinates for each position to draw a character in its
        x1 = col * self.width/3 + widthOffset
        y1 = row * self.height/3 + heightOffset
 
        x2 = (col + 1) * self.width/3 - widthOffset
        y2 = (row + 1) * self.height/3 - heightOffset

        # Drawing O and X on canvas
        if(data == 'O'):
            self.mainCanvas.create_oval(x1,y1,x2,y2, width=charWidth)
        elif(data == 'X'):
            self.mainCanvas.create_line(x1,y1,x2,y2, width=charWidth)
            self.mainCanvas.create_line(x1,y2,x2,y1, width=charWidth)

    # Changing board status with new player move
    def updateBoardStatus(self, row, col):
        # Updating the board position with player who has occupied that place
        self.boardStatus[row][col]=self.currPlayer
        # Updating board score for a position corresponding to the player who has occupied that place
        if self.currPlayer == 'X' : self.boardScore[row][col] += valueX
        else : self.boardScore[row][col] += valueO

    # Converting cursor click location to array index
    def locToIndex(self, event):
        row = 0
        col = 0 
        currWidth, currHeight = event.x, event.y
        
        if(currHeight < self.height/3):
            row = 0
        elif((currHeight > self.height/3) and (currHeight < (2*self.height/3))):
            row = 1
        elif(currHeight > (2*self.height/3)):
            row = 2

        if(currWidth < self.width/3):
            col = 0
        elif((currWidth > self.width/3) and (currWidth < (2*self.width/3))):
            col = 1
        elif(currWidth > (2*self.width/3)):
            col = 2
        
        # Checking if location is empty or occupied
        self.isAvailable(row, col)

        #print("To ",row, col)

    # Checkin if location is available
    def isAvailable(self, row, col):
        if(self.gameWon == False and self.gameOver == False):
            if(self.boardStatus[row][col]==''):
                self.remainingMoves -= 1
                self.drawCharacter(self.currPlayer, row, col)
                self.updateBoardStatus(row, col)
                self.gameWon = self.hasWon(row,col)
                if self.gameWon:
                    self.infoText.set(f'{self.currPlayer} has WON!!!')
                    #print(f'{self.currPlayer} has WON!!!')
                    return

            else:
                self.infoText.set('Position already occupied')
                #print('Position already occupied')
                return

        else:
            self.infoText.set('Game Over!!! Click Here To Reset!!!')
            self.infoLabel.bind('<Button-1>',self.resetAll)
            #print('Game Already Over!!!')
            return
        
        if self.remainingMoves == 0:
            self.infoText.set('No moves left!!! Click Here To Reset!!!')
            self.infoLabel.bind('<Button-1>',self.resetAll)
            #print('No more moves left game over!!!')
            #print('!!!Reset to play!!!')
            self.gameOver = True
            return
        # Selecting next player
        self.nextPlayer()
        #print(boardStatus)

    # Iterating between the players
    def nextPlayer(self):
        self.playerIndex += 1

        if(self.playerIndex > (len(players)-1)): self.playerIndex = 0 

        self.currPlayer = players[self.playerIndex]
        self.infoText.set(f'Player {self.currPlayer}\'s turn')

    # Check if current player has won. Main algorithm using matrix multiplication to calculate if a person has won.
    def hasWon(self, row, col):
        sumRows = self.boardScore.dot(self.mulMat).T.tolist()
        sumCols = self.mulMat.T.dot(self.boardScore).tolist()
        sumDiag = np.trace(self.boardScore)
        sumAntiDiag = np.trace(np.flipud(self.boardScore))

        if ((3 in sumRows[0]) or (3 in sumCols[0]) or (3 == sumDiag) or (3 == sumAntiDiag)): return True
        elif ((-3 in sumRows[0]) or (-3 in sumCols[0]) or (-3 == sumDiag) or (-3 == sumAntiDiag)): return True 
        
        return False

    # To Reset The Game
    def resetAll(self,event):
        # Setting variables to initial values
        self.gameVarInit()
        # Clearing the canvas
        self.mainCanvas.delete('all')
        # Recreating board on same canvas
        self.createBoard()
        # Removing click from label
        self.infoLabel.unbind('<Button-1>')

# Initializing board with required canvas size
board = Board(width=500, height=500)
board.root.mainloop()