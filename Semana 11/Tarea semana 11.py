matriz = [[0 for _ in range(5)] for _ in range(5)]

print("Ingrese 25 valores numéricos para llenar la matriz de 5x5")
print("=" * 50)

for fila in range(5):
    for columna in range(5):
        while True:
            try:
                valor = float(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
                matriz[fila][columna] = valor
                break
            except ValueError:
                print("Error: Ingrese un número válido.")

print("\n" + "=" * 50)
print("Matriz resultante:")
print("=" * 50)

for fila in range(5):
    for columna in range(5):
        print(f"{matriz[fila][columna]:>8.2f}", end="  ")
    print()

print("=" * 50)
