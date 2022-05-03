#(Manejo de archivos)
#Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada Resultado y, por
#otro, que lea todos los archivos con extensión . txt y escriba el contenido de todos en un único archivo llamado
#texto completo.txt, que tiene que estar dentro de la carpeta Resultado. NO se pueden usar rutas absolutas

import os, glob

def unir_txt():
    os.mkdir("Resultado")
    lista_txt = glob.glob ("*.txt")
    salida = open ("Resultado/texto_completo.txt", "a")
    for txt in lista_txt:
        archivo = open (txt, "r")
        salida.write (archivo.read())
        archivo.close()
    salida.close()
