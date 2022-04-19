#Ejercico 1
import re
def caracteres_permitidos (palabra):
    return bool(re.search("[a-zA-Z0-9.]",palabra))

print (caracteres_permitidos ("///"))
print (caracteres_permitidos ("AGus"))

#Ejercicio 2
import re 
def tiene_caracteres (string):
    return bool(re.findall("[^a-zA-Z0-9.]",string))

print (tiene_caracteres("agus"))

#Ejercicio 3
def con_he (string):
    return bool(re.search("he+", string))

print (con_he("heermano"))
print (con_he("hola"))

def dos_tres (string):
    return bool(re.search ("he{2,3}", string))

print (dos_tres ("heermano"))

#Ejercicio 4
import re
def unidas_(string,palabra1,palabra2):
    return bool(re.search(palabra1 + " _ " + palabra2, string))

print (unidas_("buenas_tardes che", "tardes","che"))
print (unidas_("buenas tardes_che", "tardes", "che"))

#Ejercicio 5
import re
def comienza_con (numero,string):
    return bool(re.match(str(numero),string))

print(comienza_con(9," 8lindo"))
print(comienza_con(8, "8lindo"))

#Ejercicio 6
import re
def lista_en_frase (lista, frase):
    return bool(re.search (lista in frase))

lista1 = ["hola", "chau", "buenas"]

print (lista_en_frase(lista1, "hola buenas chau"))

#Ejercicio 8
import re 
def solo_numeros (string):
    return re.findall ("[0-9]",string)

print(solo_numeros("1234 es hoy 23"))

#Ejercicio 9
import re
def entre_guiones(string):
    return(re.findall("-.*-",string))

print(entre_guiones("Trabajamos con re - regular expresiones"))

#Ejercicio 10


#Ejercicio 11
import re
def comienza_con_P (lista_string):
    return (re.findall ("[^P]",lista_string))

lista1 = ["practica Python", "Practica C++", "Practica Fortran"]
print (comienza_con_P (lista1))

#Ejercicio 12
sustituir = [" ", "_",":"]
import re
def reemplazar(string):
    return re.sub(sustituir, "|", string)

print (reemplazar("hola como va"))

#Ejercicio 14
import re 
def reemplazar (string):
    return re.sub("\s",":",string)

print (reemplazar("hola como\e\s\ tas"))

#Ejercicio 15



