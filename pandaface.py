import turtle 

painter = turtle.Turtle()

painter.pensize(3)
painter.speed(1)


#Draw face

painter.color('black', 'black')
painter.pendown()
painter.circle(100)

#Draw right ear

painter.penup()
painter.setx(50)
painter.sety(185)
painter.pendown()

painter.begin_fill()
painter.right(90)
painter.circle(30, -260)
painter.end_fill()

