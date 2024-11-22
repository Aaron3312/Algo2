import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def draw_3d_pixel(x, y, z, size=0.05):
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
        glColor3f(0.95, 0.95, 0.9)  # Color hueso
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.7, 0.7, 0.7)  # Color gris más oscuro para los bordes
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def bresenham_3d_line(x0, y0, z0, x1, y1, z1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    dz = abs(z1 - z0)

    xs = 1 if x1 > x0 else -1
    ys = 1 if y1 > y0 else -1
    zs = 1 if z1 > z0 else -1

    if dx >= dy and dx >= dz:
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
    elif dy >= dx and dy >= dz:
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
    else:
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

def draw_skull():
    # Puntos para el cráneo principal
    skull_points = [
        # Parte frontal del cráneo
        (-3, 4, 2), (3, 4, 2),      # Superior
        (-4, 1, 2), (4, 1, 2),      # Medio superior
        (-4, -1, 2), (4, -1, 2),    # Medio inferior
        (-3, -3, 2), (3, -3, 2),    # Inferior
        
        # Parte trasera del cráneo
        (-3, 4, -2), (3, 4, -2),    # Superior
        (-4, 1, -2), (4, 1, -2),    # Medio superior
        (-4, -1, -2), (4, -1, -2),  # Medio inferior
        (-3, -3, -2), (3, -3, -2),  # Inferior
    ]

    # Dibujar el contorno principal del cráneo
    for i in range(0, 8, 2):
        bresenham_3d_line(*skull_points[i], *skull_points[i+1])  # Horizontal frontal
        bresenham_3d_line(*skull_points[i+8], *skull_points[i+9])  # Horizontal trasero
        bresenham_3d_line(*skull_points[i], *skull_points[i+8])   # Conectar frente y atrás

    # Dibujar suturas craneales
    bresenham_3d_line(-3, 4, 2, 0, 4.2, 2)  # Sutura coronal frontal
    bresenham_3d_line(0, 4.2, 2, 3, 4, 2)
    bresenham_3d_line(-3, 4, -2, 0, 4.2, -2)  # Sutura coronal trasera
    bresenham_3d_line(0, 4.2, -2, 3, 4, -2)
    bresenham_3d_line(0, 4.2, 2, 0, 4.2, -2)  # Sutura sagital

    # Dibujar los ojos (más detallados)
    eye_size = 1.2
    # Ojo izquierdo
    for i in range(12):
        angle = i * np.pi / 6
        x1 = -2 + eye_size * np.cos(angle)
        y1 = 1 + eye_size * np.sin(angle)
        x2 = -2 + eye_size * np.cos(angle + np.pi/6)
        y2 = 1 + eye_size * np.sin(angle + np.pi/6)
        bresenham_3d_line(int(x1*10), int(y1*10), 20, int(x2*10), int(y2*10), 20)
    # Detalle interno del ojo izquierdo
    for i in range(8):
        angle = i * np.pi / 4
        x1 = -2 + 0.5 * np.cos(angle)
        y1 = 1 + 0.5 * np.sin(angle)
        x2 = -2 + 0.5 * np.cos(angle + np.pi/4)
        y2 = 1 + 0.5 * np.sin(angle + np.pi/4)
        bresenham_3d_line(int(x1*10), int(y1*10), 20, int(x2*10), int(y2*10), 20)

    # Ojo derecho
    for i in range(12):
        angle = i * np.pi / 6
        x1 = 2 + eye_size * np.cos(angle)
        y1 = 1 + eye_size * np.sin(angle)
        x2 = 2 + eye_size * np.cos(angle + np.pi/6)
        y2 = 1 + eye_size * np.sin(angle + np.pi/6)
        bresenham_3d_line(int(x1*10), int(y1*10), 20, int(x2*10), int(y2*10), 20)
    # Detalle interno del ojo derecho
    for i in range(8):
        angle = i * np.pi / 4
        x1 = 2 + 0.5 * np.cos(angle)
        y1 = 1 + 0.5 * np.sin(angle)
        x2 = 2 + 0.5 * np.cos(angle + np.pi/4)
        y2 = 1 + 0.5 * np.sin(angle + np.pi/4)
        bresenham_3d_line(int(x1*10), int(y1*10), 20, int(x2*10), int(y2*10), 20)

    # Dibujar la cavidad nasal (más detallada)
    bresenham_3d_line(0, 0, 20, -8, -8, 20)    # Borde izquierdo
    bresenham_3d_line(0, 0, 20, 8, -8, 20)     # Borde derecho
    bresenham_3d_line(-8, -8, 20, 8, -8, 20)   # Base
    # Detalles internos de la nariz
    bresenham_3d_line(-4, -4, 20, 4, -4, 20)   # Línea media
    bresenham_3d_line(0, 0, 20, 0, -8, 20)     # Tabique nasal

    # Dibujar la mandíbula
    bresenham_3d_line(-30, -20, 20, 30, -20, 20)  # Línea superior
    bresenham_3d_line(-25, -35, 20, 25, -35, 20)  # Línea inferior
    bresenham_3d_line(-30, -20, 20, -25, -35, 20)  # Lado izquierdo
    bresenham_3d_line(30, -20, 20, 25, -35, 20)   # Lado derecho

    # Dibujar los dientes (más detallados)
    # Dientes superiores
    for i in range(-3, 4):
        bresenham_3d_line(i*7, -20, 20, i*7, -25, 20)  # Dientes verticales
        if i < 3:  # Separaciones entre dientes
            bresenham_3d_line(i*7+3.5, -20, 20, i*7+3.5, -23, 20)
    
    # Dientes inferiores
    for i in range(-3, 4):
        bresenham_3d_line(i*7, -30, 20, i*7, -35, 20)  # Dientes verticales
        if i < 3:  # Separaciones entre dientes
            bresenham_3d_line(i*7+3.5, -32, 20, i*7+3.5, -35, 20)

    # Dibujar el arco cigomático (pómulos)
    bresenham_3d_line(-30, -5, 20, -40, 5, 15)   # Izquierdo frontal
    bresenham_3d_line(-40, 5, 15, -30, 15, 10)   # Izquierdo superior
    bresenham_3d_line(30, -5, 20, 40, 5, 15)     # Derecho frontal
    bresenham_3d_line(40, 5, 15, 30, 15, 10)     # Derecho superior

def main():
    pygame.init()
    display = (1024, 768)  # Ventana más grande para mejor visualización
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -15)  # Ajustado para mejor vista

    rotation_x = 0
    rotation_y = 0
    last_mouse_pos = None
    mouse_button_pressed = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_button_pressed = True
                    last_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_button_pressed = False
            elif event.type == pygame.MOUSEMOTION:
                if mouse_button_pressed:
                    current_mouse_pos = pygame.mouse.get_pos()
                    if last_mouse_pos:
                        dx = current_mouse_pos[0] - last_mouse_pos[0]
                        dy = current_mouse_pos[1] - last_mouse_pos[1]
                        rotation_x += dy * 0.5
                        rotation_y += dx * 0.5
                        glRotatef(dy * 0.5, 1, 0, 0)
                        glRotatef(dx * 0.5, 0, 1, 0)
                    last_mouse_pos = current_mouse_pos

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_skull()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()