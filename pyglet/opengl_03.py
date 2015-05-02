from pyglet.gl import *
# Direct OpenGL commands to this window.

window = pyglet.window.Window()

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    # non essenziale annulla eventuali modifiche di scala, rotazione e traslazione
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(window.width/2, window.width/2)
    glVertex2f(window.width, window.height/4)
    glVertex2f(3*window.width/4, window.height)
    glEnd()


pyglet.app.run()
