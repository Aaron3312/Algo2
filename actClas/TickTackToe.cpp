#include <iostream>
#include <vector>
#include <algorithm>

void imprimirTablero(std::vector<std::vector<char>> &tablero)
{
    for (size_t i = 0; i < tablero.size(); i++)
    {
        for (size_t j = 0; j < tablero[i].size(); j++)
        {
            std::cout << tablero[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

bool verificarGanador(std::vector<std::vector<char>> &tablero, char jugador)
{
    for (size_t i = 0; i < tablero.size(); i++)
    {
        if (tablero[i][0] == jugador && tablero[i][1] == jugador && tablero[i][2] == jugador)
        {
            return true;
        }
    }

    for (size_t i = 0; i < tablero.size(); i++)
    {
        if (tablero[0][i] == jugador && tablero[1][i] == jugador && tablero[2][i] == jugador)
        {
            return true;
        }
    }

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

int main()
{
    std::vector<std::vector<char>> tablero = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    char jugador = 'X';
    bool ganador = false;
    bool empate = false;

    while (!ganador && !empate)
    {
        imprimirTablero(tablero);
        int x, y;
        std::cout << "Ingrese la posicion (x, y): ";
        std::cin >> x >> y;

        if (tablero[x][y] == ' ')
        {
            tablero[x][y] = jugador;
            ganador = verificarGanador(tablero, jugador);
            empate = verificarEmpate(tablero);
            jugador = jugador == 'X' ? 'O' : 'X';
        }
        else
        {
            std::cout << "Posicion ocupada" << std::endl;
        }
    }

    imprimirTablero(tablero);

    if (ganador)
    {
        jugador = jugador == 'X' ? 'O' : 'X';
        std::cout << "Ganador: " << jugador << std::endl;
    }
    else
    {
        std::cout << "Empate" << std::endl;
    }

    return 0;
}