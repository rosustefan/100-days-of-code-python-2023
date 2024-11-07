from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Left top corner
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
