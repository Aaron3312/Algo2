import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math
from time import time

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

def draw_3d_pyramid(apex, base_points):
    # Dibujar la base
    for i in range(len(base_points)):
        bresenham_3d_line(
            base_points[i][0], base_points[i][1], base_points[i][2],
            base_points[(i + 1) % len(base_points)][0],
            base_points[(i + 1) % len(base_points)][1],
            base_points[(i + 1) % len(base_points)][2]
        )
    
    # Dibujar las líneas desde el apex hasta cada esquina de la base
    for point in base_points:
        bresenham_3d_line(
            apex[0], apex[1], apex[2],
            point[0], point[1], point[2]
        )

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

    # Definir los puntos iniciales de la pirámide
    original_apex = (0, 5, 0)
    original_base_points = [
        (-5, -5, 5),
        (5, -5, 5),
        (5, -5, -5),
        (-5, -5, -5)
    ]

    # Variables para el control del mouse
    rotation_x = 0
    rotation_y = 0
    last_mouse_pos = None
    mouse_button_pressed = False

    # Variables para la animación
    start_time = time()
    radius = 5.0
    angular_velocity = 2.0

    # Variable para alternar entre movimientos
    movement_type = 'circular'  # puede ser 'circular' o 'linear'
    linear_start = (-10, 0, 0)
    linear_end = (10, 0, 0)
    linear_speed = 2.0

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Cambiar tipo de movimiento
                    movement_type = 'linear' if movement_type == 'circular' else 'circular'
                    start_time = time()

        current_time = time() - start_time
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Guardar la matriz actual
        glPushMatrix()
        
        if movement_type == 'circular':
            # Movimiento circular
            x = radius * math.cos(angular_velocity * current_time)
            z = radius * math.sin(angular_velocity * current_time)
            glTranslatef(x, 0, z)
        else:
            # Movimiento lineal
            progress = (math.sin(current_time) + 1) / 2  # Oscila entre 0 y 1
            x = linear_start[0] + (linear_end[0] - linear_start[0]) * progress
            z = linear_start[2] + (linear_end[2] - linear_start[2]) * progress
            glTranslatef(x, 0, z)
        
        # Dibujar la pirámide
        draw_3d_pyramid(original_apex, original_base_points)
        
        # Restaurar la matriz
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()