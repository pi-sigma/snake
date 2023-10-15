import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_on = True
while game_on is True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -299 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        # snake.reset()  # alternative mechanism for restarting the game (part)
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[-1::1]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            # snake.reset()  # alternative mechanism for restarting the game (part)
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
