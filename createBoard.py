def createSquare(array):
    for i in range(4):
        print("  - ",end="")
    print()
    for i in range(4):
        if array[i] < 2:
            print("|   ",end="")
        else:
            print("| {} ".format(array[i]),end="")
    print("|",end="")
    
    print()
    for i in range(4):
        print("  - ",end="")

def createBoard(board):
    for i in range(4):
        createSquare(board[i])
        print()


