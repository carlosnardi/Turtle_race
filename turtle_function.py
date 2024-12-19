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

  
  