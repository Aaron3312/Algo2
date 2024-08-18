#include <iostream>
#include <vector>
#include <algorithm>

void imprimirResultado(std::vector<int> &monedas, std::vector<int> &resultado)
{
    for (size_t i = 0; i < monedas.size(); i++)
    {2
        std::cout << "Monedas de " << monedas[i] << ": " << resultado[i] << std::endl;
    }
}

void cambioGreedy(std::vector<int> &monedas, int cantidad, int size)
{
    std::vector<int> resultado(size, 0); // Vector para guardar que monedas vamos usando
    for (int i = 0; i < size; i++) // Como se le pasa el vector de monedas ya ordenado va usando la moneda de mas valor hasta que ya no pueda
    {
        while (cantidad >= monedas[i])
        {
            resultado[i]++;
            cantidad -= monedas[i];
        }
    }
    std::cout << "Resultado Greedy: " << std::endl;
    if (cantidad != 0) // No se puede hacer la cantidad restante con las monedas disponibles
    {
        std::cout << "No se puede dar cambio exacto" << std::endl;
        return;
    }
    imprimirResultado(monedas, resultado);
}

void cambioDynamic(std::vector<int> &monedas, int cantidad, int size)
{
    std::vector<int> soluciones(cantidad + 1, INT_MAX); // Menor cantidad de monedas para cada cantidad
    std::vector<int> monedasUsadas(cantidad + 1, INT_MAX); // Todas las monedas usadas para las soluciones
    std::vector<int> resultado(size, 0); // Monedas que usamos para la solucion final
    soluciones[0] = 0;

    for (int i = 1; i <= cantidad; i++)
    {
        for (int j = 0; j < size; j++)
        {
            int coin = monedas[j];
            if (i >= coin && soluciones[i - coin] != INT_MAX)
            {
                if (soluciones[i] > soluciones[i - coin] + 1)
                {
                    soluciones[i] = soluciones[i - coin] + 1; //Guardamos cuantas monedas se usaron para esta solucion 
                    monedasUsadas[i] = j; // Guardamos la moneda que se utilizo
                }
            }
        }
    }

    if (soluciones[cantidad] != INT_MAX) //Vemos que monedas usamos para la solucion final
    {
        int current = cantidad;
        while (current > 0)
        {
            int i = monedasUsadas[current];
            resultado[i]++;
            current -= monedas[i];
        }
    }

    std::cout << "Resultado Dynamic: " << std::endl;
    if (soluciones[cantidad] == INT_MAX)
    {
        std::cout << "No se puede dar cambio exacto" << std::endl;
        return;
    }
    imprimirResultado(monedas, resultado);
}

int main()
{
    int N, Q;
    std::cout << "Ingrese el numero de monedas diferentes: " << std::endl;
    std::cin >> N;
    std::vector<int> monedas(N);
    for (int i = 0; i < N; i++)
    {
        std::cout << "Valor " << i + 1 << ": ";
        std::cin >> monedas[i];
    }
    std::cout << "Cantidad de dinero a convertir: ";
    std::cin >> Q;

    std::sort(monedas.rbegin(), monedas.rend());
    cambioDynamic(monedas, Q, N);
    cambioGreedy(monedas, Q, N);
}
