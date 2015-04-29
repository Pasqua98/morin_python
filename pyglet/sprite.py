import pyglet
import random
from math import cos, sin, pi


window = pyglet.window.Window(600,600)

ball_image = pyglet.image.load('ball.png')
sprite = pyglet.sprite.Sprite(ball_image)
sprite.position = (300,300)

velocity = 90
theta = random.random()*2*pi

sprite.dx = velocity*cos(theta)
sprite.dy = velocity*sin(theta)

def update(dt):
    if sprite.x > 600-80 or sprite.x < 10:
        sprite.dx = -sprite.dx
    sprite.x += sprite.dx * dt
    if sprite.y > 600-80 or sprite.y < 10:
        sprite.dy = -sprite.dy
    sprite.y += sprite.dy * dt
    
        
pyglet.clock.schedule_interval(update, 1/40.0) # update at 40Hz

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()
