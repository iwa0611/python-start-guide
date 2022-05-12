import turtle

class Turtle_square(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.shape('turtle')
    self.shapesize(2,2)

  def draw_square(self):
    for x in range (20):
      for x in range(4):
        self.fd(100)
        self.left(90)
      self.left(18)

#四角を18度ずつ傾けながら２０回描画する。
