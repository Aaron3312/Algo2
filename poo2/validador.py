def validar_contrasena(contrasena):
    """
    Valida la fortaleza de una contraseña según los siguientes criterios:
    - Longitud mínima de 8 caracteres.
    - Debe contener al menos una letra mayúscula.
    - Debe contener al menos un número.
    - Debe contener al menos un carácter especial (!@#$%^&*).
    """

    longitud_minima = 8
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False

    if len(contrasena) < longitud_minima:
        return False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in "!@#$%^&*":
            tiene_especial = True

    if tiene_mayuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False