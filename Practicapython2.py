#Ejercicio 1
#Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.
def mayuscula_o_minuscula(palabra):
    if palabra[0] == str.upper(palabra[0]):
        return "Mayuscula"
    elif palabra[0] == str.lower(palabra[0]):
        return "Minuscula"
print(mayuscula_o_minuscula("Messi"))
print(mayuscula_o_minuscula("messi"))


#Ejercicio 2
#Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

def positivo_negativo(numero):
    resultado = ""
    if numero < 0:
        resultado += "Negativo"
    elif numero > 0:
        resultado += "Positivo"
    else:
        resultado += "Cero"
    return resultado + " " + par_o_impar(numero)

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
print(positivo_negativo(4))


#Ejercicio 3
#Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado.
#Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.
def numero_opuesto(numero):
    if 1 <= numero <= 6:
        return 7 - numero
    else:
        return "El numero ingresado es incorrecto"
print(numero_opuesto(6))
print(numero_opuesto(10))


#Ejercicio 4
def cobro_paquete(ubicación, peso):
    if peso > 5:
        return "Entrega rechazada"
    elif ubicación == "América del sur":
        return peso * 10.00
    elif ubicación == "América central":
        return peso * 15.00
    elif ubicación == "América del norte":
        return peso * 18.00 
    elif ubicación == "Europa":
        return peso * 24.00 
    elif ubicación == "Asia":
        return peso * 30.00
print(cobro_paquete("Asia", 4))


#Ejercicio 5
#Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
# Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.
def dia_semana(numero):
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miercoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sabado")
    elif numero == 7:
        print("Domingo")
    else:
        print("El numero es incorrecto")
dia_semana(3)
dia_semana(20)


#Ejercicio 6
#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
lista1 = ["messi"]
lista2 = list(reversed(lista1))
print(lista2)


#Ejercicio 7
#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. 
# Una vez hecho esto se deben imprimir los elementos de la lista

lista_numero = []
numero = int(input("dame un numero"))

while numero >= 0:
    lista_numero.append(numero)
    numero = int(input("dame un numero"))
    if numero < 0:
        print (lista_numero)

#otra forma
lista7=[]
def agregar_num(num):
  if num > 0:
    return list.append(lista7,num)
  else:
    print(lista7)




#Ejercicio 8
#Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una
#por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 
# (es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)

def suma_de_listas(lista11, lista22):
    lista33 = [lista11[0] + lista22[0], lista11[1] + lista22[1], lista11[2] + lista22[2], lista11[3] + lista22[3], lista11[4] + lista22[4]]
    return lista33
print(suma_de_listas([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))


#Ejercicio 9 
#Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada alumno por teclado.
#El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:
#La edad máxima de todos los alumnos.
#Los alumnos que tengan la edad máxima

listanombres=[]
listaedades = []

while True:
    nombre = input ("Nombre: ")
    if nombre != "*":
        listanombres.append(nombre)
        listaedades.append(int(input("Edad: ")))
    if nombre == "*": break; 

edad_max_alumnos = max (listaedades)

    for nombre, edad in zip(listanombres, listaedades):
        if edad == edad_max_alumnos:
            print ("Almuno en edad maxima:", (nombre))

 print ("Edad maxima es", (edad_max_alumnos))


#Ejercicio 10
#Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena 
#considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

def letra(string):
    diccionario = {}
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra("bebet benedetto"))


#Ejercicio 11
#Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
diccionario = {}
for letra in alfabeto + alfabeto.upper():
    diccionario[letra] = 0 
def letra2(string):
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra2("lionel andres messi"))


#Ejercicio 12
#Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas
#Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno
#El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo
# Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.







#Ejercicio 13
#Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
def esMultiplo(numero1, numero2):
    return numero1 % numero2 == 0 or numero2 % numero1 == 0
print(esMultiplo(2, 4))


#Ejercicio 14
#Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
#El programa tiene que pedir el número de días que se van a introducir.
def temperatura_media(max, min):
    return (max + min) / 2
print(temperatura_media(20, 4))



#Ejercicio 15
#Creá un programa para gestionar datos de los socios de un club, el cual permita:
#Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). 
#El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:
#Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día
#Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día
#Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

#Informar la cantidad de socios que tiene el club.
#Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.
#Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.
#Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).
#Imprimir el listado de socios completos.

def cargarSocios(socios):
    numero = int(input("Número de socio: "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso: ")
        cuota = input("¿Cuota al día? s/n: ")
        pago = cuota.lower() == "s"
        socios[numero] = [nombre, fecha, pago]
        numero = int(input("Número de socio: "))
    return socios
def modificarFecha(socios, fechaAnterior, fechaNueva):
    for datos in socios.values():
        if datos[1] == fechaAnterior:datos[1] = fechaNueva
    return socios
def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower() == nombre.lower():
            return numero
            return 0
def formatoFecha(fecha):
    return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]
def imprimirListado(socios):
    for numero,datos in socios.items():
        print("Número: ", numero)
        print("Nombre: ", datos[0])
        print("Fecha de ingreso ", formatoFecha(datos[1]))
        if datos[2]:
            print("Cuota al día")
        else:
            print("En deuda")
            print("---------------")
        return None
    socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}
    print("Cargar socios")
    socios_activos = cargarSocios(socios_activos)
    print("El club tiene", len(socios_activos), "socios")
    print("Registrar pago de cuotas")
    numero = int(input("Numero de socio: "))
    socios_activos[numero][2] = True 
    print("Modificando fecha de ingreso...")
    socios_activos = modificarFecha(socios_activos, "21102017", "22102017")
    print("Eliminar socio:")
    nombre = input("Nombre y apellido: ")
    numero = numeroSocio(socios_activos, nombre)
    del socios_activos[numero]
    imprimirListado(socios_activos)