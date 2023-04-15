from tkinter import *
from random import *
import time
class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill = color)
        self.canvas.move(self.id, winW/2, winH/2)
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]
        shuffle(startPos)
        self.x = startPos[0]
        self.y = -2
        self.notTouchButtom = True
    def hitRacket(self, ballPos):
        racketPos = self.canvas.coords(self.racket.id)
        if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
            if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:
            self.x *= -1
        if ballPos[1] <= 0:
            self.y *= -1
        if ballPos[2] >= winW:
            self.x *= -1
        if ballPos[3] >= winH:
            self.y *= -1
        if self.hitRacket(ballPos) == True:
            self.y *= -1
        if ballPos[3] >= winH:
            self.notTouchButtom = False
class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 15, fill = color)
        self.canvas.move(self.id, 270, 400)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Right>", self.moveRight)
        self.canvas.bind_all("<KeyPress-Left>",self.moveLeft)
    def racketMove(self):
        self.canvas.move(self.id, self.x, 0)
        racketPos = self.canvas.coords(self.id)
        if racketPos[0] <= 0:
            self.x *= -1
        if racketPos[2] >= winW:
            self.x *= -1
    def moveLeft(self, event):
        self.x = -3
    def moveRight(self, event):
        self.x = 3

winW = 640
winH = 480
speed = 0.01

tk = Tk()
tk.title("Bouncing Ball")
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = winW, height = winH)
canvas.pack()

racket = Racket(canvas, "purple")
ball = Ball(canvas, "yellow", winW, winH, racket)

while ball.notTouchButtom:
    try:
        ball.ballMove()
    except:
        break
    racket.racketMove()
    tk.update()
    time.sleep(speed)