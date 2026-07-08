
from validaciones import pedir_codigo_valido, pedir_texto_obligatorio, pedir_numero_valido, validar_numero_positivo, validar_texto_vacio
from archivos import guardar_inventario


def calcular_alerta_stock(stock_actual, stock_minimo) -> str:
    """
    Compara el stock actual con el mínimo y devuelve el estado del producto.
    """
    actual = int(stock_actual)
    minimo = int(stock_minimo)
    if actual == 0:
        return "Sin Stock"
    elif actual <= minimo:
        return "Stock Bajo"
    else:
        return "Stock Normal"


def alta_producto(inventario: dict) -> None:
    """
    Pide los datos de un nuevo producto, los valida y los guarda.
    """
    print("\n--- Registrar Producto ---")
    
    codigo = pedir_codigo_valido(inventario)
    
    nombre = pedir_texto_obligatorio(
        "Ingrese el nombre del producto: ", 
        "⚠️ Error: El nombre no puede estar vacío."
    )
    
    categoria = pedir_texto_obligatorio(
        "Ingrese la categoría: ", 
        "⚠️ Error: La categoría no puede estar vacía."
    )
    
    precio = pedir_numero_valido(
        "Ingrese el precio unitario: ", 
        "⚠️ Error: El precio debe ser un número mayor a cero.",
        de_tipo="float", permitir_cero=False
    )
    
    stock = pedir_numero_valido(
        "Ingrese el stock disponible: ", 
        "⚠️ Error: El stock debe ser un número entero mayor o igual a cero.",
        de_tipo="int", permitir_cero=True
    )
    
    stock_minimo = pedir_numero_valido(
        "Ingrese el stock mínimo: ", 
        "⚠️ Error: El stock mínimo debe ser mayor o igual a cero.",
        de_tipo="int", permitir_cero=True
    )
    
    proveedor = pedir_texto_obligatorio(
        "Ingrese el nombre del proveedor: ", 
        "⚠️ Error: El proveedor no puede estar vacío."
    )

    # Procesamiento y guardado
    alerta = calcular_alerta_stock(stock, stock_minimo)

    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor,
        "alerta_stock": alerta
    }

    if guardar_inventario(inventario) == True:
        print(f"\n✅ ¡Producto '{nombre}' registrado con éxito!")

def listar_productos(inventario: dict) -> None:
    """
    Opción 2: Recorre el inventario y muestra todos los productos en pantalla.
    """
    print("\n=======================================================")
    print("   LISTADO DE PRODUCTOS  ")
    print("=======================================================")
    if not inventario:
        print("El inventario está completamente vacío.")
        print("=======================================================")
        return
        
    for codigo, p in inventario.items():
        print(f"Código: {codigo}")
        print(f"Nombre: {p['nombre']}")
        print(f"Categoría: {p['categoria']}")
        print(f"Precio: ${p['precio']:,.2f}")
        print(f"Stock: {p['stock']}")
        print(f"Stock mínimo: {p['stock_minimo']}")
        print(f"Proveedor: {p['proveedor']}")
        print(f"Estado: {p['alerta_stock']}")
        print("-" * 30)
    print("=======================================================")


def consultar_producto(inventario: dict) -> None:
    """
    Realiza una consulta directa y exacta de un artículo por su clave única.
    
    Solicita el código por consola al usuario y, si existe como clave en el diccionario, 
    despliega en pantalla el desglose ordenado de todos sus campos técnicos.

    Args:
        inventario (dict): El diccionario que contiene el stock de productos del sistema.
    """
    print("\n--- Buscar producto por código ---")
    codigo = input("Ingrese el código del producto a buscar: ") 
    
    if codigo in inventario:
        p = inventario[codigo]
        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {p['nombre']}")
        print(f"Categoría: {p['categoria']}")
        print(f"Precio: ${p['precio']:,.2f}")
        print(f"Stock: {p['stock']}")
        print(f"Stock mínimo: {p['stock_minimo']}")
        print(f"Proveedor: {p['proveedor']}")
        print(f"Estado: {p['alerta_stock']}")
    else:
        print("⚠️ Error: El código de producto no existe.")


def buscar_producto_por_categoria(inventario: dict) -> None:
    """
    Filtra y lista en pantalla los productos pertenecientes a un mismo rubro.
    
    Implementa un recorrido clásico sobre los ítems del inventario haciendo una 
    comparación exacta de cadenas para identificar coincidencias lógicas.

    Args:
        inventario (dict): El diccionario que contiene el stock de productos del sistema.
    """
    print("\n--- Buscar producto por categoría ---")
    categoria_buscar = input("Ingrese la categoría a consultar: ")
    
    hubo_coincidencias = False
    
    for codigo, p in inventario.items():
        if p["categoria"] == categoria_buscar:
            if hubo_coincidencias == False:
                print("\nProductos encontrados:")
                print("-" * 30)
            print(f"Código: {codigo} | Nombre: {p['nombre']} | Stock: {p['stock']} | Estado: {p['alerta_stock']}")
            hubo_coincidencias = True
            
    if hubo_coincidencias == False:
        print(f"⚠️ No existen productos registrados exactamente para la categoría '{categoria_buscar}'.")

def modificar_producto_completo(inventario: dict) -> None:
    """
    Modifica los atributos de un producto existente.
    
    Presenta un menú interno de opciones del 1 al 6. Captura y valida de forma interactiva 
    el nuevo dato ingresado mediante funciones de persistencia obligatoria y actualiza 
    los estados de alerta antes de impactar el cambio de forma automática en el disco JSON.

    Args:
        inventario (dict): El diccionario que contiene el stock de productos en memoria.
    """
    from validaciones import pedir_texto_obligatorio, pedir_numero_valido
    
    print("\n--- Modificar Producto ---")
    codigo = input("Ingrese el código del producto a modificar: ") 
    
    if (codigo in inventario) == False:
        print("⚠️ Error: El código no existe.")
        return
        
    p = inventario[codigo]
    print(f"\nProducto seleccionado: {p['nombre']}")
    print("1. Modificar Nombre")
    print("2. Modificar Categoría")
    print("3. Modificar Precio")
    print("4. Modificar Stock")
    print("5. Modificar Stock Mínimo")
    print("6. Modificar Proveedor")
    
    opcion = input("Seleccione qué campo desea modificar (1-6): ")  
    
    if opcion == "1":
        nuevo = pedir_texto_obligatorio("Ingrese el nuevo nombre: ", "⚠️ Error: Nombre inválido.\n")
        p["nombre"] = nuevo
        print("Nombre modificado.")
        
    elif opcion == "2":
        nuevo = pedir_texto_obligatorio("Ingrese la nueva categoría: ", "⚠️ Error: Categoría inválida.\n")
        p["categoria"] = nuevo
        print("Categoría modificada.")
        
    elif opcion == "3":
        nuevo = pedir_numero_valido("Ingrese el nuevo precio: ", "⚠️ Error: Precio inválido.\n", de_tipo="float", permitir_cero=False)
        p["precio"] = nuevo
        print("Precio modificado.")
        
    elif opcion == "4":
        nuevo = pedir_numero_valido("Ingrese el nuevo stock: ", "⚠️ Error: Stock inválido.\n", de_tipo="int", permitir_cero=True)
        p["stock"] = nuevo
        p["alerta_stock"] = calcular_alerta_stock(p["stock"], p["stock_minimo"])
        print("Stock y estado actualizados.")
        
    elif opcion == "5":
        nuevo = pedir_numero_valido("Ingrese el nuevo stock mínimo: ", "⚠️ Error: Stock mínimo inválido.\n", de_tipo="int", permitir_cero=True)
        p["stock_minimo"] = nuevo
        p["alerta_stock"] = calcular_alerta_stock(p["stock"], p["stock_minimo"])
        print("Stock mínimo y estado actualizados.")
        
    elif opcion == "6":
        nuevo = pedir_texto_obligatorio("Ingrese el nuevo proveedor: ", "⚠️ Error: Proveedor inválido.\n")
        p["proveedor"] = nuevo
        print("Proveedor modificado.")
    else:
        print("⚠️ Opción incorrecta.")
        return

    # Si se realizó un cambio válido, se persiste automáticamente en el JSON
    guardar_inventario(inventario)


def dar_baja_producto(inventario):
    """
    Elimina un producto por su código único.
    """
    print("\n--- Eliminar Producto del Inventario ---")
    codigo = input("Ingrese el código del producto a eliminar: ") 
    
    if codigo in inventario:
        nombre_eliminado = inventario[codigo]["nombre"]
        
        # Pedimos confirmación
        print(f"\n⚠️ ¿Está seguro que desea eliminar '{nombre_eliminado}' permanentemente?")
        confirmacion = input("Escriba 'Si' para confirmar o cualquier otra tecla para cancelar: ")
        
        if confirmacion == "Si" or confirmacion == "si":
            del inventario[codigo]
            guardar_inventario(inventario)
            print(f"✅ El producto '{nombre_eliminado}' fue eliminado con éxito.")
        else:
            print("❌ Eliminación cancelada. El producto sigue en el inventario.")
            
    else:
        print("⚠️ Error: El código de producto no existe.")