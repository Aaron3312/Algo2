import numpy as np

def cross_product_sign(v1, v2):
    """
    Calcula el signo del producto cruz entre dos vectores 2D.
    Returns:
        1 si es positivo (sentido antihorario)
        -1 si es negativo (sentido horario)
        0 si es cero (vectores paralelos)
    """
    # El producto cruz en 2D es: v1.x * v2.y - v1.y * v2.x
    cross = v1[0] * v2[1] - v1[1] * v2[0]
    
    if abs(cross) < 1e-10:  # Para manejar errores de punto flotante
        return 0
    return 1 if cross > 0 else -1

# Definir los vectores para cada caso
# Caso 1: ángulo agudo
v1_caso1 = np.array([1, 0])
v2_caso1 = np.array([1, 1])

# Caso 2: ángulo obtuso
v1_caso2 = np.array([1, 1])
v2_caso2 = np.array([1, -1])

# Caso 3: vectores paralelos
v1_caso3 = np.array([-1, 0])
v2_caso3 = np.array([1, 0])

# Calcular los resultados
resultado1 = cross_product_sign(v1_caso1, v2_caso1)
resultado2 = cross_product_sign(v1_caso2, v2_caso2)
resultado3 = cross_product_sign(v1_caso3, v2_caso3)

print("Resultados del producto cruz P1 × P2:")
print(f"Caso 1: {'Positivo' if resultado1 > 0 else 'Negativo' if resultado1 < 0 else 'Cero'}")
print(f"Caso 2: {'Positivo' if resultado2 > 0 else 'Negativo' if resultado2 < 0 else 'Cero'}")
print(f"Caso 3: {'Positivo' if resultado3 > 0 else 'Negativo' if resultado3 < 0 else 'Cero'}")