import turtle
class  DrawLine():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sim(self):
        turtle.setpos(self.x,self.y)
a=DrawLine(50,50)
a.sim()