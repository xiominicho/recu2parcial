from archivos import cargar_inventario
from menu import menu_principal


inventario_sistema = cargar_inventario()

menu_principal(inventario_sistema)

