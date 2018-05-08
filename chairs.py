from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def init():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
def draw_cube(n,x,y,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glMatrixMode(GL_MODELVIEW)
    glScale(x,y,z)
    glutSolidCube(n)
    glPopAttrib()
    glPopMatrix()
def draw():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    draw_cube(2,3,.5,3)

    glTranslate(0,2.5,-3)
    draw_cube(2,3,3,.5)

    glTranslate(-2.8,-5.5,-1)
    draw_cube(1,.5,5,.5)

    glTranslate(5.3,0,1)
    draw_cube(1,.5,5,.5)

    glTranslate(0,0,5)
    draw_cube(1.2,.5,5,.5)

    glTranslate(-5.2,0,.7)
    draw_cube(1,.5,5,.5)

    glPopAttrib()
    glPopMatrix()



def draw_2():
    glMatrixMode(GL_MODELVIEW)
    glColor3f(0, 0, 1)
    glTranslate(-5,0,0)
    draw()
    glColor3f(1,0,0)
    glTranslate(7,0,0)
    draw()

    glFlush()






glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"......")
glutDisplayFunc(draw_2)
init()
glutMainLoop()