def cantidad_total_productos(inventario: dict) -> int:
    """
    Cuenta y devuelve la cantidad total de unidades físicas en stock.
    """
    contador = 0
    for codigo in inventario:
        contador += 1
    return contador


def valor_total_inventario(inventario: dict) -> float:
    """
    Calcula y devuelve el valor monetario total de todos los productos acumulados.
    """
    total = 0.0
    for datos in inventario.values():
        total += (datos["precio"] * datos["stock"])
    return total


def precio_promedio_productos(inventario):
    """
    Calcula el precio promedio de los artículos cargados.
    """
    total_productos = cantidad_total_productos(inventario)
    if total_productos == 0:
        return 0.0
        
    suma_precios = 0.0
    for datos in inventario.values():
        suma_precios += datos["precio"]
    return suma_precios / total_productos


def producto_mas_caro(inventario):
    """
    Busca el producto con mayor precio.
    """
    if not inventario:
        return None
        
    es_primero = True
    cod_max = None
    precio_max = 0.0
    
    for codigo, datos in inventario.items():
        if es_primero or datos["precio"] > precio_max:
            precio_max = datos["precio"]
            cod_max = codigo
            es_primero = False
            
    return inventario[cod_max]["nombre"], precio_max


def producto_mayor_stock(inventario):
    """
    Busca el producto que tiene mayor cantidad de stock.
    """
    if not inventario:
        return None
        
    es_primero = True
    cod_max = None
    stock_max = -1
    
    for codigo, datos in inventario.items():
        if es_primero or datos["stock"] > stock_max:
            stock_max = datos["stock"]
            cod_max = codigo
            es_primero = False
            
    return inventario[cod_max]["nombre"], stock_max


def cantidad_productos_sin_stock(inventario) -> int:
    """
    Filtra, lista y cuenta cuántos productos están sin stock.
    """
    contador = 0
    for datos in inventario.values():
        if datos["stock"] == 0:
            contador += 1
    return contador


def cantidad_productos_stock_bajo(inventario) -> int:
    """
    Filtra, lista y cuenta cuántos productos están con stock bajo.
    """
    contador = 0
    for datos in inventario.values():
        if datos["alerta_stock"] == "Stock Bajo":
            contador += 1
    return contador


def cantidad_productos_por_categoria(inventario):
    """
    Agrupa y cuenta cuántos productos pertenecen a cada categoría existente.
    """
    conteo_categorias = {}
    for datos in inventario.values():
        cat = datos["categoria"]
        if cat not in conteo_categorias:
            conteo_categorias[cat] = 1
        else:
            conteo_categorias[cat] += 1
    return conteo_categorias


def porcentaje_productos_stock_bajo(inventario):
    """
    Calcula el porcentaje que representan los productos con stock bajo 
    respecto del total de productos cargados.
    """
    total = cantidad_total_productos(inventario)
    if total == 0:
        return 0.0
        
    bajo_stock = cantidad_productos_stock_bajo(inventario)
    return (bajo_stock / total) * 100


def mostrar_modulo_estadisticas(inventario):
    """
    Muestra el menú de reportes en pantalla. No devuelve ningún valor.
    """
    print("\n=================================== PANEL DE ESTADÍSTICAS ===================================")
    if not inventario:
        print("El inventario está vacío. No se pueden calcular estadísticas.")
        print("=============================================================================================")
        return

    # 1. Cantidad total
    print(f" • Cantidad total de productos: {cantidad_total_productos(inventario)}")
    
    # 2. Valor total
    print(f" • Valor total del inventario: ${valor_total_inventario(inventario):,.2f}")
    
    # 3. Precio promedio
    print(f" • Precio promedio de los productos: ${precio_promedio_productos(inventario):.2f}")
    
    # 4. Más caro
    nom_caro, pre_caro = producto_mas_caro(inventario)
    print(f" • Producto más caro: {nom_caro} (${pre_caro:.2f})")
    
    # 5. Mayor cantidad stock
    nom_stock, cant_stock = producto_mayor_stock(inventario)
    print(f" • Producto con mayor cantidad de stock: {nom_stock} ({cant_stock} unidades)")
    
    # 6. Sin stock
    print(f" • Cantidad de productos sin stock: {cantidad_productos_sin_stock(inventario)}")
    
    # 7. Stock bajo
    print(f" • Cantidad de productos con stock bajo: {cantidad_productos_stock_bajo(inventario)}")
    
    # 8. Cantidad por categoría
    print(" • Cantidad de productos por categoría:")
    categorias_dicc = cantidad_productos_por_categoria(inventario)
    for cat, cantidad in categorias_dicc.items():
        print(f"    - {cat}: {cantidad}")
        
    # 9. Porcentaje stock bajo
    print(f" • Porcentaje de productos con stock bajo respecto del total: {porcentaje_productos_stock_bajo(inventario)}%")
    
    print("=============================================================================================")