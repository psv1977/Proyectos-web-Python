# Tomar una matriz sencilla, calcular sus autovalores y autovectores, e interpretar el resultado
# La idea es usar una matriz pequeña, por ejemplo una matriz cuadrada 2×2 que tenga valores reales y autovalores fáciles de interpretar.

import numpy as np
# Definir una matriz 2x2
A = np.array([[4, 2],
              [1, 3]])
# Calcular los autovalores y autovectores
autovalores, autovectores = np.linalg.eig(A)
# Mostrar los resultados
print("Matriz A:")
print(A)
print("\nAutovalores:")
print(autovalores)
print("\nAutovectores:")
print(autovectores)

#comprobacion de los autovalores y autovectores
np.allclose(A @ autovectores[:, 0], autovalores[0] * autovectores[:, 0])