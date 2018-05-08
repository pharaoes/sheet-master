from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame



def init():
    LightPos = [0, 0, 0, 1]
    LightAmb = [0.2, 0.2, 0.2, 1.0]
    LightDiff = [1, 1, 1, 1.0]
    LightSpec = [1, 1, 1, 1.0]
    global MatShnF
    MatShnF = [128]

    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glClearColor(0.0, 0.0, 0.0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(45, 1, 0.1, 50)
    gluLookAt(15, 15, 15, 0, 0, 0, 0, 1, 0)
    glEnable(GL_DEPTH_TEST)

angle = [0, 0]

def draw_planet(sun_dist, radius, angle, r, g, b):
    global MatShnF
    glLoadIdentity()
    MatAmbF = [r, g, b, 1]
    MatDifF = [r, g, b, 1]
    MatSpecF = [r, g, b, 1]

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShnF)

    glColor(r, g, b, 0)
    glutSolidTorus(0.01, sun_dist, 30, 30)
    glRotate(angle, 0, 0, 1)
    glTranslate(sun_dist, 0, 0)
    glRotate(angle, 0, 0, 1)
    glutSolidSphere(radius, 30, 30)

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #sun
    draw_planet(0, 1, 0, 5, 5, 0)
    #mercury
    draw_planet(3, 0.5, angle[0], 1, 0, 0)
    angle[0] = (angle[0] % 360) + 0.1
    #vernus
    draw_planet(5, 0.7, angle[1], 1, 0, 1)
    angle[1] = (angle[1] % 360) + 0.15


    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutCreateWindow(b"Solar System")
glutDisplayFunc(display)
glutIdleFunc(display)
init()
glutMainLoop()