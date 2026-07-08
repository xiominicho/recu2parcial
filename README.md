✒️ Autor
Xiomara Nicho 

Proyecto desarrollado para la cátedra de Programación - UTN.




# Sistema de Gestión de Inventario

Un sistema modular desarrollado en Python para la administración, control y seguimiento de stock de productos, diseñado bajo criterios lógicos estrictos y persistencia de datos en formato JSON.

---

## 🚀 Características Principales

* **Estructura Modular:** Código organizado de forma limpia en módulos independientes (`menu.py`, `productos.py`, `validaciones.py`, `archivos.py`, `estadisticas.py`).
* **Validaciones Robustas:** Control exhaustivo de ingreso de datos sin funciones integradas automáticas (`.strip()` o `.lower()`), priorizando el desarrollo de algoritmos de validación manuales y estructuras cíclicas de persistencia.
* **Persistencia Local:** Los datos se leen y guardan automáticamente en un archivo `inventario.json`.
* **Alertas Inteligentes:** Control automático del estado de stock en base a los límites mínimos configurados ("Sin Stock", "Stock Bajo", "Stock Normal").

---

## 🛠️ Estructura del Proyecto

* **`main.py`**: Punto de entrada del programa.
* **`menu.py`**: Interfaz de consola interactiva con bucles controlados por banderas booleanas y estructuras `match-case`.
* **`productos.py`**: Lógica de negocio (Alta, consulta, listado, modificación controlada y baja con confirmación).
* **`validaciones.py`**: Motor de control e interacción que blinda las entradas de datos del usuario.
* **`archivos.py`**: Control de lectura y escritura del archivo JSON.
* **`estadisticas.py`**: Módulo de reportes numéricos y cálculos analíticos de stock.

---

## 💻 Requisitos e Instalación

Para ejecutar este sistema solo necesitas tener instalado **Python 3.10** o superior (debido al uso de estructuras `match-case`).

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener el archivo `inventario.json` en la misma raíz.
3. Ejecuta el programa desde la terminal con:
   ```bash
   python main.py