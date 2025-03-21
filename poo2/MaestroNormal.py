from abc import ABC, abstractmethod
from typing import List

class IProfesor(ABC):
    def __init__(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad
    
    @abstractmethod
    def teach_method(self) -> str:
        pass

class ProfesorMatematicas(IProfesor):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Matemáticas")
        self.usa_calculadora = True
    
    def teach_method(self) -> str:
        return f"{self.nombre} enseña matemáticas usando ejercicios prácticos y resolución de problemas"

class ProfesorHistoria(IProfesor):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Historia")
        self.periodo_especialidad = "Moderna"
    
    def teach_method(self) -> str:
        return f"{self.nombre} enseña historia a través de narrativas y análisis de eventos históricos"

class ProfesorIngles(IProfesor):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Inglés")
        self.nivel_cambridge = "C1"
    
    def teach_method(self) -> str:
        return f"{self.nombre} enseña inglés usando el método comunicativo y prácticas conversacionales"

class Escuela(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.profesores: List[IProfesor] = []

    def get_profesor(self, especialidad: str) -> IProfesor:
        for profesor in self.profesores:
            if profesor.especialidad.lower() == especialidad.lower():
                return profesor
        return None

    @abstractmethod
    def teach_method(self) -> str:
        pass

class EscuelaPublica(Escuela):
    def __init__(self, nombre: str, fondos_gubernamentales: float):
        super().__init__(nombre)
        self.fondos_gubernamentales = fondos_gubernamentales

    def teach_method(self) -> str:
        return "Método de enseñanza público estandarizado"

    def solicitar_recursos(self) -> str:
        return f"Solicitando recursos adicionales. Fondos actuales: {self.fondos_gubernamentales}"

class EscuelaPrivada(Escuela):
    def __init__(self, nombre: str, cuota_mensual: float):
        super().__init__(nombre)
        self.cuota_mensual = cuota_mensual

    def teach_method(self) -> str:
        return "Método de enseñanza personalizado con grupos reducidos"

    def cobrar_cuotas(self) -> float:
        return self.cuota_mensual * len(self.profesores)

def main():
    # Crear profesores
    prof_mate = ProfesorMatematicas("Juan Pérez")
    prof_historia = ProfesorHistoria("María García")
    prof_ingles = ProfesorIngles("John Smith")

    # Crear escuelas
    escuela_publica = EscuelaPublica("Escuela Pública #123", 100000.0)
    escuela_privada = EscuelaPrivada("Colegio Privado ABC", 500.0)

    # Asignar profesores a escuelas
    escuela_publica.profesores.extend([prof_mate, prof_historia])
    escuela_privada.profesores.extend([prof_ingles, ProfesorMatematicas("Ana López")])

    # Demostrar funcionalidad
    print("\n=== Escuela Pública ===")
    print(f"Nombre: {escuela_publica.nombre}")
    print(f"Método de enseñanza: {escuela_publica.teach_method()}")
    print(f"Recursos: {escuela_publica.solicitar_recursos()}")
    
    # Mostrar métodos de enseñanza de los profesores
    for profesor in escuela_publica.profesores:
        print(profesor.teach_method())

    print("\n=== Escuela Privada ===")
    print(f"Nombre: {escuela_privada.nombre}")
    print(f"Método de enseñanza: {escuela_privada.teach_method()}")
    print(f"Ingresos por cuotas: ${escuela_privada.cobrar_cuotas()}")
    
    # Buscar profesor por especialidad
    profesor_mate = escuela_privada.get_profesor("matemáticas")
    if profesor_mate:
        print(f"Profesor encontrado: {profesor_mate.nombre}")
        print(profesor_mate.teach_method())

if __name__ == "__main__":
    main()