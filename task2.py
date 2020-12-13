import turtle as t


class DrawRectangle:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def set(self,X,Y,Width,Height):
        self.x=X
        self.y=Y
        self.width=Width
        self.height=Height

    def show(self):
        t.tracer(False)
        t.pensize(2)
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        for _ in range(0,2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)

a=DrawRectangle(0,0,50,60)
a.show()