import pyglet
from pyglet.window import mouse

window = pyglet.window.Window(500,500)

label = pyglet.text.Label('Start',
    font_name = 'Lora',
    font_size = 12,
    x = window.width//2, 
    y = window.height//2,
    anchor_x ='left', 
    anchor_y='center'
    )

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        label.text = 'mouse@' + str(x) + ',' + str(y)
        label.x = x
        label.y = y
    
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
