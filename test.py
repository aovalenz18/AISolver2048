import numpy as np 

board = np.zeros((4,4),dtype=int)

# board[0,0] = 2
# board[0,1] = 2
board[0,2] = 2
board[0,3] = 2

board[1,2] = 2
board[1,0] = 2
board[3,1] = 2

board[3,2] = 2
print(board)

for i in range(len(board)):
    for j in range(len(board)-2, -1, -1):
        value = board[j,i]
        copyIndex = j
        if value > 0: 
            done = False
            next = board[copyIndex+1,i]
            while not done:
                if next == 0:
                    board[copyIndex+1,i] = value
                    board[copyIndex,i] = 0
                    copyIndex += 1
                    if copyIndex == 3:
                        done= True
                    else:
                        next = board[copyIndex+1,i]
                else:
                    done = True

print(board)

##logic for shift up 

