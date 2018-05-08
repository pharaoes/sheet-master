from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def drawing_heart():
    glClearColor(0, 0.61, 0.98, 1)
    glClear(GL_COLOR_BUFFER_BIT)



    # draw the heart equation
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POINTS)
    for theta in np.arange(0, 2*pi, 0.001):
        r = (2 - 2 * sin(theta) + sin(theta) * (sqrt(fabs(cos(theta))) / (sin(theta) + 1.4)))
        for n in np.arange(0,1,0.001):
            glVertex2f(r * cos(theta)*n, r * sin(theta)*n)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b" heart")
glutDisplayFunc(drawing_heart)
glutMainLoop()

