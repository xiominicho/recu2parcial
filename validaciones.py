def validar_texto_vacio(texto: str) -> bool:
    """
    Valida si una cadena de texto es correcta.
    Comprueba que la cadena no esté vacía, que no comience 
    ni termine con espacios en blanco y que no esté 
    compuesta únicamente por espacios.

    Args:
        texto (str): La cadena de caracteres que se desea evaluar.

    Returns:
        bool: True si el texto es válido y limpio. False si infringe alguna regla.
    """
    # Verifica si la cadena está completamente vacía de entrada
    if texto == "":
        return False
        
    # Verifica si el primer o el último carácter es un espacio
    if texto[0] == " " or texto[-1] == " ":
        return False
        
    # Verifica con un 'for' si son todos espacios en blanco
    letras_validas = 0
    for caracter in texto:
        if caracter != " ":
            letras_validas += 1
            
    if letras_validas == 0:
        return False
        
    return True


def validar_numero_positivo(cadena: str, de_tipo="int", permitir_cero=True) -> bool:
    """
    Verifica cadena de caracteres representa un número numérico válido.
    Analiza caracter por caracter que corresponda a dígitos entre '0' y '9' o puntos decimales 
    controlados.

    Args:
        cadena (str): El texto ingresado por el usuario que se desea validar.
        de_tipo (str, opcional): El tipo de dato esperado, puede ser "int" o "float". Por defecto es "int".
        permitir_cero (bool, opcional): Indica si el valor 0 se considera válido. Por defecto es True.

    Returns:
        bool: True si la conversión es segura y cumple los rangos. False en caso contrario.
    """
    # Validamos que no esté vacío ni tenga espacios tramposos usando nuestra función
    if validar_texto_vacio(cadena) == False:
        return False
        
    if cadena[0] == "." or cadena[-1] == ".":
        return False
        
    puntos_decimales = 0
    es_valido = True
    
    for caracter in cadena:
        if caracter == ".":
            if de_tipo == "int":
                es_valido = False
            puntos_decimales += 1
            if puntos_decimales > 1:
                es_valido = False
        elif caracter < "0" or caracter > "9":
            es_valido = False
            
    if es_valido == True:
        if de_tipo == "float":
            numero = float(cadena)
        else:
            numero = int(cadena)
            
        if permitir_cero == True and numero >= 0:
            return True
        elif permitir_cero == False and numero > 0:
            return True
            
    return False


def validar_codigo_unico(codigo: str, inventario: dict) -> bool:
    """
    Comprueba si el codigo ingresado ya existe.

    Args:
        codigo (str): La clave alfanumérica que se desea verificar.
        inventario (dict): El diccionario principal que contiene los productos en memoria.

    Returns:
        bool: True si el código está disponible (NO existe). False si el código ya está duplicado.
    """
    if codigo in inventario:
        return False
    return True



def pedir_codigo_valido(inventario: dict) -> str:
    """Insiste al usuario hasta obtener un código único y bien formateado."""
    codigo_valido = False
    codigo = ""
    while codigo_valido == False:
        codigo = input("Ingrese el código único del artículo: ") 
        
        if validar_texto_vacio(codigo) == False:
            print("⚠️ Error: El código no puede estar vacío ni contener espacios en los extremos.\n")
        elif codigo[0] == "." or codigo[-1] == ".":
            print("⚠️ Error: El código no puede empezar ni terminar con un punto (.).\n")
        elif validar_codigo_unico(codigo, inventario) == False:
            print(f"⚠️ Error: El código '{codigo}' YA EXISTE. Ingrese uno diferente.\n")
        else:
            codigo_valido = True
    return codigo


def pedir_texto_obligatorio(mensaje_input: str, mensaje_error: str) -> str:
    """Insiste al usuario hasta que ingrese un texto correcto."""
    valido = False
    texto = ""
    while valido == False:
        texto = input(mensaje_input) 
        if validar_texto_vacio(texto) == True:
            valido = True
        else:
            print(mensaje_error)
    return texto


def pedir_numero_valido(mensaje_input: str, mensaje_error: str, de_tipo="int", permitir_cero=True):
    """
    Insiste hasta que el usuario ingrese un número valido.

    Args:
        mensaje_input (str): Mensaje de solicitud de datos para la consola.
        mensaje_error (str): Mensaje de alerta en caso de ingresar caracteres inválidos o fuera de rango.
        de_tipo (str, opcional): Define el casteo final, permitiendo "int" o "float". Por defecto es "int".
        permitir_cero (bool, opcional): Dictamina si el valor numérico 0 aceptado. Por defecto es True.

    Returns:
        int | float: El valor numérico convertido y validado de manera segura según el tipo requerido.
    """
    valido = False
    valor_final = 0
    while valido == False:
        entrada_raw = input(mensaje_input)
        if validar_numero_positivo(entrada_raw, de_tipo, permitir_cero) == True:
            if de_tipo == "float":
                valor_final = float(entrada_raw)
            else:
                valor_final = int(entrada_raw)
            valido = True
        else:
            print(mensaje_error)
    return valor_final