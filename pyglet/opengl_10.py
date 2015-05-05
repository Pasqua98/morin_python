from pyglet.gl import *
import pyglet.graphics

window = pyglet.window.Window()
# colora la finestra
glClearColor(0.05, 0.05, 0.2, 1)

vl_triangle = pyglet.graphics.vertex_list(3,
    ('v2i', (200, 200, 300, 300, 300, 200)),
    ('c3B', (255, 0, 0, 0, 255, 0, 0, 0, 255))
)

x = 0
def update(dt):
    global x
    x += 1


pyglet.clock.schedule_interval(update, 0.5)

@window.event
def on_draw():
    global x
    # cancella il display
    glClear(GL_COLOR_BUFFER_BIT)
    
    # la successiva istruzione non e' necessaria: DEFAULT e' GL_MODELVIEW (muove l'oggetto)
    glMatrixMode(GL_MODELVIEW)
    # rimpiazza la matrice al suo posto di origine
    glLoadIdentity()
    # I STEP: trasla alle coordinate float (OPEN_GL)
    glTranslatef(128, 128, 0)
    # II STEP: ruota attorno all'asse z (OPEN_GL)
    glRotatef(x, 0, 0, 1)
    glTranslatef( -128, -128, 0 )
    
    # disegna l'oggetto
    vl_triangle.draw(pyglet.gl.GL_TRIANGLES)

pyglet.app.run()
