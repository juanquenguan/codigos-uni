"""
--------------Laboratorio 02 - F.D.P.I. Grupo 52
--------------Nombre: Juan Paulo Quenguan Loaiza
--------------Código: 2460557
"""


import random #Importamos esta libreria para obtener un numero aleatorio
import funciones_lab as function

"""

def principal():
    
    numero_secreto = function.generar_numero()
    intentos_restantes = 5

    if function.revisarDigitos(numero_secreto)==False:
        print("el número aleatorio generado por el PC no tiene los dígitos diferentes.")
    else:
        print(
            "Bienvenido al juego de Pin-Pon"
            "\nTendras que adivinar un número entero aleatorio de 3 dígitos"
            "\nEn cada intento recibiras 1 Pin por cada digito que adivines y este en posición correcta"
            "\nEn cada intento recibiras 1 Pon por cada digito que adivines pero no este en posición correcta"
            "\nTienes 5 intentos para adivinar el número."
            )
        
        
        primer_intento = int(input("Introduce tu primer intento de adivinar el número: "))
        print(numero_secreto)
        function.verificarIntentos(numero_secreto, primer_intento, intentos_restantes - 1)

principal()
"""
import tkinter as tk
from tkinter import messagebox
import random

def llenarMatriz(matriz):
    tMatriz = len(matriz)
    parejas = int((tMatriz ** 2) / 2)
    elementos = list(range(1, parejas + 1)) * 2
    random.shuffle(elementos)
    indice = 0
    for i in range(tMatriz):
        for j in range(tMatriz):
            matriz[i][j] = elementos[indice]
            indice += 1

def mostrarMatriz(matriz):
    tMatriz = len(matriz)
    posiciones = ''
    for i in range(tMatriz):
        for j in range(tMatriz):
            posicion = str(i) + "," + str(j) + "\t"
            posiciones += posicion
        posiciones += '\n'
    return posiciones

def matrizTabulada(matriz, fpar1, cpar1, fpar2, cpar2, parejas_encontradas):
    tMatriz = len(matriz)
    fichasUsuarios = "\n"
    for fila in range(tMatriz):
        for columna in range(tMatriz):
            if (fila == fpar1 and columna == cpar1) or (fila == fpar2 and columna == cpar2) or (fila, columna) in parejas_encontradas:
                ficha = str(matriz[fila][columna]) + "\t"
                fichasUsuarios += ficha
            else:
                vacio = "-\t"
                fichasUsuarios += vacio
        fichasUsuarios += "\n"
    return fichasUsuarios

def verificarPareja(matriz, fpar1, cpar1, fpar2, cpar2):
    return matriz[fpar1][cpar1] == matriz[fpar2][cpar2]

def create_widgets(root, matriz, tMatriz):
    buttons = [[None for _ in range(tMatriz)] for _ in range(tMatriz)]
    for i in range(tMatriz):
        for j in range(tMatriz):
            button = tk.Button(root, text='-', width=8, height=4, command=lambda i=i, j=j: reveal(i, j))
            button.grid(row=i, column=j)
            buttons[i][j] = button

    label_puntaje = tk.Label(root, text=f'Puntaje: {puntaje}')
    label_puntaje.grid(row=tMatriz, column=0, columnspan=tMatriz // 2)
    label_intentos = tk.Label(root, text=f'Intentos restantes: {5 - intento}')
    label_intentos.grid(row=tMatriz, column=tMatriz // 2, columnspan=tMatriz // 2)
    return buttons, label_puntaje, label_intentos

def reveal(i, j):
    global seleccion, parejas_encontradas, puntaje, intento, nParejas, completado

    if (i, j) in parejas_encontradas or len(seleccion) == 2:
        return

    buttons[i][j].config(text=str(matriz[i][j]))
    seleccion.append((i, j))

    if len(seleccion) == 2:
        root.after(1000, check_pareja)

def check_pareja():
    global seleccion, parejas_encontradas, puntaje, intento, nParejas, completado

    fpar1, cpar1 = seleccion[0]
    fpar2, cpar2 = seleccion[1]

    if verificarPareja(matriz, fpar1, cpar1, fpar2, cpar2):
        parejas_encontradas.append((fpar1, cpar1))
        parejas_encontradas.append((fpar2, cpar2))
        puntaje += 10
        nParejas += 1
    else:
        buttons[fpar1][cpar1].config(text='-')
        buttons[fpar2][cpar2].config(text='-')
        intento += 1

    label_puntaje.config(text=f'Puntaje: {puntaje}')
    label_intentos.config(text=f'Intentos restantes: {5 - intento}')
    seleccion = []

    if nParejas == (tMatriz ** 2) // 2:
        messagebox.showinfo("Juego de Memoria", "¡Ganaste!")
        completado = True
        root.destroy()
    elif intento >= 5:
        messagebox.showinfo("Juego de Memoria", "Te has quedado sin intentos")
        root.destroy()

# Inicialización del juego
intento = 0
puntaje = 0
nParejas = 0
parejas_encontradas = []
seleccion = []
completado = False

tMatriz = int(input("Que tamaño desea que tenga la matriz: "))
while tMatriz < 2 or tMatriz % 2 != 0:
    print("La matriz debe tener un numero par de elementos")
    tMatriz = int(input("Que tamaño desea que tenga la matriz: "))

matriz = [[0 for columna in range(tMatriz)] for fila in range(tMatriz)]
llenarMatriz(matriz)

root = tk.Tk()
root.title("Juego de Memoria")

buttons, label_puntaje, label_intentos = create_widgets(root, matriz, tMatriz)

root.mainloop()
