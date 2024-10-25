# Act 4.1
def orientacion(p, q, r):
    """
    Determina la orientación del triplete ordenado (p, q, r).
    Retorna:
    0 --> p, q y r son colineales
    1 --> Sentido horario
    -1 --> Sentido antihorario
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    if val > 0:
        return 1
    return -1

def intersectan(p1, q1, p2, q2):
    """
    Determina si el segmento p1q1 intersecta con el segmento p2q2
    """
    o1 = orientacion(p1, q1, p2)
    o2 = orientacion(p1, q1, q2)
    o3 = orientacion(p2, q2, p1)
    o4 = orientacion(p2, q2, q1)

    # Caso general
    if o1 != o2 and o3 != o4:
        return True

    # Casos especiales
    if o1 == 0 and sobre_segmento(p1, p2, q1): 
        return True
    if o2 == 0 and sobre_segmento(p1, q2, q1): 
        return True
    if o3 == 0 and sobre_segmento(p2, p1, q2): 
        return True
    if o4 == 0 and sobre_segmento(p2, q1, q2): 
        return True

    return False

def sobre_segmento(p, q, r):
    """
    Verifica si el punto q está en el segmento pr
    """
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

#--Entrada Manual--
# lines = []
# while True:
#     try:
#         line = input().strip()
#         if line:
#             lines.append(line)
#         else:
#             break
#     except EOFError:
#         break

#--Leer la entrada desde un archivo--
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Procesar cada línea
results = []
for line in lines:
    points = list(map(float, line.split(',')))
    p1 = (points[0], points[1])
    q1 = (points[2], points[3])
    p2 = (points[4], points[5])
    q2 = (points[6], points[7])
    results.append(intersectan(p1, q1, p2, q2))

# Imprimir resultados
print(results)