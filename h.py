import turtle
def h():
    turtle.left(2)
    turtle.forward(3)
    turtle.ontimer(h,1)
h()
