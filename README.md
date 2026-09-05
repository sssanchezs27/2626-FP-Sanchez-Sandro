# Reserva de asientos - Semana 12

Estudiante: Sanchez Sandro

Objetivo

Este repositorio contiene un programa en Python que gestiona la reserva de un asiento en una sala de cine pequeña (3 filas x 4 columnas). Al ejecutarlo, solicita la fila y la columna del asiento, registra la reserva y muestra el estado completo de la sala como una tabla de ceros (libre) y unos (reservado).

Archivo principal

- Semana 12\reserva_cine.py : Programa principal en Python.

Cómo ejecutar

1. Abrir una terminal en la carpeta raíz del repositorio.
2. Navegar a la carpeta "Semana 12":
   cd "Semana 12"
3. Ejecutar el programa con Python 3:
   python reserva_cine.py

Al ejecutarse, el programa pedirá:
- Ingrese fila (0 a 2)
- Ingrese columna (0 a 3)

Luego mostrará la sala completa en formato de tabla (3 filas x 4 columnas) con 0 = libre y 1 = reservado.

Notas

- Asegúrese de tener Python 3 instalado.
- El archivo contiene validación básica de índices y advierte si el asiento ya está reservado.