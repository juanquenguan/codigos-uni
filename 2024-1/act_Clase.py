"""
    Clase 19/03
    Codigo: 2460557
"""
import funciones_aux as function

def principal():
    """
    Función principal que pide el día y se asegura que
    sea un número valido.
    """
    numDia = int(input("Dígite un número del 1 al 7: "))

    if numDia>=1 and numDia<=7:
        function.determinarDia(numDia)
    else:
        print("No es un número valido")
        numDia = int(input("Dígite un número del 1 al 7: "))
        if numDia>=1 and numDia<=7:
            print(function.determinarDia(numDia))
        else:
            print("No es un número valido")


principal()
