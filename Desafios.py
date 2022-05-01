#Expresiones regulares
#Desafio 1
#Construí la expresión regular que obtenga al menos 4 dígitos
"""\d{4,}"""
#Desafio 2
#Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas
"""[a-z]{3,6}"""
#Desafio 3
#Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string
"""ab*"""
#Desafio 4
#Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:

texto = 'En la clase de Introducción a la programación hay 30 estudiantes'
"\d+"
#Desafio 5
#imprimí el fragmento del texto entre la posición 22 y 26 
texto1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
print(texto1[22:26])
#Desafio 6
#Expresá el patron de búsqueda utilizando lo visto anteriormente sobre metacaracteres y rangos.
import re
print(re.findall(r"amet", texto1))


#Manipulacion de Archivos
#Desafio 1
#Descargá y ejecutá el script1_manejo_errores.py
#Desafio 2
#Creá una función denominada mitades que tenga como argumento un número e imprima el resultado de la división de ese número por 2
def mitades(numero):
    return numero/2
#Desafio 3
#Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except
def mitades(numero):
    try:
        return numero/2
    except TypeError:
        print("El argumento debe ser un número")
    except:
        print("No se puede dividir")
        