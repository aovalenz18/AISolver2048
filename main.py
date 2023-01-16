from createBoard import createBoard
import numpy as np 
from board import Board

board = Board()
block1 = board.createBlock()
block2 = board.createBlock()
board.insertBlocks([block1,block2])

createBoard(board)

done = board.getGameStatus()

while not done:
    direction = input("Select direction: up, down, left, right: ")
    board.executeAction(direction)
    createBoard(board)

    done = board.getGameStatus()

