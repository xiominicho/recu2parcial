import json


def cargar_inventario(nombre_archivo="inventario.json") -> dict:
    """
    Realiza la lectura e inserción en memoria del archivo de persistencia de datos.

    Args:
        nombre_archivo (str, opcional): Ruta física del archivo en disco. Por defecto es "inventario.json".

    Returns:
        dict: Diccionario con los productos cargados en memoria bajo la clave "inventario".
    """
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return data["inventario"]  

def guardar_inventario(inventario: dict, nombre_archivo="inventario.json") -> bool:
    """
    Persiste de forma estructurada el estado actual del inventario en el disco.

    Args:
        inventario (dict): Diccionario actual de productos en memoria.
        nombre_archivo (str, opcional): Ruta física del archivo de destino. Por defecto es "inventario.json".

    Returns:
        bool: True si la escritura en el disco se completó correctamente.
    """
    estructura_a_guardar = {"inventario": inventario}
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(estructura_a_guardar, archivo, indent=4, ensure_ascii=False)
    return True