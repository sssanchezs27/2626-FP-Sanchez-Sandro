# Programa que declara una matriz 3x3
# Autor: Sandro Sanchez
#descripcion: este programa declara una matriz 3*3, la recorre con ciclos e imprime sus valores

# Definir matriz como arreglo de 3*3

matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
print("valores de la matriz 3*3:")
print("-" *20)

#Recorrer la matriz con ciclos anidados

for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    print("-" *20)
    print("nMatriz completa")
    for fila in matriz:
        print(fila)


