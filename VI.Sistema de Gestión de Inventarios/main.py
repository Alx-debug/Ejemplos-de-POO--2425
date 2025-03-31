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
    inventario = Inventario()

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
                print("Producto añadido exitosamente!")

            elif opcion == '2':
                id = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id):
                    print("Producto eliminado")
                else:
                    print("Producto no encontrado")

            elif opcion == '3':
                id = int(input("ID del producto a actualizar: "))
                campo = input("Campo a actualizar (nombre/cantidad/precio): ").lower()
                valor = input("Nuevo valor: ")

                try:
                    if campo == 'cantidad':
                        valor = int(valor)
                    elif campo == 'precio':
                        valor = float(valor)

                    inventario.actualizar_producto(id, **{campo: valor})
                    print("Actualización exitosa")
                except ValueError as e:
                    print(f"Error: {str(e)}")

            elif opcion == '4':
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron productos")

            elif opcion == '5':
                inventario.mostrar_inventario()

            elif opcion == '6':
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida")

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    main()
