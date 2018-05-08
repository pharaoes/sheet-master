from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_Triangle():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(0.5, 0.0)
    glVertex2d(-0.5, 0.0)
    glVertex2d(0.0, 0.7)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)   # Set the window's initial width & height
glutCreateWindow(b"Black_Triangle")
glutDisplayFunc(draw_Triangle)
glutMainLoop()
