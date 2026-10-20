import sqlite3
import pandas as pd
import os

def analisis_picandela():
            
            # 1. Conectarnos a la base de datos usando la misma ruta blindada
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "picandela.db")

            print("Conectando a la base de datos de Picandela...\n")
            conexion = sqlite3.connect(db_path)

            # 2. Cargar los datos de la tabla 'productos' directamente en un DataFrame de Pandas
            df = pd.read_sql_query("SELECT * FROM productos", conexion)
            conexion.close()

            # 3. Validar si hay datos
            if df.empty:
                print("⚠️ La base de datos está vacía. Agrega productos primero.")
            else:
                print(f"✅ ¡Datos cargados con éxito! Total de registros: {len(df)}\n")
                
                # --- CALCULANDO MÉTRICAS DE NEGOCIO ---
                
                total_productos = len(df)
                precio_promedio = df['PRECIO'].mean()
                producto_mas_caro = df.loc[df['PRECIO'].idxmax()]
                producto_mas_barato = df.loc[df['PRECIO'].idxmin()]
            
                # Suma  del valor nominal de los precios registrados:
                valor_total_precios = df['PRECIO'].sum()

                print("📈 --- REPORTE DE ANÁLISIS DE INVENTARIO ---")
                print(f"• Total de productos únicos: {total_productos}")
                print(f"• Precio promedio de los productos: ${precio_promedio:,.2f}")
                print(f"• Producto más caro: {producto_mas_caro['NOMBRE']} (${producto_mas_caro['PRECIO']})")
                print(f"• Producto más barato: {producto_mas_barato['NOMBRE']} (${producto_mas_barato['PRECIO']})")
                print(f"• Sumatoria total de precios: ${valor_total_precios:,.2f}")
                
                print("\n--- VISTA PREVIA DE LOS DATOS ---")
                print(df.head(10)) # Muestra los primeros 10 productos en formato de tabla limpia
