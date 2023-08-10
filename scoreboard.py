from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 12, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()

        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.count}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)


    def eaten(self):
        self.count += 1
        self.clear()
        self.update_score()
