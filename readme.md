# 🌶️ Picandela - Sistema de Gestión y Análisis de Inventario

Proyecto modular desarrollado en Python orientado al análisis de datos y la gestión persistente de inventarios mediante una interfaz de consola (CLI).

## 🚀 Tecnologías utilizadas
* **Python 3.x**
* **Pandas**: Procesamiento y análisis de datos.
* **SQLite3**: Persistencia de datos con rutas seguras (`os.path`).
* **Matplotlib**: Visualización gráfica automatizada de precios.

## 🛠️ Arquitectura del Proyecto
El proyecto sigue un diseño modular y estructurado:
- `main.py`: Capa de Interfaz de Usuario (UI) y centro de control del menú interactivo.
- `graficos.py`: Módulo de visualización que extrae datos de la base, genera gráficos personalizados y los exporta a `.png`.
- `analisis.py`: Módulo de estadísticas y métricas de negocio.
- `picandela.db`: Base de datos SQLite integrada.

## 📋 ¿Cómo ejecutar el proyecto?
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instaladas las librerías necesarias:
   ```bash
   pip install pandas matplotlib