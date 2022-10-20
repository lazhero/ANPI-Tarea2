import numpy as np

"""
@Definicion: Calcula la matriz diagonalmente dominante
@Entradas: 
-Vector p
-Vector q
-Valor m : dimensiones de la matriz
@Salidas:
-Matriz diagonalmente dominante
"""


def tridiagonal(p, q, m):

    p = [0]+p
    q = q+[0]
    mat = np.zeros((m, m))

    for i in range(m):
        for j in range(m):
            if i == j:
                mat[i][j] = 2*p[i]+2*q[i]
            elif i-j == 1:
                mat[i][j] = p[i]
            elif j-i == 1:
                mat[i][j] = q[j-1]

    return mat


"""
@Definicion: Calcula el vector =P
@Entradas:
-m: dimensiones
@Salidas:
-
"""


def getInicialP(m):

    value = 1
    vector = []
    while(len(vector) < m-1):
        vector.append(value)
        value += 0.1

    return vector


"""
@Definicion: Calcula  el vector B
@Entradas:
-m: dimensiones
@Salidas:
- vector b
"""


def getInitialB(m):

    vector = []
    while(len(vector) < m):
        vector.append(1)
    return np.ndarray.tolist(np.transpose([vector]))


"""
@Definicion: Calcula  una matriz de ceros
@Entradas:
-m: dimensiones
@Salidas:
- matriz de ceros
"""


def getInitialX0(m):
    return np.zeros((m, 1))
