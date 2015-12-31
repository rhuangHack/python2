import turtle

def shadow(some_turtle, length, ratio, angle):
    if length < 10:
        return
    some_turtle.forward(length)
    some_turtle.left(angle)         #turn left part first
    shadow(some_turtle, length * ratio, ratio, angle)
    some_turtle.right(angle * 2)    #tutn to right part
    shadow(some_turtle, length * ratio, ratio, angle)
    some_turtle.left(angle + 180)   #turn back
    some_turtle.forward(length)     #walk back to start point
    some_turtle.left(180)           #turn to end child



def draw_shadow():
    #set background color
    window = turtle.Screen()
    window.bgcolor("white")

    #create shadows
    mark = turtle.Turtle()
    mark.shape("turtle")
    mark.color("green")
    mark.speed(0)

    mark.left(90)
    shadow(mark, 90, 0.8, 25)

    mark.color("brown")
    mark.right(180)
    shadow(mark, 80, 0.7, 35)
    window.exitonclick()            #exit wait on click

draw_shadow()
