import turtle
import time
import random
#import winsound

turtle.tracer(1.0)#MOVE SMOOTHLY

x_size=1000
y_size=1000
turtle.setup(x_size,y_size) #WINDOW SIZE
BAG_TIME_STEP=100
bag_list=[]
bag_pos=[]
bag=turtle.clone()
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
for i in TURTLE_LIST: #registers a turtle shape out of the list
    turtle.register_shape (i)


#up and down... movement
direction='none'
def up ():
    direction='up'
    print('you pressed the up button')
    seaturtle.shape('t4.gif')
def right ():
    direction='right'
    print('you pressed the right button')
    seaturtle.shape('t2.gif')

def left():
    direction='left'
    print('you pressed the left button')
    seaturtle.shape('t1.gif')
def down ():
    direction='down'
    print('you pressed the down button')
    seaturtle.shape('t5.gif')



     
    






    
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')
turtle.listen()

#make new turtle
#level one


#seaturtle.penup()
def move_seaturtle():
    my_pos=seaturtle.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]



    
    if direction==up:
        seaturtle.goto(x_pos,y_pos+SQUARE_SIZE)
        #seaturtle.forward(SQAURE_SIZE)
        print('moved up')
    elif direction==down:
        seaturtle.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')
    


def make_bag():
    bag.penup()
    line=random.randint(1,3)
    if line==1:
        bag.goto(500,seaturtle.ycor()+100)
    if line==2:
        bag.goto(500,seaturtle.ycor())
    if line==3:
        bag.goto(500,seaturtle.ycor()-100)
    
def move_bag():
    x_bag=bag.pos()[0]
    y_bag=bag.pos()[1]
    bag.goto(x_bag-10,y_bag)
    turtle.ontimer(move_bag,BAG_TIME_STEP)
make_bag()
move_bag()


turtle.mainloop()


