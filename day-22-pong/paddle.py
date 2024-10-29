from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")  # by default starts with size 20 by 20
        self.color("white")
        self.shapesize(
            stretch_wid=5,
            stretch_len=1,
        )
        self.penup()
        self.goto(position)

    def go_up(self) -> None:
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self) -> None:
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
