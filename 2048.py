import random
import sys

BLANK = ""
def main():
    input("Press enter to begin...")
    
    gameBoard = getNewBoard()
    
    while (True):
        drawBoard(gameBoard)
        print(f"Score: {getScore(gameBoard)}")
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)
        
        if (isFull(gameBoard)):
            drawBoard(gameBoard)
            print("Game over!")
            sys.exit()
            
# get new blank board
def getNewBoard():
    newBoard = {}
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK
    
    startingTwosPlaced = 0
    while (startingTwosPlaced < 2):
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if (newBoard[randomSpace] == BLANK):
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1
    
    return newBoard
    
# draw the board with numbers
def drawBoard(board):
    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)
    
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))

# get the sum of all numbers
def getScore(board):
    score = 0
    
    for x in range(4):
        for y in range(4):
            if (board[(x, y)] != BLANK):
                score += board[(x, y)]
                
    return score

# combine after move
def combineTilesInColumn(column):
    combinedTiles = []
    for i in range(4):
        if (column[i] != BLANK):
            combinedTiles.append(column[i])
            
    while (len(combinedTiles) < 4):
        combinedTiles.append(BLANK)
        
    for i in range(3):
        if (combinedTiles[i] == combinedTiles[i + 1]):
            combinedTiles[i] *= 2
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK
            
    return combinedTiles

# define the place after move
def makeMove(board, move):
    if (move == "W"):
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif (move == "A"):
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif (move == "S"):
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif (move == "D"):
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]
        
    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]
        
        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]
        
        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)
        
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]
        
    return boardAfterMove

# ask player to move
def askForPlayerMove():
    print("Enter move: (WASD or Q to quit)")
    while (True):
        move = input("> ").upper()
        if (move == "Q"):
            print("Thanks for playing!")
            sys.exit()
        
        if (move in ("W", "A", "S", "D")):
            return move
        else:
            print("Enter on of \"W\", \"A\", \"S\", \"D\", or \"Q\".")
            
# add a "2" in board
def addTwoToBoard(board):
    while (True):
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if (board[randomSpace] == BLANK):
            board[randomSpace] = 2
        return

# check whether the board is full
def isFull(board):
    for x in range(4):
        for y in range(4):
            if (board[(x, y)] == BLANK):
                return False
    
    return True
    
if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()