from productos import (
    alta_producto, 
    listar_productos, 
    consultar_producto, 
    buscar_producto_por_categoria,
    modificar_producto_completo, 
    dar_baja_producto
)
from estadisticas import mostrar_modulo_estadisticas

def menu_principal(inventario):
    """
    Muestra el menú principal y ejecuta la opción seleccionada por el usuario.
    """
    continuar = True
    
    while continuar == True:
        print("\n=======================================================")
        print("   SISTEMA DE GESTIÓN DE INVENTARIO   ")
        print("=======================================================")
        print("1. Registrar productos")
        print("2. Listar productos")
        print("3. Buscar producto por código")
        print("4. Buscar producto por categoría")
        print("5. Modificar producto")
        print("6. Eliminar producto del inventario")
        print("7. Estadísticas")
        print("8. Guardar y salir")
        print("=======================================================")
        
        opcion = input("Seleccione una opción (1-8): ")
        
        # Evaluamos directamente la variable opcion
        match opcion:
            case "1":
                alta_producto(inventario)
            case "2":
                listar_productos(inventario)
            case "3":
                consultar_producto(inventario)
            case "4":
                buscar_producto_por_categoria(inventario)
            case "5":
                print("\n--- Modificar Producto ---")
                codigo = input("Ingrese el código del producto a modificar: ")
                if codigo in inventario:
                    modificar_producto_completo(inventario)
                else:
                    print("⚠️ Error: El código no existe.")
            case "6":
                dar_baja_producto(inventario)
            case "7":
                mostrar_modulo_estadisticas(inventario)
            case "8":
                print("\n¡Muchas gracias por utilizar el sistema! Saliendo de forma segura...")
                continuar = False
            case _:  # El guion bajo funciona como el "else" (opción por defecto)
                print("⚠️ Opción inválida. Por favor, ingrese un número del 1 al 8.")