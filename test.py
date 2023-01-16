import numpy as np 

board = np.zeros((4,4),dtype=int)

board[1,2] = 2
# board[1,0] = 2
print(board)

for i in range(len(board)):
    for j in range( len(board[i]) - 2, -1 ,-1  ):
        nextValue = board[i, j+ 1]
        print(nextValue)
        while nextValue == 0: 
            board[i,nextValue] = board[i,j]
            board[i,j] = 0
            nextValue = board[i, j]

        # j = 3
        # while j > 0:
        #     lastElement = board[i,j]
        #     prev = j - 1
        #     # this is the logic of shifting a number to the left 
        #     value = board[i,prev] # last value 
        #     if value > 0 and lastElement == 0:
        #         board[i,prev + 1] = value
        #         board[i,prev] = 0
        #     j -= 1

print()
print(board)