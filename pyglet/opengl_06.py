from pyglet.gl import *
import pyglet.graphics

window = pyglet.window.Window()
vl_asteroid = pyglet.graphics.vertex_list(8,
    ('v2i', (20, 0, 30, 10, 40, 0, 40, 20, 50, 20, 40, 50, 10, 40, 0, 20)),
)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw outlines only
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # 1) originale
    glLoadIdentity()
    vl_asteroid.draw(pyglet.gl.GL_POLYGON)
    
    # 2) translazione
    glLoadIdentity()
    glTranslatef(100, 100, 0)
    vl_asteroid.draw(pyglet.gl.GL_POLYGON)
    
    # 3) translazione e rotazione
    glLoadIdentity()
    glTranslatef(200, 200, 0)
    glRotatef(45, 0, 0, 1)
    vl_asteroid.draw(pyglet.gl.GL_POLYGON)
    
    # 4) translazione e scala
    glLoadIdentity()
    glTranslatef(300, 300, 0)
    glScalef(2, 2, 1)
    vl_asteroid.draw(pyglet.gl.GL_POLYGON)
   
  

pyglet.app.run()
