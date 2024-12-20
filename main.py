from turtle import Turtle, Screen
from turtle_function import TurtleModel 
import random

screen = Screen()
screen.setup(width=150,height=100)
user_choice = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter your color: ").lower()

speed = [10,20,30,40,50]

red = TurtleModel(color="red",x=-140,y=50)
blue = TurtleModel(color="blue",x=-140,y=25)
purple = TurtleModel(color="purple",x=-140,y=0)
orange = TurtleModel(color="orange",x=-140,y=-25)
green = TurtleModel(color="green",x=-140,y=-50)

turtles = [red, blue, purple, orange, green]

race_in_progress = True

while race_in_progress:
  for turtle in turtles:
    turtle.move_forward(random.choice(speed))
    if turtle.position() >= 140:
      turtle_winner = turtle.turtle_color()
      race_in_progress = False

if user_choice == turtle_winner:
  print("You won")
else:
  print("You lost")
print(f"{turtle_winner.title()} won the race")

screen.mainloop()
