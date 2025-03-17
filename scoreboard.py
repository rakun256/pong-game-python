from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#fafbfb")
        self.penup()
        self.hideturtle()

    def show_board(self, score, position):
        self.goto(position)
        super().clear()
        self.write(arg=score, align="center", font=("Terminal", 80, "bold"))