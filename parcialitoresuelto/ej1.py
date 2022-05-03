#Consigna N1 (RE) Escribir funciones que dado un string, permitan obterner

#Cuantas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9 y ninguna en hola amigos mios. 
#La lista de los substrings delimitadso entre "aa" y "gg" que no inculyan ninguna "c". P.ej. en "ttaatatggttaacatgg", debe tomar solamente "tat", rechazando "cat"

import re

def cuantas_veces(string):
    resultado = re.findall("bc9",string)
    return len(resultado)

def sin_c (string):
    return re.findall("aa([^c]*?)gg", string)

"""el ? favorece los matches interno"""

print(sin_c("ttaatatggttaacatgg"))
print(cuantas_veces("xsabc9cabcb3sabc9 "))

