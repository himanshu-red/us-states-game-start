from turtle import Turtle


class States_on_map(Turtle):
    def __init__(self):
        super().__init__()

    def point_on_map(self, text, x, y):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(text, False, align="center", font=('Arial', 8, "normal"))
