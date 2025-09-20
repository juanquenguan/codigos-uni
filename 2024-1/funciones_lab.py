"""
--------------Laboratorio 02 - F.D.P.I. Grupo 52
--------------Nombre: Juan Paulo Quenguan Loaiza
--------------Código: 2460557
"""

import random

def revisarDigitos(numero):
    digito0 = int(numero/100)
    digito1 = int((numero-digito0*100)/10)
    digito2 = int((numero-(digito1*10+digito0*100)))
    si = bool
    if digito0 == digito1 or digito0 == digito2 or (digito2 == digito1):
        si = False
    else:
        si = True
    return si

pass

def pin_pon(numeroA, numeroB):
    digito0a = int(numeroA/100)
    digito1a = int((numeroA-digito0a*100)/10)
    digito2a = int(numeroA-(digito1a*10+digito0a*100))

    digito0b = int(numeroB/100)
    digito1b = int((numeroB-digito0b*100)/10)
    digito2b = int((numeroB-(digito1b*10+digito0b*100)))
   
    resultado = " "
    if digito0a == digito0b:
        resultado += "Pin "
    if digito0a == (digito1b or digito2b) :
        resultado += "Pon "
    if (digito0a != digito0b) and (digito0a != (digito1b or digito2b)) :
        resultado += "- "
    if digito1a == digito1b:
        resultado += "Pin "
    if digito1a == (digito0b or digito2b) :
        resultado += "Pon "
    if (digito1a != digito1b) and (digito1a != (digito0b or digito2b)) :
        resultado += "- "
    if digito2a == digito2b:
        resultado += "Pin "
    if digito2a == (digito1b or digito0b) :
        resultado += "Pon "
    if (digito2a != digito2b) and (digito2a != (digito1b or digito0b)) :
        resultado += "- "

    print(resultado)
    
pass



def verificarIntentos(numero_secreto, intento, intentos_restantes):
    if intento == numero_secreto:
        resultado = "Pin Pin Pin"
        resultado += "\nHas adivinado el número"
        print(resultado)
    elif intentos_restantes == 0:
        resultado = "Perdiste. El número secreto era "+str(numero_secreto)+" Mejor suerte la próxima vez."
        print(resultado)
    else:

        pin_pon(intento,numero_secreto)
        
        print("Quedan ",intentos_restantes," intentos")
        nuevo_intento = int(input("Introduce tu próximo intento de adivinar el número: "))
        verificarIntentos(numero_secreto, nuevo_intento, intentos_restantes - 1)
        
pass

def generar_numero():
    """
    -Esta funcion me permite crear un numero aleatorio entre el 100 y el 999.
    -No tiene parametros.
    -puede ser cualquier número entero de 3 dígitos.
    """
    return int(random.randint(100, 999))

def verificar_intentos(numero_secreto, intento, intentos_restantes):
    """
    Contrato:
    -Esta es una función recursiva que se encargara de leer el intento del usuario y retornara las palabras Pin,
    Pon, Has adivinado el número o Perdiste.
    -Entradas:
        -numero_secreto: Será el numero aleatorio que se decidira al iniciar el programa
        -intento: esta entrada sera el número ingresado por el usuario y es el que se comparara con el número
         secreto, para saber que paso seguir.
        -intentos_restantes: esta entrada me permitrá decir cuantos intentos quedan
    -Salidas:
        -resultado: Cadena de texto que le dara pistas para continuar con el juego
    """
    if intento == numero_secreto:
        resultado = "Has adivinado el número"
        return resultado
    elif intentos_restantes == 0:
        print("Perdiste. El número secreto era ",numero_secreto," Mejor suerte la próxima vez.")
        return
    else:
        resultado = ""
        if intento[0] in numero_secreto:
            if intento[0] in numero_secreto and intento[0] == numero_secreto[0]:
                resultado += "Pin"
            else:
                resultado += "Pon"
        if intento[0] not in numero_secreto:
            resultado += "-"
        if intento[1] in numero_secreto:
            if intento[1] in numero_secreto and intento[1] == numero_secreto[1]:
                resultado += "Pin"
            else:
                resultado += "Pon"
        if intento[1] not in numero_secreto:
            resultado += "-"
        if intento[2] in numero_secreto:
            if intento[2] in numero_secreto and intento[2] == numero_secreto[2]:
                resultado += "Pin"
            else:
                resultado += "Pon"
        if intento[2] not in numero_secreto:
            resultado += "-"
        print(resultado)
        
        print("Quedan ",intentos_restantes," intentos")
        nuevo_intento = input("Introduce tu próximo intento de adivinar el número: ")
        verificar_intentos(numero_secreto, nuevo_intento, intentos_restantes - 1)#Con este llamado hago que se repita la función, pero restandole 1 intento cada vez que se ejecute





