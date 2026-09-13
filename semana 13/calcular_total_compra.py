def calcular_total_compra(precio, cantidad):
    """Calcula el total a pagar por una compra."""
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio = 10
    cantidad = 3
    resultado = calcular_total_compra(precio, cantidad)
    print(f"El total de la compra es: ${resultado}")
