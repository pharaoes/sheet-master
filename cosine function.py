from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def drawing_cosine():
    glClearColor(0, 0.61, 0.98, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # draw x axis
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)

    # draw y axis
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

    # draw the equation
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POINTS)
    for x in np.arange(-1, 1, 0.001):
        y = cos(pi * x)
        z = 0
        glVertex3f(x, y, z)

    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"First Program")
glutDisplayFunc(drawing_cosine)
glutMainLoop()