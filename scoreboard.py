from turtle import Turtle,Screen
from food import Food
from snake import Snake

ALLIGNMENT="center"
FONT=('Courier',20,'italic')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,320)
        self.hideturtle()
        self.updateScore()


    def updateScore(self):
        self.clear()
        self.write(f"Score : {self.score} ",align=ALLIGNMENT,font=FONT)
    def increaseScore(self):
        self.score+=1
        self.updateScore()
   
    def gameOver(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER",align=ALLIGNMENT,font=('Courier',40,'italic','bold'))
        self.goto(0,-40)
        self.write("Press R for Reset",align=ALLIGNMENT,font=('Courier',20,'italic','bold'))
        self.color("white")


    
