import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

def draw_diamond():
    glBegin(GL_TRIANGLES)

    glColor(1, 1, 0) # colour yellow
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glColor(0, 0, 1) # colour blue
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    #

    glColor(1, 1, 0) # colour yellow
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glColor(0, 0, 1) # colour blue
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glEnd()

pygame.init()
display = (800, 600) # windows size
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Diamond")
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslate(0, 0, 0-5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glRotate(1, 1, 1, 1) # rotate object
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_diamond()
    pygame.display.flip()
    pygame.time.wait(15)