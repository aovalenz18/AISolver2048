import numpy as np 

board = np.zeros((4,4),dtype=int)

# board[0,0] = 2
# board[0,1] = 2
board[0,2] = 2
board[0,3] = 2

board[1,2] = 2
board[1,0] = 2

board[3,2] = 2
print(board)

for i in range(len(board)):
    for j in range(1,len(board)):
        value = board[i,j]
        copyIndex = j
        if value > 0: 
            done = False
            next = board[i,copyIndex-1]
            while not done:
                if next == 0:
                    board[i,copyIndex-1] = value
                    board[i, copyIndex] = 0
                    copyIndex -= 1
                    if copyIndex == 0:
                        done= True
                    else:
                        next = board[i,copyIndex-1]
                else:
                    done = True

print(board)