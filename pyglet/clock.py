import pyglet
from datetime import datetime

window = pyglet.window.Window(200,100)
cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
window.set_mouse_cursor(cursor)

label = pyglet.text.Label('OROLOGIO',
    font_name = 'Lora',
    font_size = 40,
    x = 10, 
    y = 20,
    anchor_x ='left', 
    anchor_y='bottom'
    )
        
def update(dt):
    label.text = datetime.now().time().isoformat().split(".")[0]
    # print "tick"
    
pyglet.clock.schedule_interval(update, 0.5)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
