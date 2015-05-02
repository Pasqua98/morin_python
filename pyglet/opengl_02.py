import pyglet
from pyglet.gl import *
 
win = pyglet.window.Window()
 
@win.event
def on_draw():
 
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT)
 
        # first picture
        glBegin(GL_LINES)
        glVertex2i(75, 50)
        glVertex2i(100, 50)
        glVertex2i(100, 75)
        glVertex2i(100, 100)
        glVertex2i(75, 100)
        glVertex2i(50, 100)
        glVertex2i(50, 75)
        glVertex2i(50, 50)
        glEnd()
        
        # second picture
        glBegin(GL_LINE_LOOP)
        glVertex2i(50, 150)
        glVertex2i(100, 150)
        glVertex2i(100, 200)
        glVertex2i(50, 200)
        glEnd()
        
        # Draw outlines only
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        
        # second picture
        glBegin(GL_TRIANGLES)
        glVertex2i(50, 250)
        glVertex2i(100, 250)
        glVertex2i(75, 300)
        glEnd()
        
        # third picture
        glBegin(GL_TRIANGLE_STRIP)
        glVertex2i(50, 350)
        glVertex2i(100, 350)
        glVertex2i(75, 400)
        glVertex2i(125, 400)
        glEnd()
        
        # 4th picture
        glBegin(GL_TRIANGLE_FAN)
        glVertex2i(200, 200)
        glVertex2i(200, 300)
        glVertex2i(250, 250)
        glVertex2i(200, 300)
        glVertex2i(150, 250)
        glVertex2i(100, 200)
        glVertex2i(150, 150)
        glVertex2i(200, 100)
        glVertex2i(250, 150)
        glVertex2i(300, 200)
        glVertex2i(250, 250)
        glEnd()
        
        # 5th picture
        glBegin(GL_POLYGON)
        glVertex2i(400,100)
        glVertex2i(500,100)
        glVertex2i(550,200)
        glVertex2i(500,300)
        glVertex2i(400,300)
        glVertex2i(350,200)
        
        glEnd()
        
        
        
        """
        Riassumendo:
        GL_POINTS
        GL_LINES
        GL_LINE_STRIP
        GL_LINE_LOOP
        GL_TRIANGLES
        GL_TRIANGLE_STRIP
        GL_TRIANGLE_FAN
        GL_QUADS
        GL_QUAD_STRIP
        GL_POLYGON
        """
        
        
        
 
pyglet.app.run()
