from turtle import *
import random

timmy_turner = Turtle()
screen = Screen()

screen.colormode(255)

timmy_turner.shape("classic")
timmy_turner.pensize(10)
timmy_turner.speed("fastest")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


# for i in range(3, 10):
#     for j in range(i):
#         degree = 360 / i
#         timmy_turner.forward(100)
#         timmy_turner.left(degree)
#     timmy_turner.color(random.choice(colors))
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for x in range(1000):
    timmy_turner.pencolor((random_colors()))
    timmy_turner.forward(30)
    timmy_turner.setheading(random.choice(directions))

screen.exitonclick()
