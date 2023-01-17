import numpy as np 
from block import Block
import random

class Board(object):
    def __init__(self, *args):
        super(Board, self).__init__()
        self.board = np.zeros((4,4),dtype=int)
        self.done = False
    
    def __getitem__(self,key):
        return self.board[key]
    
    def createBlock(self):
        index = self.generateBlockIndex()
        value = np.random.choice([2,4],p=[0.99,0.01])
        self.board[index[0],index[1]] = value
        return Block(index,value)
    
    def generateBlockIndex(self):
        indices = np.where(self.board == 0)
        index = random.randint(0,len(indices[0])-1)
        x = indices[0][index]
        y = indices[1][index]
        return [x,y]

    def insertBlocks(self,blocks):
        for block in blocks:
            index = block.getIndex()
            self.board[index[0],index[1]] = block.getValue()

    
    def getGameStatus(self):
        return self.done

    def executeAction(self,value):
        if value == "left":
            self.shiftLeft()
            self.mergeLeft()
            self.shiftLeft()
        elif value == "right":
            self.shiftRight()
            self.mergeRight()
            self.shiftRight()
        elif value == "up":
            self.shiftUp()
            self.mergeUp()
            self.shiftUp()
        elif value == "down":
            self.shiftDown()
            self.mergeDown()
            self.shiftDown()
        elif value == "quit":
            self.done = True
    
    def shiftRight(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)-2, -1, -1 ):
                value = self.board[i,j]
                copyIndex = j
                if value > 0: 
                    done = False
                    next = self.board[i,copyIndex+1]
                    while not done:
                        if next == 0:
                            self.board[i,copyIndex+1] = value
                            self.board[i, copyIndex] = 0
                            copyIndex += 1
                            if copyIndex == 3:
                                done= True
                            else:
                                next = self.board[i,copyIndex+1]
                        else:
                            done = True
        return
    
    def shiftUp(self):
        for i in range(len(self.board)):
            for j in range(1,len(self.board)):
                value = self.board[j,i]
                copyIndex = j
                if value > 0: 
                    done = False
                    next = self.board[copyIndex-1,i]
                    while not done:
                        if next == 0:
                            self.board[copyIndex-1,i] = value
                            self.board[copyIndex,i] = 0
                            copyIndex -= 1
                            if copyIndex == 0:
                                done= True
                            else:
                                next = self.board[copyIndex-1,i]
                        else:
                            done = True

        return
        
    def shiftDown(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)-2, -1, -1):
                value = self.board[j,i]
                copyIndex = j
                if value > 0: 
                    done = False
                    next = self.board[copyIndex+1,i]
                    while not done:
                        if next == 0:
                            self.board[copyIndex+1,i] = value
                            self.board[copyIndex,i] = 0
                            copyIndex += 1
                            if copyIndex == 3:
                                done= True
                            else:
                                next = self.board[copyIndex+1,i]
                        else:
                            done = True
        return
    
    def shiftLeft(self):
        for i in range(len(self.board)):
            for j in range(1,len(self.board)):
                value = self.board[i,j]
                copyIndex = j
                if value > 0: 
                    done = False
                    next = self.board[i,copyIndex-1]
                    while not done:
                        if next == 0:
                            self.board[i,copyIndex-1] = value
                            self.board[i, copyIndex] = 0
                            copyIndex -= 1
                            if copyIndex == 0:
                                done= True
                            else:
                                next = self.board[i,copyIndex-1]
                        else:
                            done = True

        return
    
    def mergeLeft(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)-1):
                current = self.board[i,j]
                next = self.board[i,j+1]
                if next == current: 
                    newVal = next + current
                    self.board[i,j] = newVal
                    self.board[i,j+1] = 0
    
    def mergeRight(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)-2, -1, -1 ):
                current = self.board[i,j]
                next = self.board[i,j+1]
                if next == current: 
                    newVal = next + current
                    self.board[i,j] = newVal
                    self.board[i,j+1] = 0

    def mergeUp(self):
        for i in range(len(self.board)):
            for j in range(1,len(self.board)):
                current = self.board[j,i]
                next = self.board[j-1,i]
                if next == current: 
                    newVal = next + current
                    self.board[j,i] = newVal
                    self.board[j-1,i] = 0
    
    def mergeDown(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)-2, -1, -1):
                current = self.board[j,i]
                next = self.board[j+1,i]
                if next == current: 
                    newVal = next + current
                    self.board[j,i] = newVal
                    self.board[j+1,i] = 0