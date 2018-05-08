from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10,10, -10, 10)

    glMatrixMode(GL_MODELVIEW)

def circle(rad, cx=0, cy=0):
    glLoadIdentity()
    glBegin(GL_POINTS)
    for i in np.arange(0, 100, 0.1):
        x = rad*np.cos(i *2* np.pi/100)
        y = rad*np.sin(i *2* np.pi/100)
        glVertex2d(x+cx, y+cy)
    glEnd()

def circle_face(rad, cx=0, cy=0):
    glLoadIdentity()
    glBegin(GL_LINES)
    for i in np.arange(0, 100, 0.1):
        x = rad * np.cos(i * 2 * np.pi / 100)
        y = rad * np.sin(i * 2 * np.pi / 100)
        glVertex2d(cx , cy)
        glVertex2d(x + cx, y + cy)
    glEnd()


def mouth(len):
    glLoadIdentity()
    glBegin(GL_LINES)
    glVertex2d(len/2,-2.5)
    glVertex2d(-len/2,-2.5)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(3)
    glLoadIdentity()
    glColor(0,0,0)
    circle(5)    #inner Face
    circle(5.5)  #Out Face

    # Right Eye
    circle(0.7,2,1)

    #Left Eye
    circle(0.7, -2, 1)
    #face
    circle_face(0.4,-2,1)
    circle_face(0.4, 2, 1)
    # Nose
    circle(0.6,0,-1)
    # mouth
    mouth(4)
    glutSwapBuffers()






glutInit()
glutInitWindowSize(600,600)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutCreateWindow(b"Face")
init()
glutDisplayFunc(draw)
glutMainLoop()