#Ejercicio 1
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P")
def no_p (archivo, letra):
    suma = 0
    with open(archivo, "r") as f:
        for linea in f:
            if linea[0] != letra:
                suma += 1
            else:
                return suma

print (no_p)

print (no_p("bio.txt", "m"))

#Ejercicio 2
#Escribí un programa que lea un archivo e imprima las primeras n líneas.
def imprimir (archivo, lineas):
    contador = lineas - 1
    with open (archivo, "r") as f:
        listas = f.readlines()
        print (listas[:contador + 1])

print(imprimir("bio.txt",1))

#Ejercicio 3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
def guardar (archivo, lineas):
    lista =[]
    with open (archivo, "r") as f:
        for i in f:
            lista.append (i)
    print(lista[-lineas:])

print (guardar ("bio.txt",3))

#Ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
def contar (archivo):
    with open (archivo, "r") as f:
        lista_palabras = f.read().split()
        print(len(lista_palabras))

print (contar("bio.txt"))

#Ejercicio 5
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
def susti(archivo1, archivo2):
    with open(archivo1, "r") as f, open (archivo2, "w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write (letra.replace(letra, letra + "\n"))

#Ejercicio 7
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
def palabra_larga(archivo):
    caracteres = 0
    palabra =""
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > caracteres:
                caracteres = len (word)
                palabra = word
    return palabra, caracteres

print (palabra_larga("bio.txt"))

#Ejercicio 9
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo.
#Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.
def world_counter(archivo):
    frecuencias = {}
    with open (archivo, "r") as arc:
        word_list = arc.read().split()
        for palabra in word_list:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
        for word in frecuencias.keys():
            frecuencias [word] = round (frecuencias[word]/ len(word_list),3)

print(world_counter("messi.txt"))

#Ejercicio 10
#Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
import glob
import os 
def funcion1 (archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob ("*.txt")

    with open (archivo, "a") as s:
        for f in lista_txt:
            file = open (f,"r")
            s.write(file.read())
            file.close()