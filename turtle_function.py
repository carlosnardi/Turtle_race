from turtle import Turtle

class TurtleModel:
  def __init__(self, color, x, y):
    self.turtle_model = Turtle()
    self.turtle_model.penup()
    self.turtle_model.color(color)
    self.turtle_model.shape("turtle")
    self.turtle_model.home()
    self.turtle_model.speed("slowest")
    self.turtle_model.setposition(x,y)


  def move_forward(self,size):
    self.turtle_model.forward(size)

  def position(self):
    actual_position = self.turtle_model.position()
    return actual_position[0]

  def turtle_color(self):
    turtle_color = self.turtle_model.fillcolor()
    return turtle_color