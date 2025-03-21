from abc import ABC, abstractmethod
from typing import List

class Maestro(ABC):
    def __init__(self, nombre: str, edad: int, anos_experiencia: int):
        self.nombre = nombre
        self.edad = edad
        self.anos_experiencia = anos_experiencia
        self.estudiantes = []

    @abstractmethod
    def ensenar_tecnica_especial(self) -> str:
        pass

    @abstractmethod
    def meditar(self) -> str:
        pass

    def aceptar_estudiante(self, estudiante: str) -> None:
        self.estudiantes.append(estudiante)
        print(f"{self.nombre} ha aceptado a {estudiante} como discípulo")

    def mostrar_informacion(self) -> str:
        return f"Maestro {self.nombre}, {self.edad} años, {self.anos_experiencia} años de experiencia"

class MaestroKungFu(Maestro):
    def __init__(self, nombre: str, edad: int, anos_experiencia: int, estilo: str):
        super().__init__(nombre, edad, anos_experiencia)
        self.estilo = estilo

    def ensenar_tecnica_especial(self) -> str:
        return f"El Maestro {self.nombre} enseña la técnica secreta del {self.estilo}: Puño del Dragón"

    def meditar(self) -> str:
        return f"El Maestro {self.nombre} medita en posición de loto bajo una cascada"

class MaestroTaiChi(Maestro):
    def __init__(self, nombre: str, edad: int, anos_experiencia: int, forma_preferida: str):
        super().__init__(nombre, edad, anos_experiencia)
        self.forma_preferida = forma_preferida

    def ensenar_tecnica_especial(self) -> str:
        return f"El Maestro {self.nombre} enseña la forma ancestral: {self.forma_preferida}"

    def meditar(self) -> str:
        return f"El Maestro {self.nombre} practica la respiración del dragón en el jardín zen"

class MaestroAikido(Maestro):
    def __init__(self, nombre: str, edad: int, anos_experiencia: int, rango_dan: int):
        super().__init__(nombre, edad, anos_experiencia)
        self.rango_dan = rango_dan

    def ensenar_tecnica_especial(self) -> str:
        return f"El Maestro {self.nombre} enseña la técnica de redirección de energía nivel {self.rango_dan}"

    def meditar(self) -> str:
        return f"El Maestro {self.nombre} medita mientras practica caligrafía japonesa"

class EscuelaTradicional:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.maestros: List[Maestro] = []

    def agregar_maestro(self, maestro: Maestro) -> None:
        self.maestros.append(maestro)
        print(f"El {maestro.mostrar_informacion()} se ha unido a {self.nombre}")

    def mostrar_enseñanzas(self) -> None:
        print(f"\nEnseñanzas en {self.nombre}:")
        for maestro in self.maestros:
            print(f"\n{maestro.mostrar_informacion()}")
            print(maestro.ensenar_tecnica_especial())
            print(maestro.meditar())

def main():
    escuela = EscuelaTradicional("Escuela de Artes Marciales Ancestrales")
    
    # Crear diferentes tipos de maestros
    maestro_kung_fu = MaestroKungFu("Li Wei", 65, 40, "Estilo del Tigre")
    maestro_tai_chi = MaestroTaiChi("Chen Xiaowang", 70, 45, "Forma Yang de 108 Movimientos")
    maestro_aikido = MaestroAikido("Hiroshi Tanaka", 55, 30, 7)

    # Agregar maestros a la escuela
    escuela.agregar_maestro(maestro_kung_fu)
    escuela.agregar_maestro(maestro_tai_chi)
    escuela.agregar_maestro(maestro_aikido)

    # Aceptar estudiantes
    maestro_kung_fu.aceptar_estudiante("Juan Pérez")
    maestro_tai_chi.aceptar_estudiante("María García")
    maestro_aikido.aceptar_estudiante("Carlos López")

    # Mostrar todas las enseñanzas
    escuela.mostrar_enseñanzas()

if __name__ == '__main__':
    main()