from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

game_on = True


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.title("Snake Cradle")
screen.tracer(0)
score = ScoreBoard()

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase()
        score.eaten()

    # Detect the Collision with the Wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        print("Game over with wall ")
        game_on = False
        score.game_over()

    # Detect the collision with the snake itself
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            print("Game over")
            game_on = False
            score.game_over()

screen.exitonclick()
