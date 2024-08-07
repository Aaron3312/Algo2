// actividad 1.1.a Implementación de la técnica de programación "divide y vencerás"
// Aaron Hernandez Jimenez A01642529
// Jorge Antonio Arizpe Cantu A01637441
// 07/08/2024

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Función para mezclar dos subarreglos ordenados en uno
void merge(vector<double> &arr, int inicio, int mitad, int final)
{
    int i, j, k;
    int elementosIzquierda = mitad - inicio + 1;
    int elementosDerecha = final - mitad;

    // Usa vector<double> en lugar de vector<int>
    vector<double> izquierda(elementosIzquierda), derecha(elementosDerecha);

    // Copia los datos a los vectores temporales
    for (i = 0; i < elementosIzquierda; i++)
    {
        izquierda[i] = arr[inicio + i];
    }
    for (j = 0; j < elementosDerecha; j++)
    {
        derecha[j] = arr[mitad + 1 + j];
    }

    // Mezcla los vectores temporales de nuevo en arr[inicio..final]
    i = 0;
    j = 0;
    k = inicio;

    while (i < elementosIzquierda && j < elementosDerecha)
    {
        // Cambia la condición para ordenar de mayor a menor
        if (izquierda[i] >= derecha[j])
        {
            arr[k] = izquierda[i];
            i++;
        }
        else
        {
            arr[k] = derecha[j];
            j++;
        }
        k++;
    }

    // Copia los elementos restantes de izquierda[], si hay
    while (i < elementosIzquierda)
    {
        arr[k] = izquierda[i];
        i++;
        k++;
    }

    // Copia los elementos restantes de derecha[], si hay
    while (j < elementosDerecha)
    {
        arr[k] = derecha[j];
        j++;
        k++;
    }
}

// Función de ordenamiento por merge sort
void mergeSort(vector<double> &arr, int inicio, int final)
{
    if (inicio < final)
    {
        int mitad = inicio + (final - inicio) / 2;
        mergeSort(arr, inicio, mitad);
        mergeSort(arr, mitad + 1, final);
        merge(arr, inicio, mitad, final);
    }
}

// Función para imprimir el arreglo
void printArray(vector<double> &arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    // El programa recibe un número N seguido de N números reales
    int n;

    cout << "Ingrese el numero de elementos o 0 para salir: ";
    cin >> n;

    while (n > 0)
    {
        
        // Utiliza std::vector en lugar de un arreglo estático
        vector<double> arr(n);

        // Lee los elementos del vector
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        cout << "El arreglo ingresado es: ";
        printArray(arr, n);

        // Se ordena el arreglo de mayor a menor usando merge sort
        mergeSort(arr, 0, n - 1);

        // Imprime el arreglo ordenado
        cout << "El arreglo ordenado es: ";
        printArray(arr, n);
        
        cout << "Ingrese el numero de elementos o 0 para salir: ";
        cin >> n;
    }

    return 0;
}
