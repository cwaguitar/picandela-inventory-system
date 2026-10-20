import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Esto detecta automáticamente la carpeta donde está este archivo y le pega el nombre de la BD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "picandela.db")

def generar_grafico_precios():
    # 1. Conectar a la base de datos usando la ruta fija y segura
    conexion = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT NOMBRE, PRECIO FROM productos", conexion)
    conexion.close()

    # 2. Crear un gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.bar(df['NOMBRE'], df['PRECIO'], color='lightgreen', edgecolor='black')

    # 3. Personalizar el gráfico con etiquetas y título
    plt.title('Precios de Productos - Picandela', fontsize=14, fontweight='bold')
    plt.xlabel('Productos', fontsize=12)
    plt.ylabel('Precio ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. AGREGAR VALORES EXACTOS ARRIBA DE CADA BARRA
    for barra in barras:
        altura = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 1500,
            f'${int(altura):,}',
            ha='center', 
            va='bottom',
            fontsize=10,
            fontweight='bold'
        )

    # 5. GUARDAR EL GRÁFICO AUTOMÁTICAMENTE COMO IMAGEN
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_DIR, "grafico_precios_picandela.png"), dpi=300)
    print("¡Gráfico guardado exitosamente!")

    # 6. Mostrar el gráfico en pantalla
    plt.show()

if __name__ == "__main__":
    generar_grafico_precios()

