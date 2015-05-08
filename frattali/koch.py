import turtle


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)
           
t = turtle
t.penup()
t.setposition(-100,0)
t.pendown()

koch(t, 4, 300)

raw_input("batti INVIO")
