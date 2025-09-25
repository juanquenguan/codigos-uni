"""
Funcion parta calcular la suma de dos matrices cuadradas
"""
def sumaMatrices(matrizA, matrizB):
    matrizResultante = []
    for i in(len(matrizA)):
        fila = []
        for j in (len(matrizA[0])):
            fila.append(matrizA[i][j]  + matrizB[i][j])
        matrizResultante.append(fila)
    return matrizResultante

"""
Funcion parta calcular la resta de dos matrices cuadradas
"""
def restaMatrices(matrizA, matrizB):
    matrizResultante = []
    for i in(len(matrizA)):
        fila = []
        for j in (len(matrizA[0])):
            fila.append(matrizA[i][j]  - matrizB[i][j])
        matrizResultante.append(fila)
    return matrizResultante

"""
Funcion parta calcular la suma de filas de una matriz
"""
def sumaFila(fila1, fila2):
    filaResultante = []
    for i in(len(fila1)):
        filaResultante.append(fila1[i] + fila2[i])
    return filaResultante

def multPorEscalarMatriz(matrizA, escalar):
    matrizResultante = []
    for i in(len(matrizA)):
        matrizResultante.append(multPorEscalarFila(matrizA[i], escalar))
    return matrizResultante

def multPorEscalarFila(fila, escalar):
    filaResultante = []
    for i in(len(fila)):
        filaResultante.append(fila[i] * escalar)
    return filaResultante
def traspuesta(matriz):
    matrizResultante = []
    for j in (len(matriz[0])):
        fila = []
        for i in (len(matriz)):
            fila.append(matriz[i][j])
        matrizResultante.append(fila)
    return matrizResultante

def multMatrices(matrizA, matrizB):
    matrizResultante = []
    for i in (len(matrizA)):
        fila = []
        for j in (len(matrizB[0])):
            suma = 0
            for k in (len(matrizA[0])):
                suma += matrizA[i][k] * matrizB[k][j]
            fila.append(suma)
        matrizResultante.append(fila)
    return matrizResultante

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
    for i in (len(matriz)):
        fila = []
        for j in (len(matriz)):
            fila.append((-1)**(i+j)*determinante(menorIJ(matriz,i,j)))
        matrizResultante.append(fila)
    return matrizResultante

def filaPorEscalar(matriz, escalar, fila):
    matrizResultante = []
    for i in (len(matriz)):
        if i == fila:
            matrizResultante.append(multPorEscalarFila(matriz[i], escalar))
        else:
            matrizResultante.append(matriz[i])
    return matrizResultante

def restaFilas(matriz, filaOrigen, escalar, filaDestino):
    matrizResultante = []
    for i in (len(matriz)):
        if i == filaDestino:
            matrizResultante.append(sumaFila(matriz[filaDestino], multPorEscalarFila(matriz[filaOrigen], escalar)))
        else:
            matrizResultante.append(matriz[i])
    return matrizResultante
def intercambiaFilas(matriz, fila1, fila2):
    matrizResultante = []
    for i in (len(matriz)):
        if i == fila1:
            matrizResultante.append(matriz[fila2])
        elif i == fila2:
            matrizResultante.append(matriz[fila1])
        else:
            matrizResultante.append(matriz[i])
    return matrizResultante