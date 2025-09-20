matrizA = [[1,1,2,1],
           [1,0,0,1]]
matrizB = [[1,1],
           [1,0],
           [2,1],
           [1,2]]
"""
filasA = len(matrizA)
columnasA = len(matrizA[0])
filasB = len(matrizB)
columnasB = len(matrizB[0])
matrizR = []
for i in range (filasA):
    matrizR.append([0]*columnasB)



for i in range(filasA):
    for j in range(columnasB):
        elemento = 0
        for x in range(filasB):
            elemento += matrizA[i][x] * matrizB [x][j]
        matrizR[i][j] = elemento


print(matrizR)

"""
# =========================
# Utilidades básicas
# =========================

def copia_matriz(A):
    return [fila[:] for fila in A]

def dims(A):
    return len(A), len(A[0])

def identidad(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def ceros(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]

def imprimir(A, titulo=None):
    if titulo: print(titulo)
    for fila in A:
        print(" ", ["{:8.4g}".format(x) for x in fila])
    print()

# =========================
# 1) Multiplicación de matrices (paso a paso)
# =========================

def multiplicar(A, B, explicar=True):
    m, n = dims(A)
    n2, p = dims(B)
    if n != n2:
        raise ValueError("No se pueden multiplicar: columnas(A) != filas(B)")
    C = ceros(m, p)
    if explicar:
        print("== Multiplicación de matrices ==")
        imprimir(A, "A =")
        imprimir(B, "B =")
    for i in range(m):
        for j in range(p):
            suma = 0
            if explicar:
                print(f"C[{i+1},{j+1}] = suma_k A[{i+1},k]*B[k,{j+1}]")
            for k in range(n):
                prod = A[i][k] * B[k][j]
                suma += prod
                if explicar:
                    print(f"  k={k+1}: {A[i][k]} * {B[k][j]} => parcial={suma}")
            C[i][j] = suma
            if explicar:
                print(f"  ==> C[{i+1},{j+1}] = {suma}\n")
    if explicar:
        imprimir(C, "Resultado C = A·B")
    return C

# =========================
# 2) Matriz menor M_ij
# =========================

def menor_matriz(A, i, j):
    """
    Retorna la matriz que resulta de eliminar la fila i y la columna j.
    i, j son índices base 0.
    """
    return [ [A[r][c] for c in range(len(A[0])) if c != j]
             for r in range(len(A)) if r != i ]

def ejemplo_menor():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    imprimir(A, "Matriz A =")
    i, j = 0, 0  # menor de a_11
    M = menor_matriz(A, i, j)
    imprimir(M, f"Menor M_{i+1}{j+1} (elimina fila {i+1} y columna {j+1}) =")

# =========================
# 3) Cofactor C_ij = (-1)^(i+j) * det(M_ij)
# =========================

def signo(i, j):
    # i, j base 0
    return 1 if (i + j) % 2 == 0 else -1

# Determinante por expansión (ver más abajo) lo usamos aquí:
def determinante(A, explicar=False, nivel=0):
    n, m = dims(A)
    if n != m:
        raise ValueError("El determinante requiere matriz cuadrada")
    indent = "  " * nivel
    if n == 1:
        if explicar: print(f"{indent}det([[{A[0][0]}]]) = {A[0][0]}")
        return A[0][0]
    if n == 2:
        val = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        if explicar:
            print(f"{indent}det(2x2) = {A[0][0]}*{A[1][1]} - {A[0][1]}*{A[1][0]} = {val}")
        return val
    # expansión por la primera fila
    det = 0
    if explicar:
        imprimir(A, f"{indent}Calculando det por cofactores (fila 1):")
    for j in range(n):
        a_1j = A[0][j]
        if a_1j == 0:
            if explicar:
                print(f"{indent}  a_1{j+1}=0 => término nulo, se omite.")
            continue
        M = menor_matriz(A, 0, j)
        s = signo(0, j)
        if explicar:
            print(f"{indent}  Término j={j+1}: a_1{j+1}={a_1j}, signo={s}")
        det_M = determinante(M, explicar=explicar, nivel=nivel+1)
        term = s * a_1j * det_M
        det += term
        if explicar:
            print(f"{indent}  contribución: {s}*{a_1j}*det(M_1{j+1}) = {term}  => acum={det}\n")
    if explicar:
        print(f"{indent}=> det(A) = {det}\n")
    return det

def cofactor(A, i, j, explicar=False):
    M = menor_matriz(A, i, j)
    det_M = determinante(M, explicar=explicar)
    s = signo(i, j)
    Cij = s * det_M
    if explicar:
        imprimir(A, "Matriz A =")
        imprimir(M, f"Menor M_{i+1}{j+1} =")
        print(f"C_{i+1}{j+1} = (-1)^({i+1}+{j+1}) * det(M) = {s} * {det_M} = {Cij}\n")
    return Cij

def matriz_de_cofactores(A, explicar=False):
    n, m = dims(A)
    if n != m:
        raise ValueError("Cofactores requieren matriz cuadrada")
    C = ceros(n, n)
    for i in range(n):
        for j in range(n):
            C[i][j] = cofactor(A, i, j, explicar=False)
    if explicar:
        imprimir(A, "A =")
        imprimir(C, "Matriz de cofactores de A =")
    return C

# =========================
# 4) Matriz adjunta (adjugate) = transpuesta de la matriz de cofactores
# =========================

def transpuesta(A):
    m, n = dims(A)
    return [[A[i][j] for i in range(m)] for j in range(n)]

def adjunta(A, explicar=False):
    C = matriz_de_cofactores(A, explicar=False)
    Adj = transpuesta(C)
    if explicar:
        imprimir(C, "Cofactores(A) =")
        imprimir(Adj, "Adjunta(A) = Transpuesta(Cofactores(A)) =")
    return Adj

# =========================
# 5) Determinante en términos de la adjunta:
#    A * Adj(A) = det(A) * I
# =========================

def verificar_identidad_adjunta(A):
    n, m = dims(A)
    if n != m:
        raise ValueError("Se requiere A cuadrada")
    print("== Verificación A · Adj(A) = det(A) · I ==")
    imprimir(A, "A =")
    Adj = adjunta(A, explicar=True)
    P = multiplicar(A, Adj, explicar=False)
    d = determinante(A, explicar=True)
    RHS = [[d * (1 if i==j else 0) for j in range(n)] for i in range(n)]
    imprimir(P, "Producto A·Adj(A) =")
    imprimir(RHS, f"det(A)·I  (det(A) = {d}) =")
    print("¿Coinciden? =>", P == RHS, "\n")

# =========================
# 6) Operaciones elementales por filas
# =========================

def intercambiar_filas(A, i, j, explicar=True):
    if explicar: imprimir(A, f"Intercambiar filas {i+1} y {j+1}:")
    A[i], A[j] = A[j], A[i]
    if explicar: imprimir(A, "Resultado:")

def escalar_fila(A, i, factor, explicar=True):
    if factor == 0:
        raise ValueError("Factor no puede ser 0")
    if explicar: imprimir(A, f"Multiplicar fila {i+1} por {factor}:")
    A[i] = [factor * x for x in A[i]]
    if explicar: imprimir(A, "Resultado:")

def sumar_multiplo(A, src, dst, factor, explicar=True):
    # F_dst := F_dst + factor * F_src
    if explicar: imprimir(A, f"F{dst+1} := F{dst+1} + ({factor})*F{src+1}:")
    A[dst] = [A[dst][k] + factor * A[src][k] for k in range(len(A[0]))]
    if explicar: imprimir(A, "Resultado:")

# =========================
# 7) Reducción Gauss (REF) y Gauss-Jordan (RREF)
# =========================

def buscar_pivote(M, fila_inicio, col):
    # Busca fila con pivote != 0 desde fila_inicio hacia abajo
    for r in range(fila_inicio, len(M)):
        if M[r][col] != 0:
            return r
    return None

def gauss_ref(A, explicar=True):
    """
    Lleva A a forma escalonada por filas (REF).
    Devuelve una copia transformada.
    """
    M = copia_matriz(A)
    if explicar:
        imprimir(M, "== Gauss (REF) - estado inicial ==")
    filas, cols = dims(M)
    fila_pivote = 0
    for col in range(cols):
        if fila_pivote >= filas:
            break
        r = buscar_pivote(M, fila_pivote, col)
        if r is None:
            continue
        if r != fila_pivote:
            if explicar: print(f"Pivotear: intercambiar filas {fila_pivote+1} y {r+1}")
            intercambiar_filas(M, fila_pivote, r, explicar=False)
            if explicar: imprimir(M, "Tras pivoteo:")
        # Eliminar por debajo
        piv = M[fila_pivote][col]
        if explicar: print(f"Usar pivote en ({fila_pivote+1},{col+1}) = {piv} para anular debajo")
        for r2 in range(fila_pivote + 1, filas):
            if M[r2][col] != 0:
                factor = - M[r2][col] / piv
                if explicar: print(f"  F{r2+1} := F{r2+1} + ({factor})*F{fila_pivote+1}")
                sumar_multiplo(M, fila_pivote, r2, factor, explicar=False)
        if explicar: imprimir(M, "Después de eliminar en la columna")
        fila_pivote += 1
    if explicar:
        imprimir(M, "== Resultado en REF ==")
    return M

def gauss_jordan_rref(A, explicar=True):
    """
    Lleva A a forma reducida por filas (RREF).
    Devuelve una copia transformada.
    """
    M = gauss_ref(A, explicar=explicar)
    filas, cols = dims(M)

    # Normalizar pivotes a 1 y eliminar por arriba
    if explicar: print("== Fase Gauss-Jordan: normalizar pivotes y limpiar arriba ==")
    # Recorremos de abajo hacia arriba buscando pivotes
    fila = filas - 1
    while fila >= 0:
        # encontrar columna pivote (primer no-cero en la fila)
        col_piv = None
        for c in range(cols):
            if M[fila][c] != 0:
                col_piv = c
                break
        if col_piv is not None:
            piv = M[fila][col_piv]
            # Escalar fila para que pivote sea 1
            if piv != 1:
                if explicar: print(f"  Normalizar F{fila+1} dividiendo por {piv}")
                M[fila] = [x / piv for x in M[fila]]
                if explicar: imprimir(M, f"  F{fila+1} normalizada:")
            # Eliminar por arriba
            for r in range(fila):
                if M[r][col_piv] != 0:
                    factor = - M[r][col_piv]
                    if explicar: print(f"  F{r+1} := F{r+1} + ({factor})*F{fila+1}")
                    M[r] = [M[r][k] + factor * M[fila][k] for k in range(cols)]
            if explicar: imprimir(M, "  Tras limpiar arriba de este pivote:")
        fila -= 1

    if explicar:
        imprimir(M, "== Resultado en RREF ==")
    return M

# =========================
# DEMOSTRACIONES RÁPIDAS
# (Ejecuta estos bloques para ver el paso a paso)
# =========================

if __name__ == "__main__":
    # 1) Multiplicación
    A = [[1, 2, 3],
         [4, 5, 6]]
    B = [[2, 0],
         [1, 3],
         [0, 1]]
    multiplicar(A, B, explicar=True)

    # 2) Menor de un elemento
    ejemplo_menor()

    # 3) Cofactor puntual
    A2 = [[1, 2, 3],
          [0, 4, 5],
          [1, 0, 6]]
    _ = cofactor(A2, 0, 1, explicar=True)  # C_12

    # 4) Adjunta
    Adj = adjunta(A2, explicar=True)

    # 5) Identidad A·Adj(A) = det(A)·I
    verificar_identidad_adjunta(A2)

    # 6) Operaciones por filas
    M = [[1, 2],
         [3, 4]]
    intercambiar_filas(M, 0, 1)
    escalar_fila(M, 0, -2)
    sumar_multiplo(M, 0, 1, 1.5)

    # 7) Gauss y Gauss-Jordan (ejemplo con matriz aumentada de un sistema)
    # Sistema: x + 2y = 5 ; 3x + 4y = 11
    Aug = [[1, 2, 5],
           [3, 4, 11]]
    gauss_ref(Aug, explicar=True)
    gauss_jordan_rref(Aug, explicar=True)

