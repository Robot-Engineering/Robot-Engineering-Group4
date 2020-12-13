import turtle
class  DrawRect():
    def __init__(self,long,high):
        self.long=long
        self.high=high
    def sim(self):
        for i in range(4):
            turtle.fd(self.long)
            turtle.seth(-90+i*(-90))
a=DrawRect(50,60)
a.sim()
        