from database import miTequeBase

class inventarioService:

    def __init__(self):

        self.db = miTequeBase() # el servicio posee y maneja la base de datos comienza asi porque hay que usar el se;f con la clase..

    def agregar_producto(self,nombre: str,precio_str: str):

        # VALIDA LOS DATOS ANTES DE GUARDARLOS EN LA BD, DEVUELVE MENSAJE DE EXITO O MENSAJE DE ERROR:

        # LIMPIAMOS LOS ESPACIOS EN BLANCO EXTRA:

        nombre = nombre.strip()

        if not nombre:

            return False, "El nombre del producto no puede quedar vacio" # el false se debe representar en main con una variable

        # intentamos convertir el precio a numero entero:

        try:

            precio = int(precio_str)

        except ValueError:

            return False, "El precio debe ser un numero entero valido"


        # Validamos que el precio sea mayor a cero:

        if precio <= 0 :

            return False, "El precio debe ser positivo mayor a cero"

        # SI PASA TODAS LAS REGLAS DE NEGOCIO GUARDAMOS LA INFORMACION EN LA BD
        
        self.db.insertRow(nombre,precio)

        return True, f"El producto {nombre} fue guardado correctamente con su precio de: {precio}"

    # COMO YA TODO EN MAIN DEPENDE DE SERVICES Y NO DE DATABASE DEASDE ACA LE MANDAMOS LAS FUNCIONES
    # QUE NECESITE MAIN DE DATABASE PARA ESTO LAS CREAMOS ACA Y SE LAS DEJAMOS A MAIN PARA QUE ACCEDAN:
    # DATABASE => SERVICES =>MAIN

  
#---------------------------------------

    def mostrar_producto(self):
    
            return self.db.readRow()

# ---------------------------------------

    def actualizar_producto(self,nombre_nuevo,precio_nuevo):

        return self.db.updateFields(nombre_nuevo,precio_nuevo)

#-----------------------------------------

    def borrar_producto(self,borrar):

        return self.db.deleteRow(borrar)

# ----------------------------------------
    def buscar_producto(self,busqueda):

        return self.db.search(busqueda) 
    
#-----------------------------------------

    def exportar_excel(self):

        return self.db.exportar_a_csv()

# ----------------------------------------

    def importar_excel(self):

        return self.db.importar_csv()

#nota: no hacemos el de agregar_producto porque esa funcino es la que hace la logica del service.