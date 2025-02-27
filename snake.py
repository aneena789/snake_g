import os
import turtle
import time
import random

delay=0.1

segments = []#initially no segments

#set up screen
wn=turtle.Screen()
wn.title("worm game")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off animation on screen updates

#Snake head
head=turtle.Turtle()
head.speed(0)#animation speed-fastest speed possible
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


#Snake food
food=turtle.Turtle()
food.speed(0)#animation speed-fastest speed possible
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)


#Functions

def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_left():
    if head.direction!="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"    



def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#Main game loop-updates everytime continuously
while True:
    wn.update()

    #check for collision with the border
    if head.xcor()> 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the segments
        for segment in segments:
             segment.goto(1000,1000)

        #clear segment list
        segments.clear()

    #check for collision with food
    if head.distance(food)<20:
        #move the food new position
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)




    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)  
            head.direction="stop"
            
             #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

             #clear segment list
            segments.clear()


    time.sleep(delay)


wn.mainloop()#keep window open .entire code exist between tracer and mainloop