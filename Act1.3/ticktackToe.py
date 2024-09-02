# Contador de visitas de ramas para comprender porque la profundidad de lo que realiza
contador_visitas = 0

def imprimir_tablero(tablero): # esta funcion nos hace poder imprimir un tablero en condiciones.
    for fila in tablero:
        print("---------------")
        print(" | ".join(f" {celda} " for celda in fila))
    print("---------------")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    
    # Verificar columnas
    for i in range(len(tablero)):
        if all(tablero[j][i] == jugador for j in range(len(tablero))):
            return True
    
    # Verificar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    
    return False

def verificar_empate(tablero):
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def minimax(tablero, depth, is_maximizing):
    global contador_visitas
    contador_visitas += 1  # Incrementar contador en cada llamada a minimax

    if verificar_ganador(tablero, 'O'):
        return 1
    if verificar_ganador(tablero, 'X'):
        return -1
    if verificar_empate(tablero):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'O'
                    score = minimax(tablero, depth + 1, False)
                    tablero[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'X'
                    score = minimax(tablero, depth + 1, True)
                    tablero[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def mejor_movimiento(tablero):
    best_score = -1000
    best_move = (-1, -1)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == ' ':
                tablero[i][j] = 'O'
                score = minimax(tablero, 0, False)
                tablero[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def convertir_input(movimiento): #unicamente una mejor mobilidad de input
    conversiones = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }
    return conversiones.get(movimiento, (-1, -1))

def main():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        imprimir_tablero(tablero)
        movimiento = int(input("Ingresa la posicion (1-9): "))
        x, y = convertir_input(movimiento)

        if (x, y) == (-1, -1) or tablero[x][y] != ' ':
            print("Posicion invalida o ocupada")
            continue

        tablero[x][y] = 'X'

        if verificar_ganador(tablero, 'X'):
            imprimir_tablero(tablero)
            print("Ganaste")
            break
        if verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("Empate")
            break

        movimiento_computadora = mejor_movimiento(tablero)
        tablero[movimiento_computadora[0]][movimiento_computadora[1]] = 'O'

        if verificar_ganador(tablero, 'O'):
            imprimir_tablero(tablero)
            print("Perdiste")
            break
        if verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("Empate")
            break

    # Mostrar número de visitas de ramas
    print("Numero de visitas de ramas:", contador_visitas)

if __name__ == "__main__":
    main()
