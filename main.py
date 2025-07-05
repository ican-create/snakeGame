from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from turtle import colormode
import winsound
import threading

# Create the Screen
screen = Screen()
screen.setup(width=1100, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)

# Create the scoreboard instance and pass the screen
scoreboard = Scoreboard()


# Create snake and food
snake = Snake()
food = Food()

# Sound function for non-blocking beep
def beep_async(freq, duration):
    threading.Thread(target=winsound.Beep, args=(freq, duration), daemon=True).start()

# Keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
gameIsOn = True

def game_loop():
    global gameIsOn
    while gameIsOn:
        screen.update()
        time.sleep(0.05)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 20:
            food.refresh()
            scoreboard.increaseScore()
            snake.extend()
            beep_async(600, 200)  # Play eat sound

        # Detect collision with wall
        if (
            snake.head.xcor() >530 or snake.head.xcor() < -530 or 
            snake.head.ycor() > 300 or snake.head.ycor() < -330
        ):
            gameIsOn = False
            beep_async(200, 400)  # Play game over sound
            scoreboard.gameOver()

        # Detect collision with tail
        if len(snake.segments) > 4:
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    gameIsOn = False
                    beep_async(200, 400)  # Play game over sound
                    scoreboard.gameOver()

def restart_game():
    global gameIsOn
    scoreboard.clear()
    scoreboard.score = 0
    scoreboard.goto(0, 330)
    scoreboard.updateScore()
    snake.reset()
    food.refresh()
    beep_async(400, 300)  # Play restart sound
    gameIsOn = True
    game_loop()

screen.onkey(restart_game, "r")  # Pressing 'r' calls restart_game()

game_loop()

screen.exitonclick()
