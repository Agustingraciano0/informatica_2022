#(Manejo de exepciones) Ejecutá el script_misterioso.py y realizá resolvé: 
# 1. ¿Qué tipo de exepción arroja la corrida del script? 
# 2. Mejorá el código para que capture dicho error especificamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error 
# 3. ¿Qué otras excepciones deberias considerar?

#1. ZeroDivisionError
#2. 
def obtener_media(lista):
    sumatoria = 0

    for valor in lista :

        sumatoria += valor
    longitud = len (lista)

    try:
        return sumatoria / longitud
    except ZeroDivisionError:
        print("No se puede dividir por cero")

