"""
Author: Juan Quenguan
Code: 2460557
"""
def determinarDia(num):
    """
    Determina que día corresponde con cada número
    Parametros:
    num --> entero
    Retorno:
    dia --> string
    """
    if num == 1:
        dia = "Lunes"
    elif num ==2:
        dia = "Martes"
    elif num ==3:
        dia = "Miercoles"
    elif num ==4:
        dia = "Jueves"
    elif num ==5:
        dia = "Viernes"
    elif num ==6:
        dia = "Sabado"
    else:
        dia = "Domingo"

    return dia
print(determinarDia(1))
