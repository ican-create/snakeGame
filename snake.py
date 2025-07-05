from turtle import Turtle
import random
POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__ (self):  
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    #create the initial snake
    @staticmethod # works with out self parameter
    def randomColor():
        r=random.randint(50,160)
        g=random.randint(70,180)
        b=random.randint(20,80)
        return(r,g,b)
    def create_snake(self):
        for position in POSITIONS:
            self.addSegment(position)
    def addSegment(self,position):
            new_segments=Turtle("square")
            new_segments.color(self.randomColor())
            new_segments.penup()
            new_segments.goto(position)
            self.segments.append(new_segments)
            
    def move(self):
        for segNum in range(len(self.segments)-1,0,-1):
            new_x=self.segments[segNum-1].xcor()
            new_y=self.segments[segNum-1].ycor()
            self.segments[segNum].goto(new_x,new_y)# goto one position of forward segment
        self.head.forward(DISTANCE)

    #move functions
    def up(self):
        if self.head.heading() !=DOWN: 
            self.head.setheading(UP)  
    def down(self):
        if self.head.heading() !=UP: 
            self.head.setheading(DOWN)   
    def left(self):
        if self.head.heading() !=RIGHT: 
            self.head.setheading(LEFT)    
    def right(self):
        if self.head.heading() !=LEFT: 
            self.head.setheading(RIGHT)   
    
    #add segment after eating food
    def extend(self):
        self.addSegment(self.segments[-1].position()) 
    
    #reset the snake
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]


