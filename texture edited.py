
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import pygame 

# Rotation angles for each cube.
from pygame.tests.base_test import pygame_quit

xrot1 = yrot1 = zrot1 = 0.0
xrot2 = yrot2 = zrot2 = 0.0
# =================================================================
texture = 0


def LoadTextures():
    """  Open images and convert them to "raw" pixel maps and
         bind or associate each image with and integer refernece number.
    """
    global texture
    image0 = pygame.image.load("1.png")
    image1 = pygame.image.load("3.png")
    image2 = pygame.image.load("3.png")
    image3 = pygame.image.load("7.jpg")
    image4 = pygame.image.load("5.jpg")
    image5 = pygame.image.load("3.png")

    ix0 = image0.get_width()
    iy0 = image0.get_height()
    ix1 = image1.get_width()
    iy1 = image1.get_height()
    ix2 = image2.get_width()
    iy2 = image2.get_height()
    ix3 = image3.get_width()
    iy3 = image3.get_height()
    ix4 = image4.get_width()
    iy4 = image4.get_height()
    ix5 = image5.get_width()
    iy5 = image5.get_height()
    rawimage0 = pygame.image.tostring(image0,"RGBA",1)
    rawimage1 = pygame.image.tostring(image1,"RGBA",1)
    rawimage2 = pygame.image.tostring(image2,"RGBA",1)
    rawimage3 = pygame.image.tostring(image3,"RGBA",1)
    rawimage4 = pygame.image.tostring(image4,"RGBA",1)
    rawimage5 = pygame.image.tostring(image5,"RGBA",1)

    texture = glGenTextures(12)

    texture_setup(rawimage0,0,ix0,iy0)
    texture_setup(rawimage1, 1, ix1, iy1)
    texture_setup(rawimage2, 2, ix2, iy2)
    texture_setup(rawimage3, 3, ix3, iy3)
    texture_setup(rawimage4, 4, ix4, iy4)
    texture_setup(rawimage5, 5, ix5, iy5)
    texture_setup(rawimage0, 6, ix0, iy0)
    texture_setup(rawimage0, 7, ix0, iy0)
    texture_setup(rawimage0, 8, ix0, iy0)
    texture_setup(rawimage0, 9, ix0, iy0)
    texture_setup(rawimage0, 10, ix0, iy0)
    texture_setup(rawimage0, 11, ix0, iy0)




def texture_setup(image_name, texture_num, ix, iy):
    glBindTexture(GL_TEXTURE_2D, texture[texture_num])

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)

    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_name)


def InitGL(Width , Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear the background color to black.
    glClearDepth(1.0)  # Clear the Depth buffer.
    glDepthFunc(GL_LESS)  # The type Of depth test to do.
    glEnable(GL_DEPTH_TEST)  # Leave this Depth Testing and observe the visual weirdness.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix.
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)  # Aspect ratio. Make window resizable.
    glMatrixMode(GL_MODELVIEW)

# ==============================================================



def make_cube_1(start):
    global texture
    glBindTexture(GL_TEXTURE_2D,texture[start])

    glBegin(GL_QUADS)
    glTexCoord(0,0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left of The Texture and Quad

    glTexCoord(1,0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Right of The Texture and Quad

    glTexCoord(1,1)
    glVertex3f(1.0, 1.0, 1.0)  # Top Right of The Texture and Quad

    glTexCoord(0,1)
    glVertex3f(-1.0, 1.0, 1.0)# Top Left of The Texture and Quad
    glEnd()


    # Back Face
    glBindTexture(GL_TEXTURE_2D,texture[start+1])

    glBegin(GL_QUADS)

    glTexCoord(0,0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right

    glTexCoord(1,0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Rightn

    glTexCoord(1,1)
    glVertex3f(1.0, 1.0, -1.0)  # Top Left

    glTexCoord(0,1)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left
    glEnd()

    # Top Face
    glBindTexture(GL_TEXTURE_2D,texture[start+2])

    glBegin(GL_QUADS)
    glTexCoord(0,0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left

    glTexCoord(1,0)
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left

    glTexCoord(1,1)
    glVertex3f(1.0, 1.0, 1.0)  # Bottom Right

    glTexCoord(0,1)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glEnd()

    # Bottom Face
    glBindTexture(GL_TEXTURE_2D,texture[start]+3)

    glBegin(GL_QUADS)
    glTexCoord(0,0)
    glVertex3f(-1.0, -1.0, -1.0)  # Top Right

    glTexCoord(1,0)
    glVertex3f(1.0, -1.0, -1.0)  # Top Left

    glTexCoord(1,1)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left

    glTexCoord(0,1)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glEnd();

    # Right face
    glBindTexture(GL_TEXTURE_2D,texture[start]+4)


    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right

    glTexCoord(1, 0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right

    glTexCoord(1,1)
    glVertex3f(1.0, 1.0, 1.0)  # Top Left

    glTexCoord(0, 1)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glEnd();

    # Left Face
    glBindTexture(GL_TEXTURE_2D,texture[start]+5)

    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left

    glTexCoord(1, 0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right

    glTexCoord(1,1)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right

    glTexCoord(0, 1)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glEnd();



def DrawFrontFace():
    """   A texture binding created with glBindTexture remains active until a different texture
    	  is bound to the same target, or until the bound texture is deleted with glDeleteTextures.
    """
    global xrot1, yrot1, zrot1, xrot2, yrot2, zrot2
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen and Depth buffer

    # First textured cube.
    glLoadIdentity()  # Reset The View
    glTranslatef(-2.0, 0.0, -5.0)  # Shift cube left and back.
    glRotatef(xrot1, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot1, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot1, 0.0, 0.0, 0.0)  # Rotate the cube on It's Z axis.
    make_cube_1(0)  # "0" is the first index no. of a six member sequence - images.

    xrot1 = xrot1 + 0.1  # X rotation of first cube.
    yrot1 = yrot1 - 0.05  # Y rotation
    zrot1 = zrot1 + 0.05  # Z rotation

    # Second textured cube.
    glLoadIdentity()  # Reset The view
    glTranslatef(1.5, 0.0, -5.0)  # Shift cube right and back.
    glRotatef(xrot2, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot2, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot2, 0.0, 0.0, 0.0)  # Rotate the cube on It's Z axis
    make_cube_1(6)  # "6" is the first index no. of a different six member sequence - images.

    xrot2 = xrot2 - 0.05  # X rotation of second cube.
    yrot2 = yrot2 + 0.07  # Y rotation
    zrot2 = zrot2 + 0.09  # Z rotation

    glutSwapBuffers()

    # =================================================================


def main():
    glutInit("")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(1000, 480)
    window = glutCreateWindow(b"Textured rotating cubes")
    LoadTextures()
    glutDisplayFunc(DrawFrontFace)
    glutIdleFunc(DrawFrontFace)  # When we are doing nothing, redraw the scene.
    InitGL(1000, 480)  # Initialize our window.
    glutMainLoop()  # Start the event processing engine


main()






