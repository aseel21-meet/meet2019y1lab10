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
PLASTIC_LIST=['p1.gif','p2.gif','p3.gif','p4.gif','p5.gif']#list of all the plastic pics we have
JELLY_FISH=[]#list of three pics of jellyfish
SONGS_LIST=[] #later use
FUN_FACTS=[] #later use
#turtle.speed(0) 
SQUARE_SIZE=30
TIME_STEP=100 #speed
SCREEN_X = 800
SCREEN_Y = 800
RADIUS = SCREEN_X/12
STEP_ANGLE = 30

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
time.sleep(1)  #after 3 secounds it disapears
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

def down ():
    direction='down'
    print('you pressed the down button')
    seaturtle.shape('t5.gif')



     
    





    
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.listen()

#make new turtle


        
    

jelly1=turtle.Turtle()
jelly1.shape('circle') #to know witch jelly fish it is i defined diff shapes-later will put gifs!
jelly2=turtle.Turtle()
jelly2.shape('square')
jelly3=turtle.Turtle()
jelly3.shape('arrow')

score=0# score dont touch
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



def mj_s():
    jelly1.penup()
    jelly2.penup()
    jelly3.penup()
    jelly1.goto(400,250)
    jelly1.goto(400, 0)
    jelly1.goto(400, -250)
def move_jelly (steps):
    mj_s() #so everytime this function ends new jellyfish appear
    #for h in range (2):
    if jelly1.pos()[0] <= -SCREEN_X/2:

        jelly1.reset() #eve_jelltime the jellyfish finishes its trail then its complwtly deleted so a new one is made
        jelly2.reset()
        jelly3.reset()
        move_jelly(1) 

    
    if steps % 180/STEP_ANGLE == 0:
        if steps % 2*180/STEP_ANGLE:
            jelly1.right(90)
            jelly2.right(90)
            jelly3.right(90)
        elif steps % 180/STEP_ANGLE:
            jelly1.right(270)
            jelly2.right(270)
            jelly3.right(270)
            
    jelly1.circle(RADIUS,STEP_ANGLE)
    jelly2.circle(RADIUS,STEP_ANGLE)
    jelly1.circle(RADIUS,STEP_ANGLE) #a trail where its like curves and it looks like 4 half circles


    
##    print('i am 1 moving')
##    for r in range (2):
##        jelly2.circle(100,180)
##        jelly2.circle(100,-180)
##        print('i am 3 moving')
##    for e in range (2):
##        jelly3.circle(100,180)
##        jelly3.circle(100,-180)
##        print('i am 3 moving')

##
##    if jelly1.pos() ==seaturtle.pos() or jelly2.pos() ==seaturtle.pos() or jelly3.pos() ==seaturtle.pos() : #if the user eats the jellyfish he/she gets one point
##        turtle.print('ate jellyfish yeyy')
##        global score  #scoring system 
##        score+=1
##        scoring.clear()
##        scoring.color('blue')
##        scoring.write(score,align='center',move=False,font=('arial',18,'normal'))
##        print('you scored')
##        if jelly1.pos() ==seaturtle.pos():  #to delet the one the user ate after the user scored 
##            jelly1.reset()
##        
##        elif jelly2.pos() ==seaturtle.pos():
##            jelly2.reset()
##        elif jelly3.pos() ==seaturtle.pos():
##            jelly3.reset()

    move_jelly(steps+1)
       


    
move_jelly(1)





turtle.mainloop()


