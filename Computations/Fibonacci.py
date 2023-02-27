from turtle import *

def fibo(fibo_nr):
    def draw_square(side_length):  #Function for drawing a square
        for i in range(4):
            forward(side_length)
            right(90)

    nr=len(fibo_nr)

    if nr < 6:
        factor=10
    elif nr > 5 and nr < 11:
        factor=5
    else:
        setup(1.0, 1.0)
        factor = 1                        #Enlargement factor

    penup()
    goto(50,50)                  #Move starting point right and up
    pendown()
    for i in range(nr):
        draw_square(factor*fibo_nr[i]) #Draw square
        penup()                        #Move to new corner as starting point
        if i == nr-1:
            break
        forward(factor*fibo_nr[i])
        right(90)
        forward(factor*fibo_nr[i])
        pendown()

    penup()
    goto(50,50)       #Move to starting point
    setheading(0)   #Face the turtle to the right
    pencolor('red')
    pensize(2)
    pendown()
    #Draw quartercircles with fibonacci numbers as radius
    for i in range(nr):
        circle(-factor*fibo_nr[i],90)  # minus sign to draw clockwise
    done()
