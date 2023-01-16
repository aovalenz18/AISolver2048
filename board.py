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
        index = self.generateBlockIndex();
        value = np.random.choice([2,4],p=[0.9,0.1])
        return Block(index,value)
    
    def generateBlockIndex(self):
        return [random.randint(0,3), random.randint(0,3)]

    def insertBlocks(self,blocks):
        for block in blocks:
            index = block.getIndex()
            self.board[index[0],index[1]] = block.getValue()
    
    def getGameStatus(self):
        return self.done

    def executeAction(self,value):
        if value == "left":
            self.shiftLeft()
        elif value == "right":
            self.shiftRight()
        elif value == "up":
            self.shiftUp()
        elif value == "down":
            self.shiftDown()
        elif value == "quit":
            self.done = True
    
    def shiftRight(self):
        return
    def shiftUp(self):
        return
    def shiftDown(self):
        return
    
    def shiftLeft(self):
        for i in range(len(self.board)):
            lastElement = self.board[i,3]
            j = 2
            # this is the logic of shifting a number to the left 
            value = self.board[i,j] #last value 
            if value > 0 and lastElement == 0:
                self.board[i,j + 1] = value
                self.board[i,j] = 0

        return