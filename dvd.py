import sys, random, time, bext

WIDTH, HEIGHT = bext.size()

WIDTH -= 1

NUMBER_OF_LOGOS, PAUSE_AMOUNT = 5, 0.2
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT = "ur", "ul", "dr", "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR, X, Y, DIR = "color", "x", "y", "direction"

def main():
    bext.clear()
    
    # add logo objects
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS), X: random.randint(1, WIDTH - 4), Y: random.randint(1, HEIGHT - 4), DIR: random.choice(DIRECTIONS)})
        
        # make the x coordinate is even so that it can hit the corner
        if (logos[-1][X] % 2 == 1):
            logos[-1][X] -= 1
    
    while (True):
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            originalDirection = logo[DIR]
            
            # check whether touch the corner
            if (logo[X] == 0 and logo[Y] == 0):
                logo[DIR] = DOWN_RIGHT
            elif (logo[X] == 0 and logo[Y] == HEIGHT - 1):
                logo[DIR] = UP_RIGHT
            elif (logo[X] == WIDTH - 3 and logo[Y] == 0):
                logo[DIR] = DOWN_LEFT
            elif (logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1):
                logo[DIR] = UP_LEFT
                
            # check whether touch left limit
            elif (logo[X] == 0 and logo[DIR] == UP_LEFT):
                logo[DIR] = UP_RIGHT
            elif (logo[X] == 0 and logo[DIR] == DOWN_LEFT):
                logo[DIR] = DOWN_RIGHT
            
            # check whether touch right limit
            elif (logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT):
                logo[DIR] = UP_LEFT
            elif (logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT):
                logo[DIR] = DOWN_LEFT
            
            # check whether touch upper limit
            elif (logo[Y] == 0 and logo[DIR] == UP_LEFT):
                logo[DIR] = DOWN_LEFT
            elif (logo[Y] == 0 and logo[DIR] == UP_RIGHT):
                logo[DIR] = DOWN_RIGHT
            
            # check whether touch lower limit
            elif (logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT):
                logo[DIR] = UP_LEFT
            elif (logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT):
                logo[DIR] = UP_RIGHT
            
            # change color when change direction
            if (logo[DIR] != originalDirection):
                logo[COLOR] = random.choice(COLORS)
                
            # move the object
            if (logo[DIR] == UP_RIGHT):
                logo[X] += 2
                logo[Y] -= 1
            elif (logo[DIR] == UP_LEFT):
                logo[X] -= 2
                logo[Y] -= 1
            elif (logo[DIR] == DOWN_RIGHT):
                logo[X] += 2
                logo[Y] += 1
            elif (logo[DIR] == DOWN_LEFT):
                logo[X] -= 2
                logo[Y] += 1
        
        # display the object
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end = "")
            
        bext.goto(0, 0)
        
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)
        
if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("\nBouncing DVD logo")
        sys.exit()