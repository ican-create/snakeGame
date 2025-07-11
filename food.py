from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)  # 10x10 size
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        random_x = random.randint(-530, 530)
        random_y = random.randint(-330, 290)
        self.goto(random_x, random_y)
