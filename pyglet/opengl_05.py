from pyglet.gl import *
import pyglet.graphics

window = pyglet.window.Window()
vl_01 = pyglet.graphics.vertex_list(2,
    ('v2i', (50, 50, 100, 100)),
    ('c3B', (255, 0, 0, 0, 255, 0))
)
vl_02 = pyglet.graphics.vertex_list(3,
    ('v2i', (200, 200, 300, 300, 300, 200))
)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    vl_01.draw(pyglet.gl.GL_POINTS)
    vl_02.draw(pyglet.gl.GL_TRIANGLES)
  

pyglet.app.run()
