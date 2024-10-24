import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def snake_game() -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Listen to arrow-keys pressed
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.15)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            # Move food to a new random location
            food.refresh()
            # Increase snake size by +1
            snake.extend()
            # Increase the score by +1
            scoreboard.increase_score()

        # Detect collision with wall
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        # NOTE: Compare all segments, but the head because it will fail at game start
        for segment in snake.segments[1::]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    snake_game()
