import turtle 
bz=turtle.Turtle()
scr=turtle.Screen()
bz.speed(0)
scr.bgcolor("black")
color=("red","Green","Magenta","Blue","Purple","Orange")
for i in range(300):
    bz.pencolor(color[i%6])
    bz.width(i/100==1)
    bz.forward(i)
    bz.left(61)
turtle.done() 