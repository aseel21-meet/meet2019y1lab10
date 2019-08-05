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
turtle.register_shape('t4.gif') #the turtle up pic
turtle.register_shape('t5.gif')#the turtle.down pic
TURTLE_LIST=['t4.gif','t5.gif'] #lst of turtle pics we can use
PLASTIC_LIST=['p1.gif','p2.gif','p3.gif','p4.gif','p5.gif']#list of all the plastic pics we have
JELLY_FISH=[]#list of three pics of jellyfish
SONGS_LIST=[] #later use
FUN_FACTS=[] #later use
#turtle.speed(0) 
SQUARE_SIZE=30
TIME_STEP=100 #speed


border=turtle.Turtle() #drawing the actual game bored in the screen witch is 800 on 800
border.penup()
border.goto(-400,400)
border.pendown()
border.goto(400,400)
border.goto(400,-400)
border.goto(-400,-400)
border.goto(-400,400)
border.hideturtle()


#create the game ored-design

title='trash crash'
bag3=turtle.clone()
bag4=turtle.clone()
bag5=turtle.clone()
bag6=turtle.clone()
bag7=turtle.clone()
bag8=turtle.clone()
bag9=turtle.clone()
bag10=turtle.clone()
bag11=turtle.clone()
bag12=turtle.clone()




#the title and instructions showing off on screen at the beggining

instructions='1.avoid the trash\n 2.eat the jellyfish\n 3.you may only use the up and down buttons\n  4.have fun'
turtle.color('blue')
turtle.penup()
turtle.goto(0,200)
turtle.write(title,move=False,align='center',font=('arial',18,'normal'))
turtle.hideturtle()
instructor=turtle.Turtle()
instructor.color('pink')
instructor.penup()
instructor.goto(0,0)
instructor.write(instructions,move=False,align='center',font=('arial',18,'normal'))
instructor.hideturtle()
time.sleep(3)  #after 3 secounds it disapears
instructor.clear()
turtle.hideturtle()


seaturtle=turtle.Turtle()  #main turtle the user can play with       
#for i in TURTLE_LIST: #registers a turtle shape out of the list
    #turtle.register_shape (i)


#up and down... movement
direction='none'
def up (): #setting a new shape to turtle according to the direction 
    direction='up'
    print('you pressed the up button')
    seaturtle.shape('t4.gif')
#def right ():
    #direction='right'
    #print('you pressed the right button')
    #seaturtle.shape('t2.gif')

#def left():
    #direction='left'
    #print('you pressed the left button')
    #seaturtle.shape('t1.gif')
def down ():
    direction='down'
    print('you pressed the down button')
    seaturtle.shape('t5.gif')



     
    





    
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
#turtle.onkeypress(left,'Left')
#turtle.onkeypress(right,'Right')
turtle.listen()

#make new turtle
#level one

bag2=turtle.clone()
my_list=[bag,bag2]
#seaturtle.penup()
def move_seaturtle():
    my_pos=seaturtle.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if direction=='up':
        seaturtle.goto(x_pos,y_pos+SQUARE_SIZE)
        #seaturtle.forward(SQAURE_SIZE)
        print('moved up')
    elif direction=='down':
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
def move_bag(plastic):   
    x_bag=plastic.pos()[0]
    y_bag=plastic.pos()[1]
    plastic.goto(x_bag-10,y_bag)
    turtle.ontimer(move_bag,BAG_TIME_STEP)
    
def move_all_bags():
    my_list=[bag,bag2]
    for i in my_list:
        ontimer(move_bag(plastic),1000)
        
    
for i in my_list:
    move_bag(i)


score=0
scoring=turtle.Turtle()
scoring.penup()
scoring.goto(0,-400)
scoring.pendown()
scoring.hideturtle()

def make_jelly (): #maing  3 diff jelly fishes (they are turtles)
    min_x=300
    max_x=400
    min_y=-400
    max_y=400  #the edges of the area they are supposed to apear in 
    jelly1=turtle.Turtle()
    jelly1.shape('circle') #to know witch jelly fish it is i defined diff shapes-later will put gifs!
    jelly2=turtle.Turtle()
    jelly2.shape('square')
    jelly3=turtle.Turtle()
    jelly3.shape('arrow')
    jelly1.penup()
    jelly2.penup()
    jelly3.penup()
    jelly1_x_cor=random.randint(min_x,max_x)
    jelly1_y_cor=random.randint(min_y,max_y)
    jelly2_x_cor=random.randint(min_x,max_x)
    jelly2_y_cor=random.randint(min_y,max_y)
    jelly3_x_cor=random.randint(min_x,max_x)
    jelly3_y_cor=random.randint(min_y,max_y) #the three show up in random diff places in the area
    jelly1.goto(jelly1_x_cor,jelly1_y_cor)
    jelly2.goto(jelly2_x_cor,jelly2_y_cor)
    jelly3.goto(jelly3_x_cor,jelly3_y_cor)
def move_jelly ():
    make_jelly() #so everytime this function ends new jellyfish appear
    for h in range (2):
        jelly1.circle(100,180)
        jelly1.circle(100,-180) #a trail where its like curves and it looks like 4 half circles 
        print('i am 1 moving')
    for r in range (2):
        jelly2.circle(100,180)
        jelly2.circle(100,-180)
        print('i am 3 moving')
    for e in range (2):
        jelly3.circle(100,180)
        jelly3.circle(100,-180)
        print('i am 3 moving')
    
    if jelly1.pos() ==seaturtle.pos() or jelly2.pos() ==seaturtle.pos() or jelly3.pos() ==seaturtle.pos() : #if the user eats the jellyfish he/she gets one point
        turtle.print('ate jellyfish yeyy')
        global score  #scoring system 
        score+=1
        scoring.clear()
        scoring.color('blue')
        scoring.write(score,align='center',move=False,font=('arial',18,'normal'))
        print('you scored')
        if jelly1.pos() ==seaturtle.pos():  #to delet the one the user ate after the user scored 
            jelly1.reset()
        
        elif jelly2.pos() ==seaturtle.pos():
            jelly2.reset()
        elif jelly3.pos() ==seaturtle.pos():
            jelly3.reset()
        
    jelly1.reset() #everytime the jellyfish finishes its trail then its complwtly deleted so a new one is made
    jelly2.reset()
    jelly3.reset()

	


    
    
    
make_bag()
#move_bag(my_list)








turtle.mainloop()


