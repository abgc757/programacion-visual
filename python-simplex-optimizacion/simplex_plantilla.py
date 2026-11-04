# -*- coding: utf-8 -*-
"""
PRÁCTICA: Método Simplex en Python
Materia: Métodos y Técnicas de Optimización — LIC_R_ING_4
Alumno: ______________________   Matrícula: __________   Fecha: ________

Instrucciones: completa cada bloque marcado con  # TODO.
Ejecuta el archivo completo:  python simplex_Apellido.py
"""
import numpy as np


# ---------------------------------------------------------------
# PARTE 1 — MAXIMIZAR:  max z = c·x   sujeto a  A x <= b,  x >= 0
# ---------------------------------------------------------------
def simplex_max(c, A, b, mostrar=True):
    c = np.array(c, dtype=float)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    m, n = A.shape                      # m restricciones, n variables

    # TODO 1: crea la tabla T de ceros con (m+1) filas y (n+m+1) columnas
    T = None

    # TODO 2: llena la tabla  [ A | I | b ]  y la última fila  [ -c | 0 | 0 ]
    #   T[:m, :n]       = A
    #   T[:m, n:n+m]    = np.eye(m)
    #   T[:m, -1]       = b
    #   T[m, :n]        = -c

    base = list(range(n, n + m))        # al inicio las holguras son las básicas
    it = 0

    while True:
        if mostrar:
            print(f"\n--- Tabla {it} ---")
            print(np.round(T, 3))
            print("Base:", [f"x{j+1}" for j in base])

        fila_z = T[m, :-1]

        # TODO 3: si NO hay negativos en fila_z, la solución es óptima -> break

        # TODO 4: columna pivote = posición del valor más negativo (np.argmin)
        col = None

        # TODO 5: cocientes b_i / a_i,col solo donde a_i,col > 0 ; fila pivote = menor cociente
        fila = None

        # TODO 6: divide la fila pivote entre el pivote y haz ceros en el resto de la columna

        base[fila] = col
        it += 1

    x = np.zeros(n + m)
    for i, j in enumerate(base):
        x[j] = T[i, -1]
    precios_sombra = T[m, n:n + m]
    return x[:n], T[m, -1], precios_sombra


# ---------------------------------------------------------------
# PARTE 2 — MINIMIZAR usando el DUAL:  min z = c·x  s.a.  A x >= b
# ---------------------------------------------------------------
def simplex_min(c, A, b, mostrar=True):
    A = np.array(A, dtype=float)
    # TODO 7: resuelve el DUAL con simplex_max(b, A.T, c) y regresa:
    #         x* = precios sombra del dual, z* = valor del dual
    pass


# ---------------------------------------------------------------
# PRUEBAS (no borrar)
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== PROBLEMA 1 (MAX) ===")
    x, z, p = simplex_max([3, 5], [[1, 0], [0, 2], [3, 2]], [4, 12, 18])
    print("x =", x, " Z =", z, " precios sombra =", p)

    print("\n=== PROBLEMA 3 (MIN) ===")
    x, z, y = simplex_min([12, 20], [[6, 8], [7, 12]], [100, 120])
    print("x =", x, " Z =", z)
