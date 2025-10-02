"""
Funcion parta calcular la suma de dos matrices cuadradas
"""
def sumaMatrices(matrizA, matrizB):
    matrizResultante = []
    for i in range(len(matrizA)):
        fila = []
        for j in range(len(matrizA[0])):
            fila.append(matrizA[i][j]  + matrizB[i][j])
        matrizResultante.append(fila)
    return matrizResultante

"""
Funcion parta calcular la resta de dos matrices cuadradas
"""
def restaMatrices(matrizA, matrizB):
    matrizResultante = []
    for i in range(len(matrizA)):
        fila = []
        for j in range(len(matrizA[0])):
            fila.append(matrizA[i][j]  - matrizB[i][j])
        matrizResultante.append(fila)
    return matrizResultante

"""
Funcion parta calcular la suma de filas de una matriz
"""
def sumaFila(fila1, fila2):
    filaResultante = []
    for i in range(len(fila1)):
        filaResultante.append(fila1[i] + fila2[i])
    return filaResultante

""" Funcion parta calcular la multiplicacion de una matriz por un escalar """
def multPorEscalarMatriz(matrizA, escalar):
    matrizResultante = []
    for i in range(len(matrizA)):
        matrizResultante.append(multPorEscalarFila(matrizA[i], escalar))
    return matrizResultante

""" Funcion parta calcular la multiplicacion de una fila por un escalar """
def multPorEscalarFila(fila, escalar):
    filaResultante = []
    for i in range(len(fila)):
        filaResultante.append(fila[i] * escalar)
    return filaResultante

""" Funcion parta calcular la traspuesta de una matriz cuadrada """
def traspuesta(matriz):
    matrizResultante = []
    for j in range(len(matriz[0])):
        fila = []
        for i in range (len(matriz)):
            fila.append(matriz[i][j])
        matrizResultante.append(fila)
    return matrizResultante

""" Funcion parta calcular la multiplicacion de dos matrices cuadradas """
def multMatrices(matrizA, matrizB):
    matrizResultante = []
    for i in range (len(matrizA)):
        fila = []
        for j in range (len(matrizB[0])):
            suma = 0
            for k in range (len(matrizA[0])):
                suma += matrizA[i][k] * matrizB[k][j]
            fila.append(suma)
        matrizResultante.append(fila)
    return matrizResultante

""" Funcion parta calcular la matriz menor resultante de eliminar la fila i y columna j de una matriz cuadrada """
def menorIJ(matriz, i, j):
    matrizResultante = []
    for fila in range(len(matriz)):
        if fila != i:
            filaResultante = []
            for columna in range(len(matriz)):
                if columna != j:
                    filaResultante.append(matriz[fila][columna])
            matrizResultante.append(filaResultante)
    return matrizResultante

""" Funcion parta calcular el determinante de una matriz """
def determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    elif len(matriz) == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    else:
        det = 0
        for j in range(len(matriz)):
            det += (-1)**j * matriz[0][j] * determinante(menorIJ(matriz, 0, j))
        return det
    
"""
Funcion parta calcular la adjunta de una matriz cuadrada
"""
def adjunta(matriz):
    matrizResultante = []
    for i in range (len(matriz)):
        fila = []
        for j in range (len(matriz)):
            fila.append((-1)**(i+j)*determinante(menorIJ(matriz,i,j)))
        matrizResultante.append(fila)
    return matrizResultante

""" Funcion parta calcular la inversa de una matriz """
def inversa(matriz):
    return multPorEscalarMatriz(traspuesta(adjunta(matriz)), 1/determinante(matriz))

# Operaciones elementales en una matriz 

""" Funcion parta calcular la multiplicacion de una fila por un escalar """
def filaPorEscalar(matriz, escalar, fila):
    matrizResultante = []
    for i in range (len(matriz)):
        if i == fila:
            matrizResultante.append(multPorEscalarFila(matriz[i], escalar))
        else:
            matrizResultante.append(matriz[i])
    return matrizResultante

"""Funcion parta calcular la suma o resta de una fila con otra multiplicada por un escalar """
def restaFilas(matriz, filaOrigen, escalar, filaDestino):
    matrizResultante = []
    for i in range (len(matriz)):
        if i == filaDestino:
            matrizResultante.append(sumaFila(matriz[filaDestino], multPorEscalarFila(matriz[filaOrigen], escalar)))
        else:
            matrizResultante.append(matriz[i])
    return matrizResultante

""" Funcion parta intercambiar dos filas de una matriz """
def intercambioFilas(matriz, fila1, fila2):
    matrizResultante = []
    for i in range (len(matriz)):
        if i == fila1:
            matrizResultante.append(matriz[fila2])
        elif i == fila2:
            matrizResultante.append(matriz[fila1])
        else:
            matrizResultante.append(matriz[i])
    return matrizResultante

def gaussiana(matriz):

    A = matriz.copy()
    for i in range(len(A)):
        # 1. Verificar si el pivote es 0, si lo es, intercambiar filas
        if A[i][i] == 0:
            for k in range(i+1, len(A)):
                if A[k][i] != 0:
                    A = intercambioFilas(A, i, k)
                    break
        
        # 2. Hacer ceros debajo del pivote
        for k in range(i+1, len(A)):
            if A[k][i] != 0:  # solo si hay algo distinto de 0
                if A[i][i] == 0:  # si el pivote es 0, buscar otra fila
                    for r in range(i+1, len(A)):
                        if A[r][i] != 0:
                            A = intercambioFilas(A, i, r)
                        break
            if A[i][i] != 0:  # ahora sí podemos dividir
                factor = -A[k][i] / A[i][i]
                A = restaFilas(A, i, factor, k)

    
    return A

def gaussJordan(M):
    n = len(M)

    for i in range(n):
        # 1. Pivotear si el pivote es 0
        if M[i][i] == 0:
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M = intercambioFilas(M, i, k)
                    break

        # 2. Normalizar fila para que pivote sea 1
        pivote = M[i][i]
        if pivote != 0:
            M = filaPorEscalar(M, 1 / pivote, i)

        # 3. Hacer ceros en las demás filas
        for k in range(n):
            if k != i:
                if M[k][i] != 0:
                    factor = -M[k][i]
                    M = restaFilas(M, i, factor, k)

    return M


def resolverSistema(A, B):
    n = len(A)

    # Asegurar que B sea una matriz columna
    if not isinstance(B[0], list):
        nuevaB = []
        for b in B:
            nuevaB.append([b])
        B = nuevaB

    # Construir la matriz aumentada [A | B]
    M = []
    for i in range(n):
        fila = []
        for elemento in A[i]:
            fila.append(elemento)
        for elemento in B[i]:
            fila.append(elemento)
        M.append(fila)

    # Aplicar Gauss-Jordan
    M = gaussJordan(M)

    # Extraer la parte derecha (X)
    X = []
    for fila in M:
        parteDerecha = []
        for j in range(n, len(fila)):
            parteDerecha.append(fila[j])
        X.append(parteDerecha)

    return X
