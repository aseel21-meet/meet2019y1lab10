import turtle
import time
import random
turtle.bgpic('water.gif')
turtle.tracer(1.0)#MOVE SMOOTHLY

x_size=1000
y_size=1000
turtle.setup(x_size,y_size) #WINDOW SIZE
global timess
timess=0

PLASTIC_LIST=['p1.gif','p2.gif','p3.gif','p4.gif','p5.gif']#list of all the plastic pics we have

SONGS_LIST=[] #later use

SQUARE_SIZE=20
TIME_STEP=100 #speed
SCREEN_X = 800
SCREEN_Y = 800


title='trash crash'

#the title and instructions showing off on screen at the beggining

instructions='1.avoid the trash\n 2.eat the jellyfish\n 3.you may only use the up and down buttons\n  4.have fun'
turtle.color('pink')
turtle.penup()
turtle.goto(0,450)
turtle.write(title,move=False,align='center',font=('arial',18,'normal'))
turtle.hideturtle()
instructor=turtle.Turtle()
instructor.color('green')
instructor.penup()
instructor.goto(0,0)
instructor.write(instructions,move=False,align='center',font=('arial',18,'normal'))
instructor.hideturtle()
time.sleep(1)  #after 3 secounds it disapears
instructor.clear()
turtle.hideturtle()
turtle.color('red')


seaturtle=turtle.Turtle()  #main turtle the user can play with       
#for i in TURTLE_LIST: #registers a turtle shape out of the list
    #turtle.register_shape (i)
seaturtle.hideturtle()





turtle.register_shape("s.t.gif")
seaturtle.shape ("s.t.gif")
UP_EDGE = 400
DOWN_EDGE = -400
seaturtle.direction="Up"
seaturtle.penup()
seaturtle.goto(-200,0)
seaturtle.showturtle()



def up():
    seaturtle.direction="Up" #Change direction to up
    move_seaturtle()
    print("You pressed the up key!")

def down():
    seaturtle.direction="Down" #Change direction to up
    move_seaturtle()
    print("You pressed the down key!")

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down,"Down")
turtle.listen()
def dist(pos1, pos2):
    return ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5

def move_seaturtle():
    my_pos = seaturtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = seaturtle.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()            
   
   
   
    if seaturtle.direction == "Up":
        seaturtle.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif seaturtle.direction=="Down":
        seaturtle.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")
     
    
  #making jelly fish  
turtle.register_shape('jf.gif')
jelly1=turtle.Turtle()
jelly1.hideturtle()
jelly1.shape('jf.gif') #to know witch jelly fish it is i defined diff shapes-later will put gifs!
jelly2=turtle.Turtle()
jelly2.hideturtle()
jelly2.shape('jf.gif')
jelly3=turtle.Turtle()
jelly3.hideturtle()
jelly3.shape('jf.gif')
##jelly1.speed(10)
##jelly2.speed(10)
##jelly3.speed(10)

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
    max_y=200  #the edges of the area they are supposed to apear in 
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
    jelly1.showturtle()
    jelly2.goto(jelly2_x_cor,jelly2_y_cor)
    jelly2.showturtle()
    jelly3.goto(jelly3_x_cor,jelly3_y_cor)
    jelly3.showturtle()
def reset_jelly(jelly):
    print("*****RESETTING*******")
    jelly.hideturtle()
    make_jelly()
    jelly.showturtle()
global side
side =True
jelly1.right(163)
jelly2.right(163)
jelly3.right(163)
def go_jelly():
    global side
   
    global timess
    timess+=1
   
    jelly1.forward(4)
    jelly2.forward(4)
    jelly3.forward(4)
    print(jelly1.pos())
    if dist(jelly1.pos(),seaturtle.pos())<45 or dist(jelly2.pos(),seaturtle.pos())<45 or dist(jelly3.pos(),seaturtle.pos())<45 : #if the user eats the jellyfish he/she gets one point
        print('*******************')
        print(seaturtle.pos())
        print(jelly1.pos())
        print('**')
        print(dist(jelly1.pos(),seaturtle.pos()))
        print(dist(jelly2.pos(),seaturtle.pos()))
        print(dist(jelly3.pos(),seaturtle.pos()))
        print('ate jellyfish yeyy')
        global score  #scoring system
        score+=1
        scoring.clear()
        scoring.color('blue')
        scoring.write(score,align='center',move=False,font=('arial',18,'normal'))
        print('you scored')
        
    if dist(jelly1.pos(),seaturtle.pos())<45:  #to delet the one the user ate after the user scored 
        reset_jelly(jelly1)
    elif dist(jelly2.pos() ,seaturtle.pos())<45:
        reset_jelly(jelly2)
    elif dist(jelly3.pos() ,seaturtle.pos())<45:
        reset_jelly(jelly3)
    if timess==85:
       
        if side==True:
            jelly2.right(50)
            jelly1.right(50)
            jelly3.right(50)
        else:
            jelly1.left(50)
            jelly2.left(50)
            jelly3.left(50)
        side=not side
        timess=0
    turtle.ontimer(go_jelly, 10)
 #trash gifs   
turtle.register_shape('t1.gif')
turtle.register_shape('t2.gif')
turtle.register_shape('t3.gif')
turtle.register_shape('t4.gif')
turtle.register_shape('t5.gif')

    #making new 5 turtles as trash
trash1=turtle.Turtle()
trash1.hideturtle()
trash1.shape('t1.gif') #to know which jelly fish it is i defined diff shapes-later will put gifs!
trash2=turtle.Turtle()
trash2.hideturtle()
trash2.shape('t2.gif')
trash3=turtle.Turtle()
trash3.hideturtle()
trash3.shape('t3.gif')
trash4=turtle.Turtle()
trash4.hideturtle()
trash4.shape('t4.gif')
trash5=turtle.Turtle()
trash5.hideturtle()
trash5.shape('t5.gif')



def make_trash ():
    min_x=300
    max_x=400
    min_y=-400
    max_y=400  #the edges of the area they are supposed to apear in 
    trash1.penup()
    trash2.penup()
    trash3.penup()
    trash4.penup()
    trash5.penup()
    trash1.speed(10)
    trash2.speed(10)
    trash3.speed(10)
    trash4.speed(10)
    trash5.speed(10)
    trash1.hideturtle()
    trash2.hideturtle()
    trash3.hideturtle()
    trash4.hideturtle()
    trash5.hideturtle()
    trash1_x_cor=random.randint(min_x,max_x)
    trash1_y_cor=random.randint(min_y,max_y)
    trash2_x_cor=random.randint(min_x,max_x)
    trash2_y_cor=random.randint(min_y,max_y)
    trash3_x_cor=random.randint(min_x,max_x)
    trash3_y_cor=random.randint(min_y,max_y)#the three show up in random diff places in the area
    trash4_x_cor=random.randint(min_x,max_x)
    trash4_y_cor=random.randint(min_y,max_y)
    trash5_x_cor=random.randint(min_x,max_x)
    trash5_y_cor=random.randint(min_y,max_y) 
    trash1.goto(trash1_x_cor,trash1_y_cor)
    trash1.showturtle()
    trash2.goto(trash2_x_cor,trash2_y_cor)
    trash2.showturtle()
    trash3.goto(trash3_x_cor,trash3_y_cor)
    trash3.showturtle()
    trash4.goto(trash4_x_cor,trash4_y_cor)
    trash4.showturtle()
    trash5.goto(trash5_x_cor,trash5_y_cor)
    trash5.showturtle()
    


def move_trash():
    make_trash()
    trash1.penup()
    trash2.penup()
    trash3.penup()
    trash4.penup()
    trash5.penup()
    print("moving")

    id1_ls=[]
    id2_ls=[]
    id3_ls=[]
    id4_ls=[]
    id5_ls=[]

    for step in range (30):
        
        trash1.goto(trash1.xcor()-SQUARE_SIZE,trash1.ycor())
        id1=trash1.stamp()
        id1_pos = trash1.pos()
        id1_ls.append(id1)
        print(trash1.pos())
        if dist(seaturtle.pos(),id1_pos)<45 :
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0,0)
            turtle.write('loser',move=False,align='center',font=('arial',32,'normal'))
            quit()
        
        trash1.goto(trash1.xcor()-SQUARE_SIZE,trash1.ycor())
        trash1.clearstamp(id1)

        id1_ls.pop(0)
        
        
        
    for step in range (40):
        
        trash2.goto(trash2.xcor()-SQUARE_SIZE,trash2.ycor())
        id2=trash2.stamp()
        id2_pos=trash2.pos()
        id2_ls.append(id2)
        if dist(seaturtle.pos(),id2_pos)<45 :
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0,0)
            turtle.write('loser',move=False,align='center',font=('arial',32,'normal'))
            quit()
        

        trash2.goto(trash2.xcor()-SQUARE_SIZE,trash2.ycor())
        trash2.clearstamp(id2)
        id2_ls.pop(0)
        if id2_pos[1]==-400:
            break
         
    for step in range (40):
        
        trash3.goto(trash3.xcor()-SQUARE_SIZE,trash3.ycor())
        id3=trash3.stamp()
        id3_pos=trash3.pos()
        id3_ls.append(id3)
        if dist(seaturtle.pos(),id3_pos)<45 :
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0,0)
            turtle.write('loser',move=False,align='center',font=('arial',32,'normal'))
            quit()
        if id3_pos[1]==-400:
           break     

        trash3.goto(trash3.xcor()-SQUARE_SIZE,trash3.ycor())
        trash3.clearstamp(id3)
        id3_ls.pop(0)
    for step in range (40):
        
        trash4.goto(trash4.xcor()-SQUARE_SIZE,trash4.ycor())
        id4=trash4.stamp()
        id4_pos=trash4.pos()
        id4_ls.append(id4)
        if dist(seaturtle.pos(),id4_pos)<45 :
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0,0)
            turtle.write('loser',move=False,align='center',font=('arial',32,'normal'))
            quit()
        if id4_pos[1]==-400:
            break    

        trash4.goto(trash4.xcor()-SQUARE_SIZE,trash4.ycor())
        trash4.clearstamp(id4)
        id4_ls.pop(0)
        
    for step in range (40):
        
        trash5.goto(trash5.xcor()-SQUARE_SIZE,trash5.ycor())
        id5=trash5.stamp()
        id5_pos=trash5.pos()
        id5_ls.append(id5)
        if dist(seaturtle.pos(),id5_pos)<45 :
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0,0)
            turtle.write('loser',move=False,align='center',font=('arial',32,'normal'))
            quit()
        if id5_pos[1]==-400:
            break    

        trash5.goto(trash5.xcor()-SQUARE_SIZE,trash5.ycor())
        trash5.clearstamp(id5)
        id5_ls.pop(0)
        
    
    
    

    turtle.ontimer(move_trash, TIME_STEP)
    

    
    

        
make_jelly()
go_jelly()
move_trash()


                  





turtle.mainloop()



