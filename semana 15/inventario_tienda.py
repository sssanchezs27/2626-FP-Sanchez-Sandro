# Programa: Gestión de inventario de una tienda
# Este programa utiliza colecciones de datos (diccionario, lista y conjunto)
# para registrar productos, buscar información y eliminar elementos.

productos = {
    "manzana": {"precio": 2.50, "cantidad": 25, "categoria": "frutas"},
    "leche": {"precio": 3.20, "cantidad": 18, "categoria": "lácteos"},
    "arroz": {"precio": 4.00, "cantidad": 12, "categoria": "cereales"},
    "pan": {"precio": 2.00, "cantidad": 30, "categoria": "panadería"}
}

carrito = []
categorias = {producto["categoria"] for producto in productos.values()}


def mostrar_menu():
    print("\n=== INVENTARIO DE LA TIENDA ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Agregar al carrito")
    print("6. Mostrar carrito")
    print("7. Ver total del inventario")
    print("0. Salir")


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    if nombre in productos:
        print(f"El producto '{nombre}' ya existe. Use la opción de buscar o editar si deseas actualizarlo.")
        return

    try:
        precio = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        categoria = input("Ingrese la categoría: ").strip().lower()
    except ValueError:
        print("Entrada inválida. Verifique precio y cantidad.")
        return

    productos[nombre] = {
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    categorias.add(categoria)
    print(f"Producto '{nombre}' agregado correctamente.")


def mostrar_inventario():
    if not productos:
        print("El inventario está vacío.")
        return

    print("\nInventario actual:")
    for nombre, detalle in productos.items():
        print(f"- {nombre.title()}: {detalle['cantidad']} unidades, precio ${detalle['precio']:.2f}, categoría: {detalle['categoria']}")


def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    if nombre in productos:
        detalle = productos[nombre]
        print(f"\nProducto encontrado: {nombre.title()}")
        print(f"Precio: ${detalle['precio']:.2f}")
        print(f"Cantidad: {detalle['cantidad']}")
        print(f"Categoría: {detalle['categoria']}")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
    if nombre in productos:
        del productos[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe.")


def agregar_al_carrito():
    nombre = input("Ingrese el nombre del producto para agregar al carrito: ").strip().lower()
    if nombre not in productos:
        print("El producto no existe en el inventario.")
        return

    carrito.append(nombre)
    print(f"'{nombre.title()}' se agregó al carrito.")


def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
        return

    print("\nContenido del carrito:")
    for producto_nombre in carrito:
        detalle = productos[producto_nombre]
        print(f"- {producto_nombre.title()}: ${detalle['precio']:.2f}")


def total_inventario():
    total = 0
    for detalle in productos.values():
        total += detalle["precio"] * detalle["cantidad"]
    print(f"El valor total del inventario es: ${total:.2f}")


def main():
    print("Bienvenido a la gestión de inventario.")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            agregar_al_carrito()
        elif opcion == "6":
            mostrar_carrito()
        elif opcion == "7":
            total_inventario()
        elif opcion == "0":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
