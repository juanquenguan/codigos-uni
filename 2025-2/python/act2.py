"""
Funcion parta calcular la suma de dos matrices cuadradas
"""
def suma(matrizA, matrizB):
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
def resta(matrizA, matrizB):
    matrizResultante = []
    for i in(len(matrizA)):
        fila = []
        for j in (len(matrizA[0])):
            fila.append(matrizA[i][j]  - matrizB[i][j])
        matrizResultante.append(fila)
    return matrizResultante


"""
Funcion parta calcular la adjunta de una matriz cuadrada
"""
def adjunta(matriz):
    matrizResultante = []
    for i in (len(matriz)):
        fila = []
        for j in (len(matriz)):
            print("taka taki")
            #fila.append((-1)**(i+j)*determinante(menorIJ(matriz,i,j)))
        matrizResultante.append(fila)
    return matrizResultante