from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Initialization
def init():
    ## determine light components and calling the function (  glLightfv(....) ) to create light
    LightPos   = [0 ,0 ,0, 1]   #where the sourse of it (sun)
    LightAmb   = [0.2, 0.2, 0.2, 1] #part indirected with source
    LightDiff  = [1 ,1, 1, 1]       #part most near of ambient
    LightSpec  = [1, 1, 1, 1]       #the directed part
    global MatShn
    MatShn     = [ 128 ]

    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f
    gluPerspective(45,1,0.1,50)          #projection    fovy(x), aspect ratio(y), znear   , zfar
    gluLookAt(20,20,20,0,0,0,0,1,0)       #camera place
    #glEnable(Gl_DEPTH_TEST)


def draw_planets(raduis, sun_dist, angle, r,g,b):
    global MatShn

    glLoadIdentity()
    #its not easy to determine colors for objects(materials : planets and sun ) from now
    MatAmb  = [r, g, b, 1]  #reflection of the materials
    MatDiff = [r, g, b, 1]
    MatSpec = [r, g, b, 1]

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmb)
    #glMaterialfv(GL_BACK, GL_AMBIENT, MatAmb)   #AS source og light inside sun, So. the ambient of sun little to , we make him bigger og specular
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDiff)
    #glMaterialfv(GL_BACK, GL_DIFFUSE, MatDiff)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpec)
    #glMaterialfv(GL_BACK, GL_SPECULAR, MatSpec)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShn)
    #glMaterialfv(GL_BACK, GL_SHININESS, MatShn)

    glColor(0.3, 0.3, 0.3 )    #gray color
    glutSolidTorus(0.01, sun_dist, 30, 30)    #drawing orbits
    glColor(r,g,b)
    glRotate(angle, 0,0,1)      #planets on space not the sun x,y (space drawing) spin about z-axis
    glTranslate(sun_dist,0,0)
    glutSolidSphere(raduis,30,30)
    glRotate(angle, 0, 0,  1)


angle =[0,0]     #list of planets angles
def display_1():
    global angle                   #variable responsible in small tansformation(rotation type)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor(1.0, 0.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #sun
      #its color :yollow
    MatAmb  = [5, 5, 0, 1]  #reflection of the materials   #AS source og light inside sun, So. the ambient of sun little to , we make him bigger og specular
    MatDiff = [1, 1, 0, 1]
    MatSpec = [1, 1, 0, 1]

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDiff)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpec)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShn)

    glColor(1.0,1.0,0.0)    #yollow color
    glutSolidSphere(1,30,30)

    #mercury
    draw_planets(0.5, 3,angle[0], 1,0,0)
    angle[0] = ( angle[0] % 360) + 0.15
    #vernus
    draw_planets(0.7, 5,angle[1], 1,0,1)
    angle[1] = (angle[1] % 360) + 0.1             #remainder idea not to happens overflow for value og angle

    glutSwapBuffers()


def main():
   glutInit()
   glutInitDisplayMode ( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)   #display mode
   glutInitWindowSize(800, 800)
   glutCreateWindow (b"solar system")
   glutDisplayFunc(display_1)
   glutIdleFunc(display_1)
   init()
   glutMainLoop()

main()
