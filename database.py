import sqlite3
import os

# Obtenemos la ruta absoluta de la carpeta donde vive este archivo database.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class miTequeBase:
    def __init__(self, db_name="picandela.db"):
        # Unimos la ruta de la carpeta con el nombre de la base de datos
        self.db_path = os.path.join(BASE_DIR, db_name)
        self.createTable() # Llamamos a la creación de la tabla automáticamente al iniciar

    def conectar(self):
        # Usamos siempre la ruta principal:
        return sqlite3.connect(self.db_path)

    def createTable(self):  # CREAMOS LA TABLA
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE TEXT NOT NULL,
                PRECIO INTEGER NOT NULL
            )
        """)
        
        conexion.commit()
        conexion.close()
    
    # ACA INSERTAMOS EL NOMBRE Y EL PRECIO SERIAN LOS NOMBRES DE LAS COLUMNAS PRINCIPALES DE LA TABLA:

    def insertRow(self, nombre, precio):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (NOMBRE, PRECIO) VALUES (?, ?)", (nombre, precio))
        conexion.commit()
        conexion.close()

    # ACA ABAJO LEEMOS QUE CONTIENE LA TABLA ENTERA, COMO LA VAMOS A TRAER HACEMOS FETCHALL:


    def readRow(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        conexion.close()
        return datos

    # ACA ABAJO ACTUALIZAMOS EL CAMPO DE LA TABLA QUE DESEEMOS:

    def updateFields(self, precio_nuevo, nombre_nuevo):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET PRECIO = ? WHERE NOMBRE = ? COLLATE NOCASE", (precio_nuevo, nombre_nuevo),)
        conexion.commit()
        conexion.close()

#ACA ABAJO BORRAMOS LA FILA QUE QUERAMOS BUSCANDOLA POR EL NOMBRE:

    def deleteRow(self, nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE NOMBRE = ? COLLATE NOCASE", (nombre,))
        conexion.commit()
        conexion.close()

    #ABAJO BUSCAMOS LA FILA QUE DESEAMOS POR MEDIO DEL NOMBRE:
    def search(self, nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        instruccion = "SELECT * FROM productos WHERE NOMBRE LIKE ? COLLATE NOCASE"
        parametro = f"%{nombre}%"
        cursor.execute(instruccion, (parametro,))
        datos = cursor.fetchall()
        conexion.close()
        return datos

    #-----------enviamos a excel ---------#

    def exportar_a_csv(self, nombre_archivo="inventario.csv"):
        import csv
        
        # 1. Obtenemos todos los datos actuales la tabla:2
        datos = self.readRow()
        
        if not datos:
            return False # Si no hay datos, retornamos False para avisarle al main
            
        # 2. Abrimos (o creamos) un archivo CSV en modo escritura ('w')

        # Usamos encoding='utf-8' para que no haya problemas con tildes o eñes
        
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            # Opcional: Escribimos una cabecera para las columnas
            escritor.writerow(["ID", "NOMBRE", "PRECIO"])
            
            # 3. Escribimos todas las filas de la base de datos en el CSV
            for fila in datos:
                escritor.writerow(fila)
                
        return True


    ----------Traemos de excel -----------------
    
    def importar_csv(self, nombre_archivo="inventario.csv"):
        import csv

        try:
            with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
                # Leemos todo el contenido para detectar automáticamente el delimitador (coma o tabulador)
                contenido = archivo.read()
                delimitador = '\t' if '\t' in contenido else ','
                
                # Volvemos al inicio del archivo
                archivo.seek(0)
                lector = csv.reader(archivo, delimiter=delimitador)

                for fila in lector:
                    # 1. Ignoramos filas vacías
                    if not fila:
                        continue
                    
                    # 2. Ignoramos encabezados (si la fila contiene "ID" o "NOMBRE")
                    if "NOMBRE" in fila[0].upper() or "ID" in fila[0].upper():
                        continue

                    # 3. Validamos que haya al menos 2 columnas
                    if len(fila) < 2:
                        continue

                    try:
                        # Si el archivo tiene formato [ID, NOMBRE, PRECIO]
                        if len(fila) >= 3:
                            nombre = fila[1].strip()
                            precio = int(fila[2].strip())
                        # Si el archivo tiene formato [NOMBRE, PRECIO]
                        else:
                            nombre = fila[0].strip()
                            precio = int(fila[1].strip())

                        self.insertRow(nombre, precio)
                    except ValueError:
                        # Si el precio no es un número válido, saltamos esa línea
                        continue

            return True

        except FileNotFoundError:
            print(f"No se encontró el archivo: {nombre_archivo}")
            return False

        
