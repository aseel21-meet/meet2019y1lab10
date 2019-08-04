import turtle
import time
#import random
#import winsound

turtle.tracer(1.0)#MOVE SMOOTHLY

x_size=1000
y_size=1000
turtle.setup(x_size,y_size) #WINDOW SIZE

TURTLE_LIST=['t1.gif','t2.gif','t3.gif','t4.gif','t5.gif']
PLASTIC_LIST=['p1.gif','p2.gif','p3.gif','p4.gif','p5.gif']
JELLY_FISH=[]
SONGS_LIST=[]
FUN_FACTS=[]

SQUARE_SIZE=30
TIME_STEP=100


#create the game ored-design

title='trash crash'



#the title amd instructions

instructions='1.avoid the trash\n 2.eat the jellyfish\n 3.have fun'
turtle.penup()
turtle.goto(0,200)
turtle.write(title,move=False,align='center',font=('arial',18,'normal'))
turtle.hideturtle()
instructor=turtle.Turtle()
instructor.penup()
instructor.goto(0,0)
instructor.write(instructions,move=False,align='center',font=('arial',18,'normal'))
instructor.hideturtle()
time.sleep(5)
instructor.clear()
turtle.hideturtle()


        



seaturtle=turtle.Turtle()
direction='none'
def up ():
    direction='up'
    print('you pressed the up button')
    seaturtle.register_shape('t4.gif')
def right ():
    direction='right'
    print('you pressed the right button')
    seaturtle.register_shape('t2.gif')

def left():
    direction='left'
    print('oyu pressed the left button')
    seaturtle.register_shape('t1.gif')
def down ():
    direction='down'
    print('you pressed the down button')
    turtle.register_shape('t5.gif')

turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')
turtle.listen()

#make new turtle
#level one
seaturtle.penup()
def move_seaturtle():
    my_pos=seaturtle.pos()
    x_pos=[0]
    y_pos=[1]
    if direction==up:
        seaturtle.goto(x_pos,y_pos+SQUARE_SIZE)
        print('moved up')
    if directon==down:
        seaturtle.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')
        seaturtle.ontimer(move_seaturtle,TIME_STEP)
        
move_seaturtle()



turtle.mainloop()


