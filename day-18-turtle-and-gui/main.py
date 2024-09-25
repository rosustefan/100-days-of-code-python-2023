# Define a dict with shapes and their number of edges/sides
SHAPES = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "nonagon": 9,
    "decagon": 10,
}

# Turtle string-like colours
COLOURS = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

# Turtle directions: left, up, right, down
DIRECTIONS = [0, 90, 180, 270]

# Colours extract using colorgram.extract(<image>, num_colours_to_extract)
EXTRACTED_RGB_COLOURS = [
    (244, 242, 237),
    (228, 234, 241),
    (245, 237, 241),
    (235, 243, 238),
    (214, 157, 85),
    (33, 105, 151),
    (238, 215, 94),
    (153, 75, 52),
    (125, 168, 199),
    (209, 134, 163),
    (156, 60, 81),
    (22, 39, 54),
    (212, 85, 61),
    (176, 162, 47),
    (200, 85, 119),
    (135, 184, 150),
    (56, 119, 90),
    (240, 213, 4),
    (25, 46, 37),
    (228, 167, 186),
    (64, 46, 34),
    (87, 157, 100),
    (9, 99, 75),
    (34, 166, 189),
    (40, 60, 102),
    (228, 175, 166),
    (179, 189, 213),
    (95, 126, 173),
    (68, 34, 44),
    (105, 42, 60),
]


from turtle import Turtle, Screen
from os import sys
import random
import colorgram


# Draw a square
def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


# Draw a dotted line
def draw_dotted_line():
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# Draw shapes based on their number of edges and color
def draw_shapes():
    for shape, num_edges in SHAPES.items():
        print(f"Drawing a {shape}!")
        for _ in range(num_edges):
            angle = 360 / num_edges
            tim.pencolor(generate_colour())  # RGB tuple generator
            tim.forward(100)
            tim.right(angle)


# Generate a random RGB colour
def generate_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


# Generate a random walk
def random_walk():
    for _ in range(210):
        # tim.color(random.choice(colours))
        tim.pencolor(generate_colour())
        tim.pensize(8)
        tim.speed("fastest")
        tim.forward(21)
        tim.setheading(random.choice(DIRECTIONS))


# Draw a spirograph
def draw_spirograph():
    tim.speed("fastest")
    heading_shift = 5  # in degrees
    for _ in range(int(360 / heading_shift)):
        tim.pencolor(generate_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + heading_shift)


# Create a Hirst-like spot painting
def spot_painting():
    # 1. Extract most frequent x colors from an image
    # colors = colorgram.extract("day-18-turtle-and-gui\image.jpg", 30)
    # rgb_colors = []
    # for color in colors:
    #     red = color.rgb.r
    #     green = color.rgb.g
    #     blue = color.rgb.b
    #     new_color = (red, green, blue)
    #     rgb_colors.append(new_color)

    # 2. Use previously extracted RGB colours to paint circles
    # Move the cursor/turtle to the bottom-left part of the screen
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(320)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        # Draw circle shape
        tim.dot(20, random.choice(EXTRACTED_RGB_COLOURS))
        tim.forward(50)

        # Move the cursor/turtle to the start of the next line
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)  # Enable full RGB range (0-255)

    tim = Turtle()
    tim.shape("turtle")
    tim.color("green")

    # Get user input
    user_input = int(
        input(
            "1 for Square, \n\
2 for Dotted line, \n\
3 for Shapes, \n\
4 for Random walk, \n\
5 for Spirograph, \n\
6 for Spot Painting, \n\
0 to quit: "
        )
    )

    # Match case to call the corresponding function
    match user_input:
        case 1:
            draw_square()
        case 2:
            draw_dotted_line()
        case 3:
            draw_shapes()
        case 4:
            random_walk()
        case 5:
            draw_spirograph()
        case 6:
            spot_painting()
        case 0:
            sys.exit(0)
        case _:
            print("Invalid input, please enter a number between 1 and 4.")

    screen.exitonclick()
