#include <iostream>
#include <vector>
#include <algorithm>

void imprimirTablero(std::vector<std::vector<char>> &tablero)
{
    for (size_t i = 0; i < tablero.size(); i++)
    {
        std::cout << "-------------" << std::endl;
        for (size_t j = 0; j < tablero[i].size(); j++)
        {
            std::cout << " " << tablero[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "-------------" << std::endl;
}

bool verificarGanador(std::vector<std::vector<char>> &tablero, char jugador)
{
    // Verificar filas
    for (size_t i = 0; i < tablero.size(); i++)
    {
        if (tablero[i][0] == jugador && tablero[i][1] == jugador && tablero[i][2] == jugador)
        {
            return true;
        }
    }

    // Verificar columnas
    for (size_t i = 0; i < tablero.size(); i++)
    {
        if (tablero[0][i] == jugador && tablero[1][i] == jugador && tablero[2][i] == jugador)
        {
            return true;
        }
    }

    // Verificar diagonales
    if (tablero[0][0] == jugador && tablero[1][1] == jugador && tablero[2][2] == jugador)
    {
        return true;
    }

    if (tablero[0][2] == jugador && tablero[1][1] == jugador && tablero[2][0] == jugador)
    {
        return true;
    }

    return false;
}

bool verificarEmpate(std::vector<std::vector<char>> &tablero)
{
    for (size_t i = 0; i < tablero.size(); i++)
    {
        for (size_t j = 0; j < tablero[i].size(); j++)
        {
            if (tablero[i][j] == ' ')
            {
                return false;
            }
        }
    }
    return true;
}

int minimax(std::vector<std::vector<char>> &tablero, int depth, bool isMaximizing)
{
    char jugador = isMaximizing ? 'O' : 'X';

    if (verificarGanador(tablero, 'O'))
    {
        return 1;
    }
    if (verificarGanador(tablero, 'X'))
    {
        return -1;
    }
    if (verificarEmpate(tablero))
    {
        return 0;
    }

    if (isMaximizing)
    {
        int bestScore = -1000;
        for (size_t i = 0; i < tablero.size(); i++)
        {
            for (size_t j = 0; j < tablero[i].size(); j++)
            {
                if (tablero[i][j] == ' ')
                {
                    tablero[i][j] = 'O';
                    std::cout << std::string(depth, '-') << "Maximizing: O at (" << i << ", " << j << "), Depth: " << depth << std::endl;
                    int score = minimax(tablero, depth + 1, false);
                    tablero[i][j] = ' ';
                    bestScore = std::max(score, bestScore);
                }
            }
        }
        return bestScore;
    }
    else
    {
        int bestScore = 1000;
        for (size_t i = 0; i < tablero.size(); i++)
        {
            for (size_t j = 0; j < tablero[i].size(); j++)
            {
                if (tablero[i][j] == ' ')
                {
                    tablero[i][j] = 'X';
                    std::cout << std::string(depth, '-') << "Minimizing: X at (" << i << ", " << j << "), Depth: " << depth << std::endl;
                    int score = minimax(tablero, depth + 1, true);
                    tablero[i][j] = ' ';
                    bestScore = std::min(score, bestScore);
                }
            }
        }
        return bestScore;
    }
}

std::pair<int, int> mejorMovimiento(std::vector<std::vector<char>> &tablero)
{
    int bestScore = -1000;
    std::pair<int, int> bestMove = {-1, -1};
    for (size_t i = 0; i < tablero.size(); i++)
    {
        for (size_t j = 0; j < tablero[i].size(); j++)
        {
            if (tablero[i][j] == ' ')
            {
                tablero[i][j] = 'O';
                int score = minimax(tablero, 0, false);
                tablero[i][j] = ' ';
                if (score > bestScore)
                {
                    bestScore = score;
                    bestMove = {i, j};
                }
            }
        }
    }
    return bestMove;
}

int convertirInput(int movimiento)
{
    switch (movimiento)
    {
    case 1: return 0 * 3 + 0;
    case 2: return 0 * 3 + 1;
    case 3: return 0 * 3 + 2;
    case 4: return 1 * 3 + 0;
    case 5: return 1 * 3 + 1;
    case 6: return 1 * 3 + 2;
    case 7: return 2 * 3 + 0;
    case 8: return 2 * 3 + 1;
    case 9: return 2 * 3 + 2;
    default: return -1;
    }
}

int main()
{
    std::vector<std::vector<char>> tablero = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};

    while (true)
    {
        imprimirTablero(tablero);
        int movimiento;
        std::cout << "Ingresa la posicion (1-9): ";
        std::cin >> movimiento;

        int pos = convertirInput(movimiento);
        int x = pos / 3;
        int y = pos % 3;

        if (pos == -1 || tablero[x][y] != ' ')
        {
            std::cout << "Posicion invalida o ocupada" << std::endl;
            continue;
        }

        tablero[x][y] = 'X';

        if (verificarGanador(tablero, 'X'))
        {
            imprimirTablero(tablero);
            std::cout << "Ganaste" << std::endl;
            break;
        }
        if (verificarEmpate(tablero))
        {
            imprimirTablero(tablero);
            std::cout << "Empate" << std::endl;
            break;
        }

        std::pair<int, int> movimientoComputadora = mejorMovimiento(tablero);
        tablero[movimientoComputadora.first][movimientoComputadora.second] = 'O';

        if (verificarGanador(tablero, 'O'))
        {
            imprimirTablero(tablero);
            std::cout << "Perdiste" << std::endl;
            break;
        }
        if (verificarEmpate(tablero))
        {
            imprimirTablero(tablero);
            std::cout << "Empate" << std::endl;
            break;
        }
    }

    return 0;
}
