import turtle

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_triangle(some_turtle):
    for index in range(1, 4):
        some_turtle.forward(100)
        some_turtle.left(120)
        index = index + 1

def draw_art():
    #set background
    window = turtle.Screen()
    window.bgcolor("white")

    #set square turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)
    for i in range(36):
        draw_square(brad)
        brad.right(10)
    
    #set and draw circle
    #angle = turtle.Turtle()
    #angle.shape("arrow")
    #angle.color("blue")
    #angle.circle(100)

    #set and draw triangle
    #tri = turtle.Turtle()
    #tri.shape("circle")
    #tri.color("white")
    #draw_triangle(tri)


    window.exitonclick()
draw_art()
