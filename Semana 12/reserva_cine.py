# Programa: reserva_cine.py
# Autor: (escriba su nombre aquí)
# Objetivo: Gestionar la reserva de un asiento en una sala de 3 filas x 4 columnas.

# Crear la matriz de asientos (3 filas x 4 columnas) inicializada en 0
asientos = [[0] * 4 for _ in range(3)]

# Solicitar al usuario la fila y la columna, con validación
while True:
    try:
        fila = int(input("Ingrese fila (0 a 2): "))
        columna = int(input("Ingrese columna (0 a 3): "))
    except ValueError:
        print("Entrada inválida: debe ingresar números enteros. Intente de nuevo.\n")
        continue

    if not (0 <= fila <= 2 and 0 <= columna <= 3):
        print("Índices fuera de rango. Las filas válidas son 0-2 y las columnas 0-3. Intente de nuevo.\n")
        continue

    if asientos[fila][columna] == 1:
        print("El asiento ya está reservado. Por favor, elija otro.\n")
        continue

    # Reservar el asiento
    asientos[fila][columna] = 1
    break

# Mostrar el estado de la sala en formato de tabla
print("\nEstado de la sala:")
for fila_asientos in asientos:
    # Imprimir los valores de la fila en la misma línea separados por espacios
    print(' '.join(str(estado) for estado in fila_asientos))

# Fin del programa
