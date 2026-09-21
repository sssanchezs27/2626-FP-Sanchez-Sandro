# Programa: calcular promedio de tres notas usando función con parámetros y return

def promedio(n1, n2, n3):
    """Devuelve el promedio de tres notas."""
    return (n1 + n2 + n3) / 3


def main():
    try:
        n1 = float(input("Ingrese la primera nota: "))
        n2 = float(input("Ingrese la segunda nota: "))
        n3 = float(input("Ingrese la tercera nota: "))
    except ValueError:
        print("Entrada inválida. Use números.")
        return

    resultado = promedio(n1, n2, n3)
    print(f"El promedio de las tres notas es: {resultado:.2f}")


if __name__ == "__main__":
    main()
