import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("MAKE YOUR BET", "Which turtle will win the race?\n\t Enter Color:")
y_pos = [0, 50, 100, -50, -100]
colors = ["red", "orange", "yellow", "green", "blue"]

all_turtles = []

print(user_bet)

is_race_on = False

for turtle_index in range(0, 5):
    new_turtle = Turtle()
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-200, y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_bet = turtle.pencolor()
            if winning_bet == user_bet:
                print("YOU WIN")
            else:
                print("You lost, loser")

        dist = random.randint(0, 10)
        turtle.forward(dist)

screen.exitonclick()
