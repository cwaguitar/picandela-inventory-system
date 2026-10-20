from services import inventarioService  
from graficos import generar_grafico_precios
from analisis import analisis_picandela

def iniciar_app():
    
    servicio = inventarioService()
    
    while True:
        print("\n-- BIENVENIDOS A PICANDELA! ELIGE CUALQUIERA DE LAS OPCIONES A CONTINUACION:")
        print("OPCION 1: Ver todos los productos")
        print("OPCION 2: Agregar un producto")
        print("OPCION 3: Actualizar un producto")
        print("OPCION 4: Borrar un producto")
        print("OPCION 5: Buscar un producto")
        print("OPCION 6: Exportar a excel")
        print("OPCION 7: Importar desde excel")
        print("OPCION 8: Generar grafico precios")
        print("OPCION 9: Analisis producto/precio")
        print("OPCION 10: Salir")

        opcion = input("Elige una opcion entre 1 - 10 : ")

        if opcion == "1":

            print("\n--- VER TODOS LOS PRODUCTOS ---")

            mostrar = servicio.mostrar_producto()

            
            # Imprimimos el mensaje 
            
            print(f"PRODUCTOS ENCONTRADOS: \n {mostrar}")

        elif opcion == "2":

            print("\n--- AGREGAR UN PRODUCTO ---")
            nombre = input("Ingresa el nombre del producto: ") 
            precio = int(input("Ingresa su precio: ")) 

            # Llamamos al servicio y este nos devuelve una tupla: (exito: bool, mensaje: str)  
            
            exito, agregar = servicio.agregar_producto(nombre, precio)  
            print(agregar)    

            print("✅ ¡Producto agregado con éxito!")

        elif opcion == "3":
            nombre_nuevo = input("Ingresa el nombre del producto a actualizar: ") 
            precio_nuevo = int(input("Ingresa su precio actualizado: ")) 

            servicio.actualizar_producto(precio_nuevo, nombre_nuevo)
            print("✅ ¡Precio actualizado correctamente!")
            
        elif opcion == "4":
            borrar = input("Ingrese el nombre del producto a borrar: ")
            servicio.borrar_producto(borrar) 

            print("🗑️ ¡Producto procesado/eliminado!")
        
        elif opcion == "5":
            busqueda = input("Ingrese el nombre del producto a buscar: ")
            resultados = servicio.buscar_producto(busqueda) # Guardamos los resultado 
            
            if resultados:
                print(f"\n--- RESULTADOS DE BÚSQUEDA ---")
                for b in resultados:
                    print(f"ID: {b[0]} | Producto: {b[1]} | Precio: ${b[2]}")  
            else:
                print(f"\n⚠️ No se encontró ningún producto que coincida con '{busqueda}'.")

        elif opcion == "6":
            print("\n--- EXPORTANDO INVENTARIO ---")
            exito = servicio.exportar_excel()

            if exito:
                print("✅ ¡Inventario exportado con éxito!")
                print("📁 Busca el archivo 'inventario.csv' en la carpeta de tu proyecto y ábrelo con Excel.")
            else:
                print("⚠️ No hay productos en la base de datos para exportar.")

        elif opcion == '7':

            exito = servicio.importar_excel()
            
            if exito:

             print("---IMPORTANDO INVENTARIO ---")
             print("📁 Consulta tu tabla nuevamente para visualizar los archivos importados.")

        elif opcion == "8":
            
            generar_grafico_precios()

        elif opcion == "9":

            analisis_picandela()


        elif opcion == "10":

            print("¡Hasta pronto! 👋🏻")
            break

        else:
            print("\n⚠️ Opción no válida, por favor ingresa un número entre el 1 y el 10.")


if __name__ == "__main__":


    iniciar_app()


