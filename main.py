from turtle import Turtle, Screen
from turtle_function import TurtleModel 
import random

screen = Screen()
screen.setup(width=150,height=100)
user_choice = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter your color: ").lower()

speed = [10,20,30,40,50]

color_list = ["red", "blue", "purple", "orange", "green", "yellow"]
turtles_list = []
y_axis = 75

for item in color_list:
  turtle_created = TurtleModel(color=item,x=-140,y=y_axis)
  turtles_list.append(turtle_created)
  y_axis -= 25

race_in_progress = True

while race_in_progress:
  for turtle in turtles_list:
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
