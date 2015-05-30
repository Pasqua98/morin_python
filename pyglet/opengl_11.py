from pyglet.gl import *
import pyglet.graphics
from pyglet.window import mouse
import random
from math import cos, sin, pi

window = pyglet.window.Window(600, 600, caption="moving asteroid")
cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
window.set_mouse_cursor(cursor)


batch = pyglet.graphics.Batch()
vl_asteroid = batch.add(8, pyglet.gl.GL_POLYGON, None,
    ('v2f', (20.0, 0.0, 30.0, 10.0, 40.0, 0.0, 40.0, 20.0, 50.0, 20.0, 40.0, 50.0, 10.0, 40.0, 0.0, 20.0)),
)


x = 300
y = 300
velocity = 90
theta = random.random()*2*pi
dx = velocity*cos(theta)
dy = velocity*sin(theta)

def update(dt):
    global x, y, dx, dy
    x = x + dx*dt
    if x > 600:
        x = x - 600
    if x < 0:
        x = 600 + x
    y = y + dy*dt
    if y > 600:
        y = y - 600
    if y < 0:
        y = 600 + y
        
pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz

@window.event
def on_mouse_press(u, v, button, modifiers):
    global x, y, dx, dy
    if button == mouse.LEFT:
        dx = u - x
        dy = v - y

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw outlines only
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()
    glTranslatef(x, y, 0)
    batch.draw()

pyglet.app.run()
