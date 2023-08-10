from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.screen = Screen()

    def create_snake(self):
        for i in range(3):
            b1 = Turtle(shape="square")
            b1.color("white")
            b1.penup()
            b1.goto(-20 * i, 0)
            self.snake.append(b1)

    def increase(self):
        b1 = Turtle(shape="square")
        b1.color("white")
        b1.penup()
        b1.goto(self.snake[len(self.snake)-1].xcor(), self.snake[len(self.snake)-1].ycor())
        self.snake.append(b1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):

        for num in range(len(self.snake) - 1, 0, -1):
            self.snake[num].goto(self.snake[num - 1].xcor(), self.snake[num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)
