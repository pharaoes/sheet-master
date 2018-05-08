from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def draw_rectangle(x0,y0,size):
    glColor3d(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2d(x0 + size/2, y0 + size)
    glVertex2d(x0 + size/2, y0 - size)
    glVertex2d( x0 - size/2, y0 - size)
    glVertex2d(x0 - size/2, y0 + size)
    glEnd()
    glFlush()

def draw_circle(r,x0,y0):
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = x0+r * cos(theta)
        y = y0+r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()

def draw_Square():
    glColor3d(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.5)
    glVertex2d( 0.5, -0.5)
    glVertex2d( 0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glEnd()
    glFlush()


def face():
    #face circle
    draw_circle(.8, 0, 0)
    #circle right eye
    draw_circle(.1, .35, .30)
    #circle left eye
    draw_circle(.1, -.35, .30)

def body():
    glColor3d(1, 0, 0)
    draw_rectangle(0.2,0.6,0.15)

def knec():
    draw_rectangle(0.2,0.1,0.15)

def hands():
    draw_rectangle(0.26,0.3,0.1569)

def legs():
    draw_rectangle(0.3,0.0,0.4)

def dol():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    body()
    face()
    legs()
    hands()

    glFlush()


#__main function
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 700)   # Set the window's initial width & height
glutCreateWindow(b":intial carton man report")
glutDisplayFunc(dol)
glutMainLoop()


