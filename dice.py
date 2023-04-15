import random
import time

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 1

D1 = (["+-------+",
       "|       |",
       "|   0   |",
       "|       |",
       "+-------+"], 1)
D2a = (["+-------+",
        "| 0     |",
        "|       |",
        "|     0 |",
        "+-------+"], 2)
D2b = (["+-------+",
        "|     0 |",
        "|       |",
        "| 0     |",
        "+-------+"], 2)
D3a = (["+-------+",
        "| 0     |",
        "|   0   |",
        "|     0 |",
        "+-------+"], 3)
D3b = (["+-------+",
        "|     0 |",
        "|   0   |",
        "| 0     |",
        "+-------+"], 3)
D4 = (["+-------+",
       "| 0   0 |",
       "|       |",
       "| 0   0 |",
       "+-------+"], 4)
D5 = (["+-------+",
       "| 0   0 |",
       "|   0   |",
       "| 0   0 |",
       "+-------+"], 5)
D6a = (["+-------+",
        "| 0   0 |",
        "| 0   0 |",
        "| 0   0 |",
        "+-------+"], 6)
D6b = (["+-------+",
        "| 0 0 0 |",
        "|       |",
        "| 0 0 0 |",
        "+-------+"], 6)

ALL_DICE = (D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b)

input("Print enter to begin...")
correctAnswer = incorrectAnswer = 0
startTime = time.time()
# end after "QUIZ_DURATION" seconds
while (time.time() < startTime + QUIZ_DURATION):
    sumAnswer = 0
    diceFaces = []
    # create random number of dice
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        diceFaces.append(die[0])
        sumAnswer += die[1]
        
    topLeftDiceCorners = []
    for i in range(len(diceFaces)):
        while (True):
            # locate the dice's places
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
            
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT
            
            # check overlap
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                for cornerX, cornerY in ((topLeftX, topLeftY), (topRightX, topRightY), (bottomLeftX, bottomLeftY), (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom):
                        overlaps = True
                        
            if (not overlaps):
                topLeftDiceCorners.append((left, top))
                break
    
    # locate the dice
    canvas = {}
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]
                
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), " "), end = "")
        print("")
        
    # check the input whether correct
    response = input("Enter the sum: ").strip()
    if (response.isdecimal() and int(response) == sumAnswer):
        correctAnswer += 1
    else:
        print(f"Incorrect, the answer is {sumAnswer}.")
        time.sleep(2)
        incorrectAnswer += 1
        
# display result
score = correctAnswer * REWARD - incorrectAnswer * PENALTY
print(f"Correct: {correctAnswer}")
print(f"Incorrect: {incorrectAnswer}")
print(f"Score: {score}")