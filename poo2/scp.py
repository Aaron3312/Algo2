from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional
from datetime import datetime

class ClasificacionSCP(Enum):
    SAFE = "Safe"
    EUCLID = "Euclid"
    KETER = "Keter"
    THAUMIEL = "Thaumiel"
    NEUTRALIZED = "Neutralized"

class NivelAutorizacion(Enum):
    NIVEL_0 = "Nivel 0 - Público"
    NIVEL_1 = "Nivel 1 - Confidencial"
    NIVEL_2 = "Nivel 2 - Restringido"
    NIVEL_3 = "Nivel 3 - Secreto"
    NIVEL_4 = "Nivel 4 - Top Secret"
    NIVEL_5 = "Nivel 5 - Thaumiel"

class SCP(ABC):
    def __init__(self, 
                 numero: int, 
                 clasificacion: ClasificacionSCP,
                 nivel_autorizacion: NivelAutorizacion,
                 descripcion: str):
        self.numero = numero
        self.clasificacion = clasificacion
        self.nivel_autorizacion = nivel_autorizacion
        self.descripcion = descripcion
        self.registro_incidentes = []
        self.fecha_contencion = datetime.now()

    @abstractmethod
    def procedimiento_contencion(self) -> str:
        pass

    @abstractmethod
    def manifestar_anomalia(self) -> str:
        pass

    def registrar_incidente(self, incidente: str) -> None:
        fecha = datetime.now()
        self.registro_incidentes.append(f"[{fecha}] {incidente}")

    def mostrar_informacion(self) -> str:
        return f"""
        SCP-{self.numero:03d}
        Clasificación: {self.clasificacion.value}
        Nivel de Autorización: {self.nivel_autorizacion.value}
        Descripción: {self.descripcion}
        Fecha de Contención: {self.fecha_contencion}
        """

class SCPHumanoide(SCP):
    def __init__(self, 
                 numero: int,
                 clasificacion: ClasificacionSCP,
                 nivel_autorizacion: NivelAutorizacion,
                 descripcion: str,
                 capacidad_cognitiva: bool,
                 nivel_peligrosidad: int):
        super().__init__(numero, clasificacion, nivel_autorizacion, descripcion)
        self.capacidad_cognitiva = capacidad_cognitiva
        self.nivel_peligrosidad = nivel_peligrosidad
        self.estado_psicologico = []

    def procedimiento_contencion(self) -> str:
        base = f"SCP-{self.numero:03d} debe ser contenido en una celda estándar humanoidea"
        if self.nivel_peligrosidad > 7:
            base += " reforzada con acero de 30cm y campos electromagnéticos"
        if self.capacidad_cognitiva:
            base += ". Se permite acceso a material de lectura preaprobado"
        return base

    def manifestar_anomalia(self) -> str:
        return f"SCP-{self.numero:03d} ha manifestado comportamiento anómalo nivel {self.nivel_peligrosidad}"

    def evaluar_psicologicamente(self, evaluacion: str) -> None:
        self.estado_psicologico.append(evaluacion)

class SCPObjeto(SCP):
    def __init__(self,
                 numero: int,
                 clasificacion: ClasificacionSCP,
                 nivel_autorizacion: NivelAutorizacion,
                 descripcion: str,
                 es_movil: bool,
                 radiacion: bool):
        super().__init__(numero, clasificacion, nivel_autorizacion, descripcion)
        self.es_movil = es_movil
        self.radiacion = radiacion
        self.mediciones = []

    def procedimiento_contencion(self) -> str:
        contencion = f"SCP-{self.numero:03d} debe ser almacenado en una caja fuerte de acero"
        if self.radiacion:
            contencion += " con recubrimiento de plomo y monitores de radiación"
        if self.es_movil:
            contencion += " y asegurado con múltiples cerraduras electromagnéticas"
        return contencion

    def manifestar_anomalia(self) -> str:
        if self.es_movil:
            return f"SCP-{self.numero:03d} ha intentado desplazarse de su contención"
        return f"SCP-{self.numero:03d} ha manifestado propiedades anómalas estáticas"

    def registrar_medicion(self, medicion: float, tipo: str) -> None:
        self.mediciones.append((datetime.now(), medicion, tipo))

class SCPLugar(SCP):
    def __init__(self,
                 numero: int,
                 clasificacion: ClasificacionSCP,
                 nivel_autorizacion: NivelAutorizacion,
                 descripcion: str,
                 area: float,
                 tiene_portal: bool):
        super().__init__(numero, clasificacion, nivel_autorizacion, descripcion)
        self.area = area
        self.tiene_portal = tiene_portal
        self.anomalias_espaciales = []

    def procedimiento_contencion(self) -> str:
        contencion = f"SCP-{self.numero:03d} debe ser rodeado por un perímetro de seguridad de {self.area * 2}m²"
        if self.tiene_portal:
            contencion += " y monitoreado constantemente por sensores de actividad dimensional"
        return contencion

    def manifestar_anomalia(self) -> str:
        return f"SCP-{self.numero:03d} ha presentado alteraciones en su geometría espacial"

    def registrar_anomalia_espacial(self, anomalia: str) -> None:
        self.anomalias_espaciales.append((datetime.now(), anomalia))

class Fundacion:
    def __init__(self):
        self.scps: List[SCP] = []
        self.personal_autorizado = set()

    def agregar_scp(self, scp: SCP) -> None:
        self.scps.append(scp)
        print(f"SCP-{scp.numero:03d} ha sido registrado en la base de datos")

    def revisar_contenciones(self) -> None:
        print("\nEstado de contenciones:")
        for scp in self.scps:
            print(f"\nSCP-{scp.numero:03d}:")
            print(f"Procedimiento: {scp.procedimiento_contencion()}")

    def reportar_anomalias(self) -> None:
        print("\nReporte de anomalías:")
        for scp in self.scps:
            print(f"\nSCP-{scp.numero:03d}:")
            print(scp.manifestar_anomalia())

def main():
    fundacion = Fundacion()

    # Crear diferentes tipos de SCPs
    scp_049 = SCPHumanoide(
        numero=49,
        clasificacion=ClasificacionSCP.EUCLID,
        nivel_autorizacion=NivelAutorizacion.NIVEL_3,
        descripcion="El Doctor Plaga",
        capacidad_cognitiva=True,
        nivel_peligrosidad=8
    )

    scp_714 = SCPObjeto(
        numero=714,
        clasificacion=ClasificacionSCP.SAFE,
        nivel_autorizacion=NivelAutorizacion.NIVEL_2,
        descripcion="El Anillo Jade",
        es_movil=False,
        radiacion=False
    )

    scp_3008 = SCPLugar(
        numero=3008,
        clasificacion=ClasificacionSCP.EUCLID,
        nivel_autorizacion=NivelAutorizacion.NIVEL_4,
        descripcion="Una IKEA Infinita",
        area=1000.0,
        tiene_portal=True
    )

    # Registrar SCPs
    fundacion.agregar_scp(scp_049)
    fundacion.agregar_scp(scp_714)
    fundacion.agregar_scp(scp_3008)

    # Registrar algunos incidentes
    scp_049.registrar_incidente("Intento de cura en D-Class personal")
    scp_714.registrar_medicion(0.3, "Energía residual")
    scp_3008.registrar_anomalia_espacial("Expansión repentina del área comercial")

    # Revisar contenciones y anomalías
    fundacion.revisar_contenciones()
    fundacion.reportar_anomalias()

if __name__ == '__main__':
    main()