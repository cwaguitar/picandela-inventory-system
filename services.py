from database import miTequeBase

class inventarioService:

    def __init__(self):

<<<<<<< HEAD
        self.db = miTequeBase() # el servicio posee y maneja la base de datos comienza asi porque hay que usar el self con la clase..

    # VALIDA LOS DATOS ANTES DE GUARDARLOS EN LA BD, DEVUELVE MENSAJE DE EXITO O MENSAJE DE ERROR:
=======
        self.db = miTequeBase() # el servicio posee y maneja la base de datos 
>>>>>>> 15ba69c88b542b92af52c0d71065b218c9b376cb

    def agregar_producto(self,nombre: str,precio_str: str):

        nombre = nombre.strip() # LIMPIAMOS LOS ESPACIOS EN BLANCO EXTRA:

        if not nombre:

            return False, "El nombre del producto no puede quedar vacio" 

        # intentamos convertir el precio a numero entero:
        try:

            precio = int(precio_str)

        except ValueError:

            return False, "El precio debe ser un numero entero valido"

        # Validamos que el precio sea mayor a cero:

        if precio <= 0 :

            return False, "El precio debe ser positivo mayor a cero"

        # SI PASA TODAS LAS REGLAS DE NEGOCIO GUARDAMOS LA INFORMACION EN LA BD
        
        self.db.insertRow(nombre,precio) # INSERCION A LA DATABASE!

        return True, f"El producto {nombre} fue guardado correctamente con su precio de: {precio}"

    # DE RESTO VIENE DE DATABASE AL MAIN,  DATABASE = > MAIN 



