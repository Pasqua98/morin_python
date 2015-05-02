from pyglet.gl import *
from pyglet.graphics import draw, draw_indexed

window = pyglet.window.Window()

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    # non essenziale annulla eventuali modifiche di scala, rotazione e traslazione
    # GL_POINT in in pyglet.gl
    draw(2, pyglet.gl.GL_POINTS,('v2i', (50, 50, 70, 70)))
    # Draw outlines only
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # indexed
    draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],  #order
        ('v2i', #2d integer
        (100, 100,
        150, 100,
        150, 150,
        100, 150))
   )

pyglet.app.run()
