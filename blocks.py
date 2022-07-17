from turtle import Turtle

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color('red')
        self.penup()

    def delete(self):
        self.goto(1000, 1000)