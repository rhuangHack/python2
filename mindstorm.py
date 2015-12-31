import turtle

def draw_spuare():
    window = turtle.Screen()
    window.bgcolor("red")


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(1)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angle = turtle.Turtle()
    angle.shape("arrow")
    angle.color("blue")
    angle.circle(100)

    window.exitonclick()

draw_spuare()
