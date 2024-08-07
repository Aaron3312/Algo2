// actividad 1.1.b Utilizando el algoritmo std::sort
// Aaron Hernandez Jimenez A01642529
// Jorge Antonio Arizpe Cantu A01637441
// 07/08/2024
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Funcion para ordenar con el algorithm sort de la biblioteca estandar de C++ 

struct student {

  int age;

 string name;

};

int main() {
  // Crear un vector de estudiantes
  vector<student> students = {
    {20, "Juan"},
    {21, "Pedro"},
    {19, "Maria"},
    {22, "Ana"},
    {18, "Luis"}
  };

  // Ordenar el vector de estudiantes por edad en forma ascendente
  sort(students.begin(), students.end(), [](student a, student b) {
    return a.age < b.age;
  });

  // Imprimir el vector de estudiantes ordenado

  for (student s : students) {
    cout << s.age << " " << s.name << endl;
  }
  

  return 0;
}