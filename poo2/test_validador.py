import pytest
from validador import validar_contrasena

# Pruebas de cobertura de sentencias
def test_contrasena_demasiado_corta():
    """Prueba que verifica que una contraseña menor a 8 caracteres sea rechazada."""
    assert not validar_contrasena("Abc1!")

# Pruebas de cobertura de decisiones y condiciones
def test_contrasena_sin_mayuscula():
    """Prueba que verifica que una contraseña sin mayúscula sea rechazada."""
    assert not validar_contrasena("abcdefg1!")

def test_contrasena_sin_numero():
    """Prueba que verifica que una contraseña sin número sea rechazada."""
    assert not validar_contrasena("Abcdefgh!")

def test_contrasena_sin_caracter_especial():
    """Prueba que verifica que una contraseña sin carácter especial sea rechazada."""
    assert not validar_contrasena("Abcdefg123")

# Prueba de camino feliz
def test_contrasena_valida():
    """Prueba que verifica que una contraseña que cumple todos los requisitos sea aceptada."""
    assert validar_contrasena("Abc123!@")

# Pruebas de casos borde
def test_contrasena_longitud_exacta():
    """Prueba con una contraseña de exactamente 8 caracteres que cumple todos los requisitos."""
    assert validar_contrasena("Abc123!@")

def test_contrasena_solo_caracteres_validos():
    """Prueba con una contraseña que contiene exactamente una mayúscula, un número y un carácter especial."""
    assert validar_contrasena("Abcdefg1!")

# Pruebas adicionales para cubrir más caminos
def test_contrasena_todos_tipos_caracteres():
    """Prueba con una contraseña que contiene múltiples mayúsculas, números y caracteres especiales."""
    assert validar_contrasena("ABCdef123!@#")

def test_contrasena_caracteres_especiales_multiples():
    """Prueba con diferentes caracteres especiales permitidos."""
    assert validar_contrasena("Abcdef1!")
    assert validar_contrasena("Abcdef1@")
    assert validar_contrasena("Abcdef1#")
    assert validar_contrasena("Abcdef1$")
    assert validar_contrasena("Abcdef1%")
    assert validar_contrasena("Abcdef1^")
    assert validar_contrasena("Abcdef1&")
    assert validar_contrasena("Abcdef1*")