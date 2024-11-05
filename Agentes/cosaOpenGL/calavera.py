import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_3d_pixel(x, y, z, size=0.05):
    """
    Dibuja un 'pixel' 3D en forma de cubo en la posición especificada
    
    Parámetros:
        x, y, z: coordenadas del centro del pixel
        size: tamaño del pixel (longitud de cada lado del cubo)
    """
    vertices = (
        (x + size, y + size, z + size),
        (x - size, y + size, z + size),
        (x - size, y - size, z + size),
        (x + size, y - size, z + size),
        (x + size, y + size, z - size),
        (x - size, y + size, z - size),
        (x - size, y - size, z - size),
        (x + size, y - size, z - size),
    )

    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    glBegin(GL_QUADS)
    for face in ((0, 1, 2, 3), (4, 5, 6, 7), (0, 3, 7, 4), (1, 2, 6, 5), (0, 1, 5, 4), (2, 3, 7, 6)):
        glColor3f(0.7, 0.7, 1.0)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.2, 0.2, 0.8)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def bresenham_3d_line(x0, y0, z0, x1, y1, z1):
    """
    Dibuja una línea 3D entre dos puntos usando el algoritmo de Bresenham.
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    dz = abs(z1 - z0)

    xs = 1 if x1 > x0 else -1
    ys = 1 if y1 > y0 else -1
    zs = 1 if z1 > z0 else -1

    if dx >= dy and dx >= dz:  # El eje X es el dominante
        p1 = 2 * dy - dx
        p2 = 2 * dz - dx
        while x0 != x1:
            draw_3d_pixel(x0 * 0.1, y0 * 0.1, z0 * 0.1)
            x0 += xs
            if p1 >= 0:
                y0 += ys
                p1 -= 2 * dx
            if p2 >= 0:
                z0 += zs
                p2 -= 2 * dx
            p1 += 2 * dy
            p2 += 2 * dz
    elif dy >= dx and dy >= dz:  # El eje Y es el dominante
        p1 = 2 * dx - dy
        p2 = 2 * dz - dy
        while y0 != y1:
            draw_3d_pixel(x0 * 0.1, y0 * 0.1, z0 * 0.1)
            y0 += ys
            if p1 >= 0:
                x0 += xs
                p1 -= 2 * dy
            if p2 >= 0:
                z0 += zs
                p2 -= 2 * dy
            p1 += 2 * dx
            p2 += 2 * dz
    else:  # El eje Z es el dominante
        p1 = 2 * dy - dz
        p2 = 2 * dx - dz
        while z0 != z1:
            draw_3d_pixel(x0 * 0.1, y0 * 0.1, z0 * 0.1)
            z0 += zs
            if p1 >= 0:
                y0 += ys
                p1 -= 2 * dz
            if p2 >= 0:
                x0 += xs
                p2 -= 2 * dz
            p1 += 2 * dy
            p2 += 2 * dx

def draw_skull(x, y, z):
    """
    Dibuja una calavera en 3D en la posición especificada.
    
    Parámetros:
        x, y, z: Coordenadas del centro de la calavera.
    """
    # Escala básica de la calavera
    scale = 1.0

    # Cráneo (superior)
    bresenham_3d_line(x - scale, y + scale, z, x + scale, y + scale, z)   # Frente
    bresenham_3d_line(x - scale, y, z, x - scale, y + scale, z)           # Lado izquierdo
    bresenham_3d_line(x + scale, y, z, x + scale, y + scale, z)           # Lado derecho
    bresenham_3d_line(x - scale, y, z, x + scale, y, z)                   # Parte inferior del cráneo

    # Ojos
    eye_offset_x = 0.3 * scale
    eye_offset_y = 0.5 * scale
    eye_size = 0.2 * scale
    # Ojo izquierdo
    bresenham_3d_line(x - eye_offset_x - eye_size, y + eye_offset_y, z, x - eye_offset_x + eye_size, y + eye_offset_y, z)
    bresenham_3d_line(x - eye_offset_x, y + eye_offset_y - eye_size, z, x - eye_offset_x, y + eye_offset_y + eye_size, z)
    # Ojo derecho
    bresenham_3d_line(x + eye_offset_x - eye_size, y + eye_offset_y, z, x + eye_offset_x + eye_size, y + eye_offset_y, z)
    bresenham_3d_line(x + eye_offset_x, y + eye_offset_y - eye_size, z, x + eye_offset_x, y + eye_offset_y + eye_size, z)

    # Nariz
    nose_width = 0.1 * scale
    bresenham_3d_line(x - nose_width, y + 0.2 * scale, z, x, y, z)
    bresenham_3d_line(x + nose_width, y + 0.2 * scale, z, x, y, z)

    # Mandíbula (inferior)
    jaw_width = 0.8 * scale
    jaw_height = 0.4 * scale
    bresenham_3d_line(x - jaw_width / 2, y - jaw_height, z, x + jaw_width / 2, y - jaw_height, z)   # Línea inferior de la mandíbula
    bresenham_3d_line(x - jaw_width / 2, y - jaw_height, z, x - jaw_width / 2, y, z)               # Lado izquierdo de la mandíbula
    bresenham_3d_line(x + jaw_width / 2, y - jaw_height, z, x + jaw_width / 2, y, z)               # Lado derecho de la mandíbula

# Ejemplo de uso en el entorno OpenGL y Pygame
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)  # Habilita el Depth Test

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Dibuja la calavera en una posición central
        draw_skull(0, 0, 0)
        
        pygame.display.flip()
        pygame.time.wait(10)




if __name__ == "__main__":
    main()
