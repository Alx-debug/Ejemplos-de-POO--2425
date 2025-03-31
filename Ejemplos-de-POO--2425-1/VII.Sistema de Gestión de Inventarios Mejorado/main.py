# main.py
from inventario import Inventario
from product import Producto


def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario completo")
    print("6. Salir")


def main():
    try:
        inventario = Inventario()  # Carga automática del archivo al iniciar
        print("Inventario cargado correctamente desde el archivo")
    except PermissionError:
        print("Error: Sin permisos para acceder al archivo de inventario")
        return
    except Exception as e:
        print(f"Error crítico al cargar el inventario: {str(e)}")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':

                id = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                nuevo_producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
                print("✓ Producto añadido y guardado en el archivo")

            elif opcion == '2':
                id = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id):
                    print("✓ Producto eliminado y archivo actualizado")
                else:
                    print("Producto no encontrado")

            elif opcion == '3':
                id = int(input("ID del producto a actualizar: "))
                campo = input("Campo a actualizar (nombre/cantidad/precio): ").lower()
                valor = input("Nuevo valor: ")

                try:
                    # Conversión de tipos
                    if campo == 'cantidad':
                        valor = int(valor)
                    elif campo == 'precio':
                        valor = float(valor)
                    elif campo == 'nombre':
                        if not valor.strip():
                            raise ValueError("El nombre no puede estar vacío")

                    inventario.actualizar_producto(id, **{campo: valor})
                    print("✓ Cambios guardados en el archivo")
                except ValueError as e:
                    print(f"Error en los datos: {str(e)}")

            elif opcion == '4':
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    print("\nResultados de búsqueda:")
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron productos")

            elif opcion == '5':
                inventario.mostrar_inventario()

            elif opcion == '6':
                print("Guardando cambios...")
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida. Intente nuevamente")

        except ValueError as e:
            print(f"Error de formato: {str(e)}")
        except PermissionError:
            print("Error: No se pudieron guardar cambios (verifique permisos del archivo)")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    main()
