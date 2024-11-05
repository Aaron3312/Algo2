import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_3d_pixel(x, y, z, size=0.1):
    """
    Dibuja un 'pixel' 3D en forma de cubo en la posición especificada
    
    Parámetros:
        x, y, z: coordenadas del centro del pixel
        size: tamaño del pixel (longitud de cada lado del cubo)
    """
    vertices = (
        (x + size, y + size, z + size),     # 0 Frente-superior-derecha
        (x - size, y + size, z + size),     # 1 Frente-superior-izquierda
        (x - size, y - size, z + size),     # 2 Frente-inferior-izquierda
        (x + size, y - size, z + size),     # 3 Frente-inferior-derecha
        (x + size, y + size, z - size),     # 4 Atrás-superior-derecha
        (x - size, y + size, z - size),     # 5 Atrás-superior-izquierda
        (x - size, y - size, z - size),     # 6 Atrás-inferior-izquierda
        (x + size, y - size, z - size),     # 7 Atrás-inferior-derecha
    )

    edges = (
        (0,1), (1,2), (2,3), (3,0),  # Cara frontal
        (4,5), (5,6), (6,7), (7,4),  # Cara trasera
        (0,4), (1,5), (2,6), (3,7)   # Conexiones
    )

    faces = (
        (0,1,2,3),  # Frente
        (4,5,6,7),  # Atrás
        (0,3,7,4),  # Derecha
        (1,2,6,5),  # Izquierda
        (0,1,5,4),  # Superior
        (2,3,7,6)   # Inferior
    )

    # Dibuja las caras del cubo
    glBegin(GL_QUADS)
    for face in faces:
        glColor3f(0.7, 0.7, 1.0)  # Color azul claro
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Dibuja los bordes del cubo
    glBegin(GL_LINES)
    glColor3f(0.2, 0.2, 0.8)  # Color azul oscuro para los bordes
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Ejemplo de uso
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Rotación para mejor visualización
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Dibuja varios pixels 3D en diferentes posiciones
        draw_3d_pixel(0, 0, 0)      # Centro
        draw_3d_pixel(0.5, 0.5, 0)  # Arriba-derecha
        draw_3d_pixel(-0.5, 0.5, 0) # Arriba-izquierda
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()