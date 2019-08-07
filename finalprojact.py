import turtle
import time
import random
#import winsound
turtle.bgpic('water.gif')
turtle.tracer(1.0)#MOVE SMOOTHLY

x_size=1000
y_size=1000
turtle.setup(x_size,y_size) #WINDOW SIZE


PLASTIC_LIST=['p1.gif','p2.gif','p3.gif','p4.gif','p5.gif']#list of all the plastic pics we have

SONGS_LIST=[] #later use

SQUARE_SIZE=20
TIME_STEP=50 #speed
SCREEN_X = 800
SCREEN_Y = 800

##border=turtle.Turtle() #drawing the actual game bored in the screen wich is 800 on 800
##border.penup()
##border.goto(-400,400)
##border.pendown()
##border.goto(400,400)
##border.goto(400,-400)
##border.goto(-400,-400)
##border.goto(-400,400)
##border.hideturtle()


#create the game ored-design

title='trash crash'





#the title and instructions showing off on screen at the beggining

instructions='1.avoid the trash\n 2.eat the jellyfish\n 3.you may only use the up and down buttons\n  4.have fun'
turtle.color('blue')
turtle.penup()
turtle.goto(0,400)
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
jelly1.speed(10)
jelly2.speed(10)
jelly3.speed(10)

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




  
def move_jelly ():
    make_jelly()
    
    jelly1.penup()
    jelly2.penup()
    jelly3.penup()

    #moving th three jelly in a designed-messy path
    jelly1.left(90)
    jelly1.circle(100,180)
    jelly2.left(90)
    jelly2.circle(100,180)
    jelly3.left(90)
    jelly3.circle(100,180)
    jelly1.seth(0)
    jelly1.circle(100,300)
    jelly2.seth(0)
    jelly2.circle(100,300)
    jelly3.seth(0)
    jelly3.circle(100,300)
    jelly1.seth(90)
    jelly1.circle(100,180)
    jelly2.seth(90)
    jelly2.circle(100,180)
    jelly3.seth(90)
    jelly3.circle(100,180)
    jelly1.seth(0)
    jelly1.circle(100,300)
    jelly2.seth(0)
    jelly2.circle(100,300)
    jelly3.seth(0)
    jelly3.circle(100,300)
    jelly1.seth(90)
    jelly1.circle(100,180)
    jelly2.seth(90)
    jelly2.circle(100,180)
    jelly3.seth(90)
    jelly3.circle(100,180)

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
  
    #move_jelly()
    move_trash()
    turtle.ontimer(move_jelly, 20)

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
    

def dist(pos1, pos2):
    return ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5

def move_trash():
    make_trash()
    trash1.penup()
    trash2.penup()
    trash3.penup()
    trash4.penup()
    trash5.penup()
    print("moving")
    trash1_x=trash1.xcor()
    dist1=-400-(trash1_x)
    trash2_x=trash2.xcor()
    dist2=-400-(trash2_x)
    trash3_x=trash3.xcor()
    dist3=-400-(trash3_x)
    trash4_x=trash4.xcor()
    dist4=-400-(trash4_x)
    trash5_x=trash5.xcor()
    dist5=-400-(trash5_x) 

    trash1.forward((dist1))
    trash2.forward((dist2))
    trash3.forward((dist3))
    trash4.forward((dist4))
    trash5.forward((dist5))
    move_jelly()
    #if (seaturtle.pos()==trash1.pos(0 or seaturtle.pos()==trash2.pos() or seaturtle.pos()==trash3.pos() or seaturtle.pos()==trash4.pos() or seaturtle.pos()==trash5.pos():
    if dist(seaturtle.pos(),trash1.pos())<45 or dist(seaturtle.pos(),trash2.pos())<45 or dist(seaturtle.pos(),trash3.pos())<45 or dist(seaturtle.pos(),trash4.pos())<45 or dist(seaturtle.pos(),trash5.pos())<45:
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(0,0)
        turtle.write('loser',move=False,align='center',font=('arial',18,'normal'))
        quit()
    
   
    turtle.ontimer(move_trash, 200)
    

    
    

        


move_trash()
move_jelly()
                  





turtle.mainloop()


