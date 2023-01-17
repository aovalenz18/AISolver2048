from createBoard import createBoard
import numpy as np 
from board import Board

board = Board()
block1 = board.createBlock()
block2 = board.createBlock()

createBoard(board)

done = board.getGameStatus()

while not done:
    direction = input("Select direction: up, down, left, right: ")
    board.executeAction(direction)
    done = board.getGameStatus()
 
    if done:
        break

    block = board.createBlock()
    board.insertBlocks([block])

    createBoard(board)

